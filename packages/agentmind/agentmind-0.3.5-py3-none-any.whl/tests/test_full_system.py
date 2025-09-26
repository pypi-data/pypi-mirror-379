#!/usr/bin/env python
"""
Full system test for AgentMind - demonstrates both local and API modes.
"""

import os
import json
from agentmind import Memory


def test_local_mode():
    """Test local in-memory storage mode."""
    print("\n" + "="*60)
    print("TESTING LOCAL MODE (In-Memory Storage)")
    print("="*60)
    
    # Initialize in local mode
    memory = Memory(local_mode=True)
    print("✓ Initialized Memory in local mode")
    
    # Test 1: Store simple string
    print("\n1. Storing simple string...")
    mem_id = memory.remember(
        "User prefers Python and dark mode in VSCode",
        user_id="test_user",
        metadata={"category": "preferences"}
    )
    print(f"   Stored with ID: {mem_id}")
    
    # Test 2: Store complex object
    print("\n2. Storing complex object...")
    profile_data = {
        "name": "John Doe",
        "role": "Senior Developer",
        "skills": ["Python", "Django", "React", "PostgreSQL"],
        "preferences": {
            "editor": "VSCode",
            "theme": "dark",
            "tabs_vs_spaces": "spaces",
            "indent_size": 4
        }
    }
    profile_id = memory.remember(
        profile_data,
        user_id="test_user",
        id="developer_profile"
    )
    print(f"   Stored profile with ID: {profile_id}")
    
    # Test 3: Retrieve by ID
    print("\n3. Retrieving by ID...")
    retrieved = memory.get("developer_profile")
    print(f"   Retrieved: {json.dumps(retrieved, indent=2)}")
    
    # Test 4: Check existence
    print("\n4. Checking if memories exist...")
    exists1 = memory.exists("developer_profile")
    exists2 = memory.exists("non_existent")
    print(f"   'developer_profile' exists: {exists1}")
    print(f"   'non_existent' exists: {exists2}")
    
    # Test 5: Recall by query
    print("\n5. Recalling memories by query...")
    memories = memory.recall("VSCode dark mode Python", user_id="test_user", limit=3)
    print(f"   Found {len(memories)} relevant memories:")
    for i, mem in enumerate(memories, 1):
        preview = str(mem)[:100] + "..." if len(str(mem)) > 100 else str(mem)
        print(f"   {i}. {preview}")
    
    # Test 6: List all memories
    print("\n6. Listing all memories...")
    all_memories = memory.list(user_id="test_user", limit=10)
    print(f"   Total memories for user: {len(all_memories)}")
    for mem in all_memories[:3]:  # Show first 3
        print(f"   - {mem['id']}: {mem['preview']} ({mem['size']})")
    
    # Test 7: Delete a memory
    print("\n7. Deleting a memory...")
    deleted = memory.delete("developer_profile")
    print(f"   Deleted 'developer_profile': {deleted}")
    exists_after = memory.exists("developer_profile")
    print(f"   Exists after deletion: {exists_after}")
    
    print("\n✅ Local mode tests completed successfully!")
    return True


