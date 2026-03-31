# TechSpark AI - Agent Integration Guide

Complete guide for integrating and using TechSpark AI Agents in your applications.

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [Agent Types](#agent-types)
3. [Installation](#installation)
4. [Basic Usage](#basic-usage)
5. [Advanced Integration](#advanced-integration)
6. [API Reference](#api-reference)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- pip or conda

### Quick Setup

```bash
# Install dependencies
pip install openai python-dotenv

# Set environment variables
export OPENAI_API_KEY="your-api-key-here"
```

---

## Agent Types

### 1. Sales Agent
**Purpose**: Handle customer inquiries, generate quotes, manage leads

**Key Features**:
- Customer inquiry handling
- Quote generation
- Lead management
- Sales pipeline tracking

**Use Cases**:
- E-commerce businesses
- B2B sales
- Customer acquisition

**Example**:
```python
from agents_library.sales_agent import SalesAgent

agent = SalesAgent()
response = agent.chat("I need a quote for 2 agents")
quote = agent.generate_quote(
    customer_name="John Doe",
    company_name="Tech Corp",
    agents_needed=["Sales AI", "Support AI"],
    monthly_volume=5000
)
```

### 2. Support Agent
**Purpose**: Provide 24/7 customer support, manage tickets

**Key Features**:
- FAQ management
- Ticket creation and tracking
- Issue escalation
- Knowledge base integration

**Use Cases**:
- Customer support
- Technical help
- Complaint handling

**Example**:
```python
from agents_library.support_agent import SupportAgent

agent = SupportAgent()
response = agent.chat("How do I deploy an agent?")
ticket = agent.create_ticket(
    customer_name="Jane Doe",
    email="jane@company.com",
    subject="Integration issue",
    description="Agent not responding",
    priority="high"
)
```

### 3. Marketing Agent
**Purpose**: Create marketing content, manage campaigns

**Key Features**:
- Social media content generation
- Email campaign creation
- Content calendar management
- Analytics tracking

**Use Cases**:
- Social media marketing
- Email marketing
- Content creation

**Example**:
```python
from agents_library.marketing_agent import MarketingAgent

agent = MarketingAgent()
post = agent.generate_social_content(
    platform="facebook",
    topic="AI for business",
    tone="professional"
)
campaign = agent.generate_email_campaign(
    campaign_name="Q2 Campaign",
    audience="SME owners",
    subject="Introducing TechSpark AI",
    goal="Drive sign-ups"
)
```

### 4. HR Agent
**Purpose**: Manage HR operations, employee records

**Key Features**:
- Leave management
- Policy information
- Employee onboarding
- Performance tracking

**Use Cases**:
- HR operations
- Employee management
- Payroll support

### 5. Finance Agent
**Purpose**: Financial analysis, expense tracking

**Key Features**:
- Invoice analysis
- Expense categorization
- Financial reporting
- Budget tracking

**Use Cases**:
- Accounting
- Financial analysis
- Expense management

---

## Installation

### Option 1: From PyPI (Coming Soon)

```bash
pip install techspark-ai-agents
```

### Option 2: From Source

```bash
git clone https://github.com/techspark-ai/techspark-platform.git
cd techspark-platform/agents-library
pip install -e .
```

### Option 3: Docker

```bash
docker build -t techspark-agents .
docker run -e OPENAI_API_KEY="your-key" techspark-agents
```

---

## Basic Usage

### 1. Initialize an Agent

```python
from agents_library.sales_agent import SalesAgent

# Create agent instance
agent = SalesAgent(agent_name="My Sales Agent")
```

### 2. Send Messages

```python
# Send a message and get response
response = agent.chat("Tell me about your pricing")
print(response)
```

### 3. Handle Responses

```python
# Responses are strings
if "error" in response.lower():
    print("Error occurred:", response)
else:
    print("Success:", response)
```

---

## Advanced Integration

### Integration with Web Application

```python
from flask import Flask, request, jsonify
from agents_library.sales_agent import SalesAgent

app = Flask(__name__)
agent = SalesAgent()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    response = agent.chat(message)
    return jsonify({'response': response})

@app.route('/api/quote', methods=['POST'])
def generate_quote():
    data = request.json
    quote = agent.generate_quote(
        customer_name=data['customer_name'],
        company_name=data['company_name'],
        agents_needed=data['agents'],
        monthly_volume=data['volume']
    )
    return jsonify(quote)

if __name__ == '__main__':
    app.run(debug=True)
```

### Integration with Slack

```python
from slack_bolt import App
from agents_library.support_agent import SupportAgent

app = App(token="xoxb-your-token")
support_agent = SupportAgent()

@app.message(".*")
def handle_message(message, say):
    user_message = message['text']
    response = support_agent.chat(user_message)
    say(response)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
```

### Integration with WhatsApp

```python
from twilio.rest import Client
from agents_library.support_agent import SupportAgent

account_sid = "your-account-sid"
auth_token = "your-auth-token"
client = Client(account_sid, auth_token)
agent = SupportAgent()

def send_whatsapp_message(from_number, to_number, message):
    response = agent.chat(message)
    client.messages.create(
        from_=f"whatsapp:{from_number}",
        body=response,
        to=f"whatsapp:{to_number}"
    )
```

---

## API Reference

### SalesAgent

#### Methods

**`chat(user_message: str) -> str`**
- Send a message and get response
- Returns: Agent response string

**`generate_quote(customer_name, company_name, agents_needed, monthly_volume) -> Dict`**
- Generate a professional quote
- Returns: Quote dictionary with pricing

**`save_customer_data(customer_info: Dict) -> bool`**
- Save customer information
- Returns: Success status

**`get_conversation_summary() -> str`**
- Get conversation summary
- Returns: Summary string

### SupportAgent

#### Methods

**`chat(user_message: str) -> str`**
- Send a message and get response
- Returns: Agent response string

**`search_faq(keyword: str) -> Optional[str]`**
- Search FAQ by keyword
- Returns: FAQ answer or None

**`create_ticket(customer_name, email, subject, description, priority) -> Dict`**
- Create a support ticket
- Returns: Ticket dictionary

**`escalate_ticket(ticket_id: str, reason: str) -> bool`**
- Escalate ticket to human agent
- Returns: Success status

**`resolve_ticket(ticket_id: str, resolution: str) -> bool`**
- Mark ticket as resolved
- Returns: Success status

### MarketingAgent

#### Methods

**`generate_social_content(platform, topic, tone) -> Dict`**
- Generate social media content
- Returns: Content dictionary

**`generate_email_campaign(campaign_name, audience, subject, goal) -> Dict`**
- Generate email campaign
- Returns: Campaign dictionary

**`schedule_post(post_id: str, scheduled_date: str) -> bool`**
- Schedule a post
- Returns: Success status

**`publish_post(post_id: str) -> bool`**
- Publish a post
- Returns: Success status

---

## Best Practices

### 1. Error Handling

```python
try:
    response = agent.chat(message)
except Exception as e:
    print(f"Error: {str(e)}")
    # Handle error gracefully
```

### 2. Rate Limiting

```python
import time
from functools import wraps

def rate_limit(calls_per_minute=60):
    min_interval = 60.0 / calls_per_minute
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = min_interval - elapsed
            if wait_time > 0:
                time.sleep(wait_time)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit(calls_per_minute=60)
def chat_with_agent(message):
    return agent.chat(message)
```

### 3. Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def chat_with_logging(message):
    logger.info(f"User message: {message}")
    response = agent.chat(message)
    logger.info(f"Agent response: {response}")
    return response
```

### 4. Caching

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_faq_cached(keyword):
    return support_agent.search_faq(keyword)
```

---

## Troubleshooting

### Issue: "API key not found"

**Solution**:
```bash
export OPENAI_API_KEY="your-api-key-here"
# Or in Python:
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'
```

### Issue: "Rate limit exceeded"

**Solution**:
- Implement exponential backoff
- Use rate limiting decorator
- Upgrade OpenAI plan

### Issue: "Agent not responding"

**Solution**:
- Check API key validity
- Verify internet connection
- Check OpenAI API status
- Review error logs

### Issue: "Timeout error"

**Solution**:
- Increase timeout value
- Check message length
- Reduce complexity of request

---

## Examples

### Complete Sales Agent Example

```python
from agents_library.sales_agent import SalesAgent

# Initialize agent
agent = SalesAgent()

# Conversation
print(agent.chat("What's the best AI agent for e-commerce?"))
print(agent.chat("How much does it cost?"))
print(agent.chat("Can you generate a quote?"))

# Generate quote
quote = agent.generate_quote(
    customer_name="John Smith",
    company_name="TechStore Thailand",
    agents_needed=["Sales AI", "Support AI"],
    monthly_volume=5000
)

print(f"Quote ID: {quote['quote_id']}")
print(f"Monthly Cost: ${quote['monthly_cost']}")
print(f"Annual Cost: ${quote['annual_cost']}")
print(f"Estimated Savings: ${quote['estimated_annual_savings']}")
```

### Complete Support Agent Example

```python
from agents_library.support_agent import SupportAgent

# Initialize agent
agent = SupportAgent()

# FAQ search
faq = agent.search_faq("deployment")
print(faq)

# Create ticket
ticket = agent.create_ticket(
    customer_name="Jane Doe",
    email="jane@company.com",
    subject="Integration issue",
    description="Agent not responding",
    priority="high"
)

print(f"Ticket ID: {ticket['ticket_id']}")
print(f"Status: {ticket['status']}")

# Escalate if needed
agent.escalate_ticket(ticket['ticket_id'], "Requires technical investigation")
```

---

## Support

- **Documentation**: https://github.com/techspark-ai/techspark-platform/docs
- **Issues**: https://github.com/techspark-ai/techspark-platform/issues
- **Email**: support@techspark.ai
- **Discord**: https://discord.gg/techspark

---

## License

MIT License - See [LICENSE](../LICENSE)

---

**Last Updated**: March 31, 2026
