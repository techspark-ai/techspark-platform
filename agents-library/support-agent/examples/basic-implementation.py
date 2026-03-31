"""
TechSpark AI - Support Agent Example Implementation
Basic implementation of a Support AI Agent using OpenAI API

This example demonstrates:
- Initializing the Support Agent
- Handling customer support tickets
- FAQ management
- Ticket escalation
"""

import os
import json
from typing import Optional, Dict, Any, List
from datetime import datetime
import openai

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

class SupportAgent:
    """
    Support AI Agent for handling customer support tickets and FAQs
    """
    
    def __init__(self, agent_name: str = "Support Agent"):
        """
        Initialize the Support Agent
        
        Args:
            agent_name: Name of the agent
        """
        self.agent_name = agent_name
        self.conversation_history = []
        self.tickets = []
        self.faqs = self._load_faqs()
        
        # System prompt for the Support Agent
        self.system_prompt = """
You are a professional Support Agent for TechSpark AI Platform. Your role is to:
1. Answer customer questions about TechSpark AI services
2. Troubleshoot issues with AI agents
3. Provide guidance on platform usage
4. Create and manage support tickets
5. Escalate complex issues to human agents
6. Provide 24/7 support

Common FAQs:
- How to deploy an AI agent: Click "Deploy" → Select agent → Configure → Done (5 minutes)
- Pricing: Free tier, Pro ($99/month), Enterprise (custom)
- Supported integrations: Slack, Teams, WhatsApp, Email, API
- Implementation: Instant, no coding required
- Support: Email, Chat, Phone for Pro/Enterprise

Always be helpful, empathetic, and professional.
"""
    
    def _load_faqs(self) -> Dict[str, str]:
        """Load frequently asked questions"""
        return {
            "deployment": "To deploy an AI agent: 1. Go to Marketplace 2. Select agent 3. Click Deploy 4. Configure settings 5. Done! Takes ~5 minutes.",
            "pricing": "We offer: Free tier (basic), Pro ($99/month), Enterprise (custom). All include 24/7 support.",
            "integration": "We support Slack, Teams, WhatsApp, Email, and REST API integrations.",
            "training": "Our agents are pre-trained. No training required. Just deploy and start using!",
            "security": "We use enterprise-grade security: SSL encryption, data privacy compliance, regular security audits.",
            "support": "24/7 support available via email, chat, and phone for Pro/Enterprise customers.",
            "customization": "You can customize agent behavior, responses, and integrations through our dashboard.",
            "performance": "Our agents handle 10,000+ requests/minute with 99.9% uptime SLA."
        }
    
    def chat(self, user_message: str) -> str:
        """
        Send a message to the Support Agent and get a response
        
        Args:
            user_message: Customer message
            
        Returns:
            Agent response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    *self.conversation_history
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            # Extract response
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def search_faq(self, keyword: str) -> Optional[str]:
        """
        Search FAQ by keyword
        
        Args:
            keyword: Search keyword
            
        Returns:
            FAQ answer or None
        """
        keyword = keyword.lower()
        for key, answer in self.faqs.items():
            if keyword in key.lower():
                return answer
        return None
    
    def create_ticket(self,
                     customer_name: str,
                     email: str,
                     subject: str,
                     description: str,
                     priority: str = "medium") -> Dict[str, Any]:
        """
        Create a support ticket
        
        Args:
            customer_name: Customer name
            email: Customer email
            subject: Ticket subject
            description: Detailed description
            priority: Priority level (low, medium, high, critical)
            
        Returns:
            Ticket dictionary
        """
        ticket = {
            "ticket_id": f"TK-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "customer_name": customer_name,
            "email": email,
            "subject": subject,
            "description": description,
            "priority": priority,
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "assigned_to": None,
            "resolution": None
        }
        
        self.tickets.append(ticket)
        return ticket
    
    def escalate_ticket(self, ticket_id: str, reason: str) -> bool:
        """
        Escalate a ticket to human agent
        
        Args:
            ticket_id: Ticket ID
            reason: Escalation reason
            
        Returns:
            Success status
        """
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id:
                ticket["status"] = "escalated"
                ticket["escalation_reason"] = reason
                ticket["updated_at"] = datetime.now().isoformat()
                return True
        return False
    
    def resolve_ticket(self, ticket_id: str, resolution: str) -> bool:
        """
        Mark ticket as resolved
        
        Args:
            ticket_id: Ticket ID
            resolution: Resolution description
            
        Returns:
            Success status
        """
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id:
                ticket["status"] = "resolved"
                ticket["resolution"] = resolution
                ticket["updated_at"] = datetime.now().isoformat()
                return True
        return False
    
    def get_ticket_status(self, ticket_id: str) -> Optional[Dict[str, Any]]:
        """
        Get ticket status
        
        Args:
            ticket_id: Ticket ID
            
        Returns:
            Ticket information or None
        """
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id:
                return ticket
        return None
    
    def get_open_tickets(self) -> List[Dict[str, Any]]:
        """Get all open tickets"""
        return [t for t in self.tickets if t["status"] == "open"]
    
    def get_conversation_summary(self) -> str:
        """Get conversation summary"""
        if not self.conversation_history:
            return "No conversation history"
        
        summary = f"Support Conversation Summary ({len(self.conversation_history)} messages)\n"
        summary += f"Agent: {self.agent_name}\n"
        summary += "-" * 50 + "\n"
        
        for msg in self.conversation_history:
            role = "Customer" if msg["role"] == "user" else "Agent"
            content = msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"]
            summary += f"{role}: {content}\n"
        
        return summary


def main():
    """
    Main function demonstrating Support Agent usage
    """
    print("=" * 60)
    print("TechSpark AI - Support Agent Example")
    print("=" * 60)
    
    # Initialize Support Agent
    agent = SupportAgent()
    
    # Example conversation
    print("\n💬 Starting Support Agent Conversation\n")
    
    # Customer inquiry 1
    customer_message_1 = "Hi, I need help deploying a Sales AI agent. How long does it take?"
    print(f"Customer: {customer_message_1}")
    response_1 = agent.chat(customer_message_1)
    print(f"Agent: {response_1}\n")
    
    # Customer inquiry 2
    customer_message_2 = "What integrations do you support?"
    print(f"Customer: {customer_message_2}")
    response_2 = agent.chat(customer_message_2)
    print(f"Agent: {response_2}\n")
    
    # Search FAQ
    print("=" * 60)
    print("🔍 Searching FAQ\n")
    
    faq_result = agent.search_faq("pricing")
    print(f"FAQ Result: {faq_result}\n")
    
    # Create ticket
    print("=" * 60)
    print("🎫 Creating Support Ticket\n")
    
    ticket = agent.create_ticket(
        customer_name="Jane Doe",
        email="jane@company.com",
        subject="Issue with Sales AI integration",
        description="The Sales AI agent is not responding to customer messages in Slack",
        priority="high"
    )
    
    print(f"Ticket ID: {ticket['ticket_id']}")
    print(f"Customer: {ticket['customer_name']}")
    print(f"Subject: {ticket['subject']}")
    print(f"Priority: {ticket['priority']}")
    print(f"Status: {ticket['status']}\n")
    
    # Escalate ticket
    print("=" * 60)
    print("⬆️ Escalating Ticket\n")
    
    if agent.escalate_ticket(ticket['ticket_id'], "Requires technical investigation"):
        print(f"✅ Ticket {ticket['ticket_id']} escalated to human agent\n")
    
    # Get open tickets
    print("=" * 60)
    print("📋 Open Tickets\n")
    
    open_tickets = agent.get_open_tickets()
    for t in open_tickets:
        print(f"- {t['ticket_id']}: {t['subject']} (Priority: {t['priority']})")
    
    print("\n" + "=" * 60)
    print("📊 Conversation Summary\n")
    print(agent.get_conversation_summary())
    
    print("\n" + "=" * 60)
    print("✅ Support Agent Example Completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
