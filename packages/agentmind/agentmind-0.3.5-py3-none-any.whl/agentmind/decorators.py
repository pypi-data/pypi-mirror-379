"""
Decorators for AgentMind functionality including billing enforcement.
"""

from functools import wraps
from typing import Callable, Any
from .billing import BillingError


def enforce_memory_limit(func: Callable) -> Callable:
    """
    Decorator to enforce memory limits on memory storage operations.

    Usage:
        @enforce_memory_limit
        def store_memory(self, content):
            # Your memory storage logic
            pass
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        # Check if the object has subscription_manager
        if hasattr(self, 'subscription_manager') and self.subscription_manager:
            # Check limits before executing the function
            self.subscription_manager.check_memory_limit()

        # Execute the original function
        result = func(self, *args, **kwargs)

        # Record usage after successful execution
        if hasattr(self, 'subscription_manager') and self.subscription_manager:
            # Try to estimate memory size from content
            content = None
            if args:
                content = args[0]
            elif 'content' in kwargs:
                content = kwargs['content']

            if content:
                try:
                    memory_size = len(str(content).encode('utf-8'))
                    self.subscription_manager.record_memory_added(memory_size)
                except:
                    # If we can't calculate size, record with 0 bytes
                    self.subscription_manager.record_memory_added(0)

        return result

    return wrapper


def requires_pro_tier(func: Callable) -> Callable:
    """
    Decorator to restrict function access to PRO tier and above.

    Usage:
        @requires_pro_tier
        def advanced_feature(self):
            # Feature only available to PRO+ users
            pass
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        if hasattr(self, 'subscription_manager') and self.subscription_manager:
            from .billing import SubscriptionTier
            if self.subscription_manager.tier == SubscriptionTier.STARTER:
                raise BillingError(
                    "This feature requires PRO subscription or higher. "
                    "Please upgrade your subscription to access this feature."
                )

        return func(self, *args, **kwargs)

    return wrapper


def requires_enterprise_tier(func: Callable) -> Callable:
    """
    Decorator to restrict function access to ENTERPRISE tier only.

    Usage:
        @requires_enterprise_tier
        def enterprise_feature(self):
            # Feature only available to ENTERPRISE users
            pass
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        if hasattr(self, 'subscription_manager') and self.subscription_manager:
            from .billing import SubscriptionTier
            if self.subscription_manager.tier != SubscriptionTier.ENTERPRISE:
                raise BillingError(
                    "This feature requires ENTERPRISE subscription. "
                    "Please contact sales for enterprise pricing."
                )

        return func(self, *args, **kwargs)

    return wrapper


def track_api_usage(endpoint: str) -> Callable:
    """
    Decorator to track API endpoint usage for analytics.

    Usage:
        @track_api_usage("memory.recall")
        def recall(self, query):
            # Your recall logic
            pass
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs) -> Any:
            # Here you could add logging, metrics, etc.
            # For now, just execute the function
            return func(self, *args, **kwargs)

        return wrapper

    return decorator