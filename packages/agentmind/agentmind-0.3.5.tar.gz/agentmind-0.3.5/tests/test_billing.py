"""
Tests for billing and subscription management functionality.
"""

import pytest
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from agentmind.core.memory import Memory
from agentmind.billing import (
    SubscriptionTier,
    TierLimits,
    UsageTracker,
    BillingError,
    SubscriptionManager
)


class TestTierLimits:
    """Test subscription tier limits configuration."""

    def test_starter_limits(self):
        """Test Starter tier limits."""
        limits = TierLimits.get_limits(SubscriptionTier.STARTER)
        assert limits.memory_limit == 100
        assert limits.storage_limit_gb == 2
        assert limits.token_compression is False
        assert limits.graph_knowledge is False
        assert limits.priority_support is False

    def test_pro_limits(self):
        """Test Pro tier limits."""
        limits = TierLimits.get_limits(SubscriptionTier.PRO)
        assert limits.memory_limit == 1000
        assert limits.storage_limit_gb == 10
        assert limits.token_compression is True
        assert limits.graph_knowledge is True
        assert limits.priority_support is True

    def test_enterprise_limits(self):
        """Test Enterprise tier limits."""
        limits = TierLimits.get_limits(SubscriptionTier.ENTERPRISE)
        assert limits.memory_limit == 100000
        assert limits.storage_limit_gb == 2048
        assert limits.token_compression is True
        assert limits.graph_knowledge is True
        assert limits.priority_support is True


class TestUsageTracker:
    """Test usage tracking functionality."""

    def setup_method(self):
        """Setup test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.user_id = "test_user_123"
        self.tracker = UsageTracker(self.user_id, self.temp_dir)

    def teardown_method(self):
        """Cleanup test environment."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization(self):
        """Test usage tracker initialization."""
        assert self.tracker.user_id == self.user_id
        assert self.tracker.usage_file.exists()

        # Check initial data
        usage = self.tracker.get_current_usage()
        assert usage["memories_this_month"] == 0
        assert usage["storage_gb"] == 0
        assert usage["total_memories"] == 0

    def test_increment_memory_count(self):
        """Test incrementing memory count."""
        self.tracker.increment_memory_count()
        usage = self.tracker.get_current_usage()
        assert usage["memories_this_month"] == 1
        assert usage["total_memories"] == 1

        self.tracker.increment_memory_count(5)
        usage = self.tracker.get_current_usage()
        assert usage["memories_this_month"] == 6
        assert usage["total_memories"] == 6

    def test_update_storage(self):
        """Test storage usage tracking."""
        # Add 1MB of storage
        self.tracker.update_storage(1024 * 1024)
        usage = self.tracker.get_current_usage()
        assert abs(usage["storage_gb"] - 0.001) < 0.0001  # ~1MB in GB

        # Add another 1GB
        self.tracker.update_storage(1024 * 1024 * 1024)
        usage = self.tracker.get_current_usage()
        assert abs(usage["storage_gb"] - 1.001) < 0.0001

    def test_month_reset(self):
        """Test monthly counter reset."""
        # Add some memories
        self.tracker.increment_memory_count(50)
        usage = self.tracker.get_current_usage()
        assert usage["memories_this_month"] == 50

        # Simulate month change
        from datetime import datetime, timedelta
        past_month = (datetime.now() - timedelta(days=32)).strftime("%Y-%m")
        self.tracker.usage_data["current_month"] = past_month
        self.tracker._save_usage()

        # Check month should trigger reset
        self.tracker._check_month_reset()
        usage = self.tracker.get_current_usage()
        assert usage["memories_this_month"] == 0
        assert usage["total_memories"] == 50  # Total should remain

    def test_can_add_memory(self):
        """Test memory limit checking."""
        limits = TierLimits.get_limits(SubscriptionTier.STARTER)

        # Should be able to add initially
        can_add, error = self.tracker.can_add_memory(limits)
        assert can_add is True
        assert error is None

        # Set near limit
        self.tracker.usage_data["memories_this_month"] = 99
        self.tracker._save_usage()
        can_add, error = self.tracker.can_add_memory(limits)
        assert can_add is True

        # Set at limit
        self.tracker.usage_data["memories_this_month"] = 100
        self.tracker._save_usage()
        can_add, error = self.tracker.can_add_memory(limits)
        assert can_add is False
        assert "Monthly memory limit reached" in error

        # Test storage limit
        self.tracker.usage_data["memories_this_month"] = 0
        self.tracker.usage_data["storage_bytes"] = 3 * 1024 * 1024 * 1024  # 3GB
        self.tracker._save_usage()
        can_add, error = self.tracker.can_add_memory(limits)
        assert can_add is False
        assert "Storage limit reached" in error


