# TechSpark AI - Agent Examples

Complete working examples for all TechSpark AI Agents.

## 📋 Overview

This directory contains production-ready examples demonstrating how to use each AI Agent in your applications.

## 🗂️ Examples Included

### 1. Sales Agent
**File**: `../sales-agent/examples/basic-implementation.py`

**Features**:
- Customer inquiry handling
- Quote generation
- Customer data management
- Conversation tracking

**Run**:
```bash
python ../sales-agent/examples/basic-implementation.py
```

**Output**:
```
Customer: Hi, I'm interested in AI solutions...
Agent: [Response about TechSpark AI]

Quote ID: QT-20260331103045
Monthly Cost: $149.50
Annual Cost: $1,794.00
Estimated Annual Savings: $7,176.00
ROI: 4x
```

### 2. Support Agent
**File**: `../support-agent/examples/basic-implementation.py`

**Features**:
- FAQ search
- Ticket creation
- Ticket escalation
- Support tracking

**Run**:
```bash
python ../support-agent/examples/basic-implementation.py
```

**Output**:
```
Customer: How do I deploy an AI agent?
Agent: [Helpful response with steps]

Ticket ID: TK-20260331103045
Status: open
Priority: high
```

### 3. Marketing Agent
**File**: `../marketing-agent/examples/basic-implementation.py`

**Features**:
- Social media content generation
- Email campaign creation
- Content scheduling
- Analytics tracking

**Run**:
```bash
python ../marketing-agent/examples/basic-implementation.py
```

**Output**:
```
Platform: facebook
Content: [Generated marketing content]

Campaign: Q2 2026 Launch Campaign
Subject: Introducing TechSpark AI
Status: draft
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Install dependencies
pip install openai python-dotenv

# Set API key
export OPENAI_API_KEY="your-api-key-here"
```

### 2. Run Examples

```bash
# Sales Agent
python ../sales-agent/examples/basic-implementation.py

# Support Agent
python ../support-agent/examples/basic-implementation.py

# Marketing Agent
python ../marketing-agent/examples/basic-implementation.py
```

## 💡 Integration Patterns

### Web Application Integration

```python
from flask import Flask, request, jsonify
from agents_library.sales_agent import SalesAgent

app = Flask(__name__)
agent = SalesAgent()

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = agent.chat(message)
    return jsonify({'response': response})

@app.route('/api/quote', methods=['POST'])
def quote():
    data = request.json
    quote = agent.generate_quote(**data)
    return jsonify(quote)
```

### Slack Integration

```python
from slack_bolt import App
from agents_library.support_agent import SupportAgent

app = App(token="xoxb-your-token")
agent = SupportAgent()

@app.message(".*")
def handle_message(message, say):
    response = agent.chat(message['text'])
    say(response)
```

### WhatsApp Integration

```python
from twilio.rest import Client
from agents_library.support_agent import SupportAgent

client = Client(account_sid, auth_token)
agent = SupportAgent()

def handle_whatsapp(message):
    response = agent.chat(message)
    client.messages.create(
        from_="whatsapp:+1234567890",
        body=response,
        to="whatsapp:+1234567890"
    )
```

## 📊 Example Output

### Sales Agent Quote

```json
{
  "quote_id": "QT-20260331103045",
  "customer_name": "John Smith",
  "company_name": "TechStore Thailand",
  "agents": ["Support AI", "Sales AI"],
  "monthly_cost": 149.50,
  "annual_cost": 1794.00,
  "estimated_annual_savings": 7176.00,
  "roi_multiplier": "4x",
  "implementation_time": "5 minutes",
  "created_at": "2026-03-31T10:30:45.123456",
  "valid_until": "2026-03-31"
}
```

### Support Agent Ticket

