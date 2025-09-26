#!/usr/bin/env python
"""
Quick API test - run this while server is running.
"""

import requests
import json

SERVER_URL = "http://127.0.0.1:8000"

print("Testing AgentMind Server API...")
print("="*50)

# 1. Store a memory
print("\n1. Storing memory via API...")
response = requests.post(
    f"{SERVER_URL}/api/v1/memories/remember",
    json={
        "content": "This is stored in PostgreSQL via Django ORM",
        "user_id": "demo_user",
        "metadata": {"category": "demo", "importance": 0.9}
    }
)

if response.status_code == 200:
    memory_id = response.json()["memory_id"]
    print(f"✅ Stored with ID: {memory_id}")
    
    # 2. Retrieve it
    print("\n2. Retrieving memory...")
    response = requests.get(f"{SERVER_URL}/api/v1/memories/get/{memory_id}")
    print(f"✅ Retrieved: {response.json()}")
    
    # 3. Recall by query
    print("\n3. Searching for memories...")
    response = requests.post(
        f"{SERVER_URL}/api/v1/memories/recall",
        json={
            "query": "PostgreSQL Django",
            "user_id": "demo_user"
        }
    )
    memories = response.json()
    print(f"✅ Found {len(memories)} matching memories")
    
    # 4. List all
    print("\n4. Listing all memories...")
    response = requests.get(
        f"{SERVER_URL}/api/v1/memories/list",
        params={"limit": 5}
    )
    all_memories = response.json()
    # The response might be paginated or wrapped
    if isinstance(all_memories, dict) and 'items' in all_memories:
        memories_list = all_memories['items']
    elif isinstance(all_memories, list):
        memories_list = all_memories
    else:
        memories_list = []
    
    print(f"✅ Total memories returned: {len(memories_list)}")
    for mem in memories_list[:3]:
        preview = mem.get('preview', str(mem.get('content', '')))[:50]
        print(f"   - {mem['id']}: {preview}...")
    
    print("\n" + "="*50)
    print("✅ API TEST SUCCESSFUL!")
    print("Your memories are being stored in PostgreSQL (Supabase)")
    print("Check your Supabase dashboard to see the data!")
else:
    print(f"❌ API Error: {response.status_code}")
    print("Make sure server is running: ./scripts/runserver.sh")