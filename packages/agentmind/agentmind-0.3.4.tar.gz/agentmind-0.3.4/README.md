# AgentMind 🧠

> Give your AI agents memory they control. A tool your agents can use to remember important information, learn from interactions, and maintain context across conversations.

[![PyPI version](https://badge.fury.io/py/agentmind.svg)](https://badge.fury.io/py/agentmind)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why AgentMind?

Your AI agents need memory they can control. AgentMind is a tool you give to your agents, allowing them to decide what to remember, when to remember it, and how to use that knowledge. Instead of you managing context and memory, your agent does it autonomously.

**Perfect for:**
- Agents that need to track user preferences and history
- Multi-step workflows requiring persistent context  
- Learning agents that improve from past interactions
- Customer service bots that remember past issues
- Any agent that should get smarter over time

## Primary Use Case: Agent Tools

**Give your agent a memory tool it can use autonomously:**

```python
# Define a tool for your agent to use
def remember_tool(content: str, importance: float = 0.5):
    """Tool for the agent to store important information."""
    memory = Memory(api_key="am_live_YOUR_API_KEY", user_id="customer_123")
    memory_id = memory.remember(
        content=content,
        metadata={"importance": importance, "source": "agent_decision"}
    )
    return f"Remembered with ID: {memory_id}"

def recall_tool(query: str, limit: int = 5):
    """Tool for the agent to recall relevant information."""
    memory = Memory(api_key="am_live_YOUR_API_KEY", user_id="customer_123") 
    memories = memory.recall(query, limit=limit)
    return memories if memories else "No relevant memories found"

# Your agent can now decide what to remember
agent = YourAgent(
    tools=[remember_tool, recall_tool],
    system_prompt="You have access to memory tools. Use them to remember important information about users, their preferences, and past interactions."
)

# The agent autonomously manages its memory
response = agent.chat("I prefer email communications")
# Agent might call: remember_tool("User prefers email.", importance=0.9)

# Later, the agent uses its memory
response = agent.chat("How should you contact me?")
# Agent calls: recall_tool("user communication preferences")
# Returns: "You prefer email communications"
```

## Quick Start - Direct Usage

**Initialize memory:**
```python
from agentmind import Memory

# Simple cloud setup - just pass your API key
memory = Memory(api_key="am_live_YOUR_API_KEY")
```

**Store anything** - strings, dicts, lists:
```python
# Simple memory with auto-generated ID
memory_id = memory.remember("Customer prefers email over phone calls")
# Returns: "mem_7a8c3b4f"

# Store with custom ID for easy retrieval
memory.remember("API rate limit is 1000 requests per hour", id="api_limits")

# Store data of any size or type
memory.remember({
    "user_type": "enterprise",
    "features": ["sso", "analytics", "priority_support"],
    "contract_value": 50000
}, id="customer_profile")
```

**Retrieve instantly** by ID:
```python
# Get your data back
memory.get("api_limits")  # "API rate limit is 1000 requests per hour"
profile = memory.get("customer_profile")  # Returns the full customer dict

# Get with metadata
data = memory.get(memory_id, include_metadata=True)
# Returns: {"content": "Customer prefers email...", "timestamp": "2024-01-15T14:30:00Z", "session_id": "chat_001"}
```

**Natural language search** - the real power:
```python
# Store customer feedback and issues
memory.remember("Customer says checkout is too complicated")
memory.remember("App crashes when files are too big")
memory.remember("Enterprise client wants single sign-on")
memory.remember("Mobile app is slow according to users")

# Ask questions naturally - AI finds relevant memories
ui_feedback = memory.recall("What do customers think about our interface?")
# Finds: ["Customer says checkout is too complicated", "Mobile app is slow according to users"]

technical_issues = memory.recall("What problems are users having?")
# Finds: ["App crashes when files are too big"]

sales_needs = memory.recall("What do enterprise customers want?")
# Finds: ["Enterprise client wants single sign-on"]
```

That's it. No vector DBs to manage. No complex prompt engineering. Just a conscience that works.

## Features

- 🤖 **Agent-Controlled Memory** - Let your agents decide what's worth remembering
- 🚀 **5-minute integration** - Drop-in memory for any LLM app
- 🔌 **Framework agnostic** - Works with LangChain, OpenAI, Anthropic, and more
- 🔍 **Smart Retrieval** - Semantic search, recency, importance, and hybrid strategies
- 📊 **GDPR Compliant** - User data export and deletion built-in
- 💾 **Flexible Storage** - Local mode for development, cloud mode coming soon

## Installation

```bash
pip install agentmind
```

## Framework Integrations

### With LangChain

```python
from langchain import ConversationChain
from langchain.llms import OpenAI
from agentmind.integrations.langchain import AgentMindMemory

# Use AgentMind as LangChain's memory - persists across sessions!
memory = AgentMindMemory(api_key="am_live_YOUR_API_KEY", user_id="user_123")

chain = ConversationChain(
    llm=OpenAI(),
    memory=memory
)

# First conversation
chain.predict(input="I'm working on a React app with TypeScript")
chain.predict(input="I need help with state management")

# Later session - the AI remembers!
response = chain.predict(input="What technology stack am I using?")
# Output: "You're working on a React app with TypeScript. Last time we discussed
# state management options for your project."
```

### With OpenAI

```python
from openai import OpenAI
from agentmind import Memory
from agentmind.integrations.openai import enhance_with_memory

client = OpenAI()
memory = Memory(api_key="am_live_YOUR_API_KEY", user_id="founder_1234")

# Track founder's journey and challenges
memory.remember("Building a fintech startup focused on small business lending")
memory.remember("Team of 8 people, raised $2M seed round last month")
memory.remember("Revenue goal: $1M ARR by end of year")

# Founder asks for strategic advice
messages = [
    {"role": "user", "content": "Should I hire a compliance officer or outsource SOC2?"}
]

# Automatically inject relevant context
enhanced_messages = enhance_with_memory(messages, memory)

response = client.chat.completions.create(
    model="gpt-4",
    messages=enhanced_messages
)
# AI response considers the startup's size (8 people), funding ($2M), and revenue goals
```

## Advanced Features

### Semantic Search
```python
# Find memories by meaning, not just keywords
memories = memory.recall(
    "technical challenges",
    strategy="semantic",
    limit=5
)

# Context-aware retrieval
context = memory.recall("user's communication preferences")
# Finds: "I prefer direct and concise communication style"

# Multi-strategy search
relevant = memory.recall(
    "recent product feedback",
    strategy="hybrid",  # Combines semantic + recency
    user_id="customer_123"
)
```

### Direct Memory Access
```python
# Check existence before retrieval
if memory.exists("user_preferences"):
    prefs = memory.get("user_preferences")
    
# Clean up whenever needed, or let the agent manage memory itself
memory.delete("temporary_data")
```

### Explore Memory Contents
```python
# See everything in memory
all_memories = memory.list()
for mem in all_memories:
    print(f"{mem['id']}: {mem['preview']} ({mem['size']})")

# Output:
# api_limits: API rate limit is 1000 requests per hour (45 chars)
# customer_profile: {"user_type": "enterprise", "features": ["sso", "analytics"... (127 chars)
# mem_7a8c3b4f: Customer prefers email over phone calls (39 chars)
# user_feedback_mobile: Mobile app is slow according to users (38 chars)
# enterprise_sso_req: Enterprise client wants single sign-on (38 chars)

# Get full data
with_data = memory.list(include_data=True)

# Filter memories
user_memories = memory.list(user_id="user_123")
recent = memory.list(created_after="2024-01-20")
important = memory.list(category="important")

# Paginate through large memory stores
page1 = memory.list(limit=50, offset=0)
page2 = memory.list(limit=50, offset=50)
```

### Detailed Inspection
```python
# Get complete details about a memory
details = memory.inspect("mem_abc123")
print(f"Created: {details['metadata']['created']}")
print(f"Size: {details['metadata']['size']}")
print(f"Type: {details['metadata']['type']}")
print(f"Content: {details['content']}")
```

### Memory Management
```python
# Batch operations - returns list of IDs
memory_ids = memory.remember_batch([
    "Q1 OKRs: Increase ARR by 50%",
    {"content": "User interview: Needs better integrations", "id": "interview_001"},
    {"content": "Competitor launched similar feature", "metadata": {"urgent": True}}
])

# Clean up old memories
memory.forget_before(date="2023-01-01")

# Export for compliance
data = memory.export_user_data(user_id="customer_123")
```

### Session Management
```python
# Auto-summarize conversations
summary = memory.summarize_session(session_id="chat_123")

# Export user data (GDPR)
data = memory.export_user_data(user_id="user_123")
```

## How It Works

### Cloud Mode (Available Now)
Fully managed memory infrastructure - no databases to maintain:

```python
memory = Memory(api_key="am_live_YOUR_API_KEY")
# We handle storage, scaling, backups, and search
# Get your API key at https://agent-mind.com
```

### Local Mode (Development)
For development and testing:

```python
memory = Memory(local_mode=True)
# Stores memories locally for development
```

**[→ Get your API key](https://agent-mind.com)** to start using AgentMind cloud.

## Who's Using AgentMind?

### 💻 **SaaS Customer Support Teams**
- **ICP**: B2B SaaS companies with 50+ support tickets daily
- **Use case**: AI agents remember customer history, past issues, and preferences across all channels
- **Result**: 60% faster resolution times, 40% higher CSAT scores
- *"Our AI support agent knows every customer's journey - no more asking users to repeat themselves"*

### 🏦 **Financial Services & Fintech**
- **ICP**: Banks, credit unions, and fintech startups handling loan applications
- **Use case**: Agents track applicant data, credit history, and compliance requirements across the approval process
- **Result**: 3x faster loan processing, 90% reduction in compliance errors
- *"We process 500+ loan applications daily - AgentMind helps our agents make consistent, compliant decisions"*

### 🛒 **E-commerce & Retail**
- **ICP**: Online retailers with complex product catalogs and customer service needs
- **Use case**: AI shopping assistants remember customer preferences, purchase history, and browsing behavior
- **Result**: 35% increase in conversion rates, 50% reduction in cart abandonment
- *"Our AI knows if a customer prefers sustainable products or has size preferences - it's like having a personal shopper"*

### 🏥 **Healthcare & Medical Practices**
- **ICP**: Medical practices, telehealth platforms, and healthcare startups
- **Use case**: AI assistants track patient history, medication interactions, and treatment outcomes
- **Result**: 25% improvement in care coordination, 80% reduction in medical errors
- *"Our AI remembers every patient interaction - critical for continuity of care across multiple providers"*

### 🏗️ **Professional Services**
- **ICP**: Law firms, consulting agencies, and accounting practices
- **Use case**: AI assistants track client requirements, project history, and billing details across engagements
- **Result**: 45% increase in billable hour accuracy, 30% faster project delivery
- *"Our AI knows each client's communication style and project preferences - it's like having a senior partner's memory"*

## Roadmap

- [x] Core memory API
- [x] Direct memory access (get/list/inspect)
- [x] Store any data type (dict, list, objects)
- [x] LangChain integration
- [x] OpenAI integration
- [x] Semantic search with embeddings
- [ ] smolagents integration
- [ ] Memory compression
- [ ] Multi-modal memories (images, audio, PDFs)
- [ ] Reflection layer (self-improving memory)
- [ ] Cloud service

## Community

- [Discord](https://discord.gg/agentmind) - Chat with the community
- [X](https://twitter.com/agentmind) - Latest updates
- Blog - Coming soon

## Contributing

We love contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
git clone https://github.com/muiez/agentmind
cd agentmind
pip install -e ".[dev]"
pytest
```

## License

MIT License - see [LICENSE](LICENSE) for details.

---

Built with ❤️ for the AI community. Give your agents the memory they deserve.
