#!/usr/bin/env python
"""
Test script to verify AgentMind integration with Django backend.
"""

from agentmind import Memory

def test_memory_operations():
    """Test basic memory operations."""
    print("Testing AgentMind with Django backend...")
    
    # Initialize memory with local mode (will use Django if available)
    memory = Memory(local_mode=True)
    
    # Test 1: Store a simple memory
    print("\n1. Storing a memory...")
    memory_id = memory.remember(
        "User prefers dark mode and uses VSCode",
        user_id="test_user",
        metadata={"category": "preferences"}
    )
    print(f"   Stored with ID: {memory_id}")
    
    # Test 2: Store a complex object
    print("\n2. Storing complex data...")
    memory_id2 = memory.remember(
        {
            "name": "John Doe",
            "preferences": {
                "editor": "VSCode",
                "theme": "dark",
                "language": "Python"
            },
            "skills": ["Python", "Django", "React"]
        },
        user_id="test_user",
        id="user_profile"
    )
    print(f"   Stored profile with ID: {memory_id2}")
    
    # Test 3: Retrieve by ID
    print("\n3. Retrieving by ID...")
    profile = memory.get("user_profile")
    print(f"   Retrieved: {profile}")
    
    # Test 4: Check existence
    print("\n4. Checking existence...")
    exists = memory.exists("user_profile")
    print(f"   'user_profile' exists: {exists}")
    
    # Test 5: Recall by query
    print("\n5. Recalling memories about preferences...")
    memories = memory.recall("dark mode VSCode", user_id="test_user")
    for i, mem in enumerate(memories, 1):
        print(f"   {i}. {mem}")
    
    # Test 6: List all memories
    print("\n6. Listing all memories...")
    all_memories = memory.list(user_id="test_user", limit=5)
    for mem in all_memories:
        print(f"   - {mem['id']}: {mem['preview']} ({mem['size']})")
    
    print("\n✅ All tests completed successfully!")

if __name__ == "__main__":
    test_memory_operations()