class TestSubscriptionManager:
    """Test subscription management functionality."""

    def setup_method(self):
        """Setup test environment."""
        self.temp_dir = tempfile.mkdtemp()
        # Use unique user ID for each test to avoid cross-test contamination
        import uuid
        self.user_id = f"test_user_{uuid.uuid4().hex[:8]}"

    def teardown_method(self):
        """Cleanup test environment."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization(self):
        """Test subscription manager initialization."""
        with patch.dict(os.environ, {"HOME": self.temp_dir}):
            manager = SubscriptionManager(self.user_id)
            assert manager.user_id == self.user_id
            assert manager.tier == SubscriptionTier.STARTER
            assert manager.limits.memory_limit == 100

    def test_check_memory_limit_success(self):
        """Test successful memory limit check."""
        manager = SubscriptionManager(self.user_id)
        # Should not raise
        manager.check_memory_limit()

    def test_check_memory_limit_exceeded(self):
        """Test memory limit exceeded."""
        manager = SubscriptionManager(self.user_id)
        # Set at limit
        manager.usage_tracker.usage_data["memories_this_month"] = 100
        manager.usage_tracker._save_usage()

        with pytest.raises(BillingError) as exc_info:
            manager.check_memory_limit()
        assert "Monthly memory limit reached" in str(exc_info.value)

    def test_record_memory_added(self):
        """Test recording memory addition."""
        manager = SubscriptionManager(self.user_id)

        # Record memory with size
        manager.record_memory_added(1024)
        usage = manager.usage_tracker.get_current_usage()
        assert usage["memories_this_month"] == 1
        assert usage["storage_gb"] > 0

    def test_get_usage_stats(self):
        """Test getting usage statistics."""
        manager = SubscriptionManager(self.user_id, SubscriptionTier.PRO)

        # Add some usage
        manager.record_memory_added(1024 * 1024)  # 1MB
        manager.record_memory_added(1024 * 1024)  # 1MB

        stats = manager.get_usage_stats()
        assert stats["tier"] == "pro"
        assert stats["usage"]["memories_this_month"] == 2
        assert stats["limits"]["memory_limit"] == 1000
        assert stats["remaining"]["memories"] == 998
        assert stats["features"]["token_compression"] is True

    def test_upgrade_tier(self):
        """Test tier upgrade."""
        manager = SubscriptionManager(self.user_id, SubscriptionTier.STARTER)
        assert manager.limits.memory_limit == 100

        # Upgrade to Pro
        manager.upgrade_tier(SubscriptionTier.PRO)
        assert manager.tier == SubscriptionTier.PRO
        assert manager.limits.memory_limit == 1000
        assert manager.limits.token_compression is True


class TestMemoryBillingIntegration:
    """Test Memory class with billing integration."""

    def test_memory_without_billing(self):
        """Test Memory works without billing configured."""
        memory = Memory(local_mode=True)
        memory_id = memory.remember("Test memory")
        assert memory_id is not None

    def test_memory_with_billing(self):
        """Test Memory with billing enabled."""
        memory = Memory(
            local_mode=True,
            user_id="test_user",
            subscription_tier=SubscriptionTier.STARTER,
            enforce_limits=True
        )

        # Should be able to add memories
        memory_id = memory.remember("Test memory")
        assert memory_id is not None

        # Check usage
        stats = memory.get_usage_stats()
        assert stats["usage"]["memories_this_month"] == 1

    def test_memory_limit_enforcement(self):
        """Test memory limit is enforced."""
        memory = Memory(
            local_mode=True,
            user_id="limited_user",
            subscription_tier=SubscriptionTier.STARTER,
            enforce_limits=True
        )

        # Manually set near limit
        memory.subscription_manager.usage_tracker.usage_data["memories_this_month"] = 100
        memory.subscription_manager.usage_tracker._save_usage()

        # Should raise BillingError
        with pytest.raises(BillingError):
            memory.remember("This should fail")

    def test_memory_no_enforcement(self):
        """Test Memory with enforcement disabled."""
        memory = Memory(
            local_mode=True,
            user_id="unlimited_user",
            subscription_tier=SubscriptionTier.STARTER,
            enforce_limits=False
        )

        # Should be able to add unlimited memories
        for i in range(150):  # More than starter limit
            memory_id = memory.remember(f"Memory {i}")
            assert memory_id is not None

    def test_get_usage_stats_not_configured(self):
        """Test getting usage stats when billing not configured."""
        memory = Memory(local_mode=True)

        with pytest.raises(ValueError) as exc_info:
            memory.get_usage_stats()
        assert "Billing not configured" in str(exc_info.value)


class TestBillingDecorators:
    """Test billing decorators."""

    def test_enforce_memory_limit_decorator(self):
        """Test @enforce_memory_limit decorator."""
        from agentmind.decorators import enforce_memory_limit

        class MockMemoryClass:
            def __init__(self, has_manager=True, at_limit=False):
                if has_manager:
                    self.subscription_manager = Mock()
                    if at_limit:
                        self.subscription_manager.check_memory_limit.side_effect = BillingError("Limit reached")
                    else:
                        self.subscription_manager.check_memory_limit.return_value = None
                    self.subscription_manager.record_memory_added = Mock()

            @enforce_memory_limit
            def store(self, content):
                return f"stored: {content}"

        # Test with subscription manager
        obj = MockMemoryClass()
        result = obj.store("test content")
        assert result == "stored: test content"
        obj.subscription_manager.check_memory_limit.assert_called_once()
        obj.subscription_manager.record_memory_added.assert_called_once()

        # Test at limit
        obj_limited = MockMemoryClass(at_limit=True)
        with pytest.raises(BillingError):
            obj_limited.store("test content")

        # Test without subscription manager
        obj_no_manager = MockMemoryClass(has_manager=False)
        result = obj_no_manager.store("test content")
        assert result == "stored: test content"

    def test_requires_pro_tier_decorator(self):
        """Test @requires_pro_tier decorator."""
        from agentmind.decorators import requires_pro_tier

        class MockClass:
            def __init__(self, tier=SubscriptionTier.STARTER):
                self.subscription_manager = Mock()
                self.subscription_manager.tier = tier

            @requires_pro_tier
            def pro_feature(self):
                return "pro feature executed"

        # Test with Starter tier (should fail)
        obj_starter = MockClass(SubscriptionTier.STARTER)
        with pytest.raises(BillingError) as exc_info:
            obj_starter.pro_feature()
        assert "requires PRO subscription" in str(exc_info.value)

        # Test with Pro tier (should work)
        obj_pro = MockClass(SubscriptionTier.PRO)
        result = obj_pro.pro_feature()
        assert result == "pro feature executed"

        # Test with Enterprise tier (should work)
        obj_enterprise = MockClass(SubscriptionTier.ENTERPRISE)
        result = obj_enterprise.pro_feature()
        assert result == "pro feature executed"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])