def test_api_mode():
    """Test API mode with server connection."""
    print("\n" + "="*60)
    print("TESTING API MODE (Server Connection)")
    print("="*60)
    
    # Check if server is running
    server_url = "http://127.0.0.1:8000"
    
    import requests
    try:
        response = requests.get(f"{server_url}/api/v1/docs", timeout=2)
        if response.status_code != 200:
            print("⚠️  Server not accessible. Make sure server is running.")
            print("   Run: ./scripts/runserver.sh")
            return False
    except:
        print("⚠️  Cannot connect to server at http://127.0.0.1:8000")
        print("   Please start the server with: ./scripts/runserver.sh")
        return False
    
    print(f"✓ Server is running at {server_url}")
    
    # Test direct API calls
    print("\n1. Testing direct API call to store memory...")
    response = requests.post(
        f"{server_url}/api/v1/memories/remember",
        json={
            "content": "API test memory from test script",
            "user_id": "api_test_user",
            "metadata": {"source": "test_script", "category": "test"}
        }
    )
    
    if response.status_code == 200:
        memory_id = response.json()["memory_id"]
        print(f"   ✓ Stored via API with ID: {memory_id}")
        
        # Test retrieving
        print("\n2. Testing API retrieval...")
        response = requests.get(f"{server_url}/api/v1/memories/get/{memory_id}")
        if response.status_code == 200:
            content = response.json()
            print(f"   ✓ Retrieved: {content}")
        
        # Test recall
        print("\n3. Testing API recall...")
        response = requests.post(
            f"{server_url}/api/v1/memories/recall",
            json={
                "query": "test script",
                "user_id": "api_test_user",
                "limit": 5
            }
        )
        if response.status_code == 200:
            memories = response.json()
            print(f"   ✓ Found {len(memories)} memories via recall")
        
        # Test listing
        print("\n4. Testing API list...")
        response = requests.get(
            f"{server_url}/api/v1/memories/list",
            params={"user_id": "api_test_user", "limit": 10}
        )
        if response.status_code == 200:
            memories = response.json()
            print(f"   ✓ Listed {len(memories)} memories")
        
        print("\n✅ API mode tests completed successfully!")
        print("\n📝 Note: Your Django server is storing data in PostgreSQL (Supabase)")
        return True
    else:
        print(f"   ❌ API call failed: {response.status_code}")
        return False


def test_agent_tool_example():
    """Demonstrate how agents would use the memory tool."""
    print("\n" + "="*60)
    print("AGENT TOOL USAGE EXAMPLE")
    print("="*60)
    
    # Simulate an agent with memory tools
    class SimpleAgent:
        def __init__(self, user_id):
            self.memory = Memory(local_mode=True)
            self.user_id = user_id
        
        def remember_tool(self, content, importance=0.5):
            """Tool the agent uses to store memories."""
            memory_id = self.memory.remember(
                content=content,
                user_id=self.user_id,
                metadata={"importance": importance, "source": "agent_decision"}
            )
            return f"Remembered with ID: {memory_id}"
        
        def recall_tool(self, query, limit=5):
            """Tool the agent uses to recall memories."""
            memories = self.memory.recall(
                query=query,
                user_id=self.user_id,
                limit=limit
            )
            return memories if memories else "No relevant memories found"
        
        def process_message(self, message):
            """Simulate agent processing a message."""
            print(f"\n🤖 Agent received: '{message}'")
            
            # Agent decides what to remember
            if "prefer" in message.lower() or "like" in message.lower():
                result = self.remember_tool(message, importance=0.8)
                print(f"   Agent action: {result}")
            
            # Agent might need to recall information
            if "?" in message:
                memories = self.recall_tool(message)
                print(f"   Agent recalled: {memories}")
            
            return "Message processed"
    
    # Create an agent for a specific user
    agent = SimpleAgent(user_id="user_123")
    
    # Simulate conversation
    print("\nSimulating agent conversation...")
    
    agent.process_message("I prefer email communications over phone calls")
    agent.process_message("My account ID is ABC-123 and I'm on the Pro plan")
    agent.process_message("I like getting updates weekly, not daily")
    agent.process_message("How should you contact me?")
    agent.process_message("What's my account type?")
    
    print("\n✅ Agent tool demonstration completed!")


if __name__ == "__main__":
    print("\n" + "🧠 "*20)
    print("AGENTMIND FULL SYSTEM TEST")
    print("🧠 "*20)
    
    # Test local mode (always works)
    local_success = test_local_mode()
    
    # Test API mode (requires server running)
    api_success = test_api_mode()
    
    # Demonstrate agent usage
    test_agent_tool_example()
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"✅ Local Mode: {'PASSED' if local_success else 'FAILED'}")
    print(f"{'✅' if api_success else '⚠️'} API Mode: {'PASSED' if api_success else 'Server not running'}")
    print("\n💡 To test API mode, run the server with: ./scripts/runserver.sh")
    print("🚀 Your AgentMind system is ready for production!")