```json
{
  "ticket_id": "TK-20260331103045",
  "customer_name": "Jane Doe",
  "email": "jane@company.com",
  "subject": "Integration issue",
  "description": "Agent not responding to customer messages",
  "priority": "high",
  "status": "open",
  "created_at": "2026-03-31T10:30:45.123456",
  "updated_at": "2026-03-31T10:30:45.123456"
}
```

### Marketing Agent Post

```json
{
  "post_id": "POST-20260331103045",
  "platform": "facebook",
  "topic": "AI agents for e-commerce",
  "content": "Every business deserves AI employees...",
  "tone": "professional",
  "status": "published",
  "engagement_metrics": {
    "likes": 245,
    "shares": 38,
    "comments": 52,
    "reach": 3500
  }
}
```

## 🎯 Common Use Cases

### Use Case 1: E-commerce Store

```python
# Initialize agents
sales_agent = SalesAgent()
support_agent = SupportAgent()
marketing_agent = MarketingAgent()

# Handle customer inquiry
response = sales_agent.chat("I need help with product recommendations")

# Generate quote if interested
quote = sales_agent.generate_quote(
    customer_name="Customer Name",
    company_name="Store Name",
    agents_needed=["Sales AI", "Support AI"],
    monthly_volume=10000
)

# Create support ticket if issue
ticket = support_agent.create_ticket(
    customer_name="Customer Name",
    email="customer@email.com",
    subject="Issue with order",
    description="Product not received",
    priority="high"
)

# Generate marketing content
post = marketing_agent.generate_social_content(
    platform="facebook",
    topic="New product launch",
    tone="exciting"
)
```

### Use Case 2: Service Business

```python
# Initialize agents
sales_agent = SalesAgent()
support_agent = SupportAgent()

# Handle lead inquiry
response = sales_agent.chat("What services do you offer?")

# Generate proposal
quote = sales_agent.generate_quote(
    customer_name="Business Owner",
    company_name="Service Company",
    agents_needed=["Sales AI"],
    monthly_volume=500
)

# Handle support requests
faq = support_agent.search_faq("pricing")
ticket = support_agent.create_ticket(
    customer_name="Client Name",
    email="client@email.com",
    subject="Service question",
    description="Need clarification",
    priority="medium"
)
```

### Use Case 3: Marketing Agency

```python
# Initialize marketing agent
marketing_agent = MarketingAgent()

# Generate social content
facebook_post = marketing_agent.generate_social_content(
    platform="facebook",
    topic="Client product launch",
    tone="professional"
)

# Generate email campaign
campaign = marketing_agent.generate_email_campaign(
    campaign_name="Q2 Campaign",
    audience="Target audience",
    subject="Campaign subject",
    goal="Drive conversions"
)

# Schedule posts
marketing_agent.schedule_post(
    facebook_post['post_id'],
    "2026-04-05 10:00:00"
)

# Track metrics
marketing_agent.update_engagement_metrics(
    post_id=facebook_post['post_id'],
    likes=245,
    shares=38,
    comments=52,
    reach=3500
)
```

## 🔧 Configuration

### Environment Variables

```bash
# Required
OPENAI_API_KEY=your-api-key

# Optional
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
OPENAI_MAX_TOKENS=500
```

### Agent Configuration

```python
# Custom agent configuration
agent = SalesAgent(agent_name="My Custom Sales Agent")

# Or with config file
import json
with open('config.json') as f:
    config = json.load(f)
agent = SalesAgent(**config)
```

## 📚 Documentation

- [Integration Guide](../INTEGRATION_GUIDE.md)
- [Sales Agent README](../sales-agent/README.md)
- [Support Agent README](../support-agent/README.md)
- [Marketing Agent README](../marketing-agent/README.md)

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](../../CONTRIBUTING.md)

## 📄 License

MIT License - See [LICENSE](../../LICENSE)

## 🔗 Links

- **Repository**: https://github.com/techspark-ai/techspark-platform
- **Documentation**: https://techspark-ai.github.io/techspark-platform
- **Support**: support@techspark.ai

---

**Last Updated**: March 31, 2026
