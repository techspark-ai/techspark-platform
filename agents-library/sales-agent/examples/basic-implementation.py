"""
TechSpark AI - Sales Agent Example Implementation
Basic implementation of a Sales AI Agent using OpenAI API

This example demonstrates:
- Initializing the Sales Agent
- Handling customer inquiries
- Generating quotes
- Managing conversation state
"""

import os
import json
from typing import Optional, Dict, Any
from datetime import datetime
import openai

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

class SalesAgent:
    """
    Sales AI Agent for handling customer inquiries and generating quotes
    """
    
    def __init__(self, agent_name: str = "Sales Agent"):
        """
        Initialize the Sales Agent
        
        Args:
            agent_name: Name of the agent
        """
        self.agent_name = agent_name
        self.conversation_history = []
        self.customer_data = {}
        self.quotes = []
        
        # System prompt for the Sales Agent
        self.system_prompt = """
You are a professional Sales Agent for TechSpark AI Platform. Your role is to:
1. Answer customer questions about our AI agents and services
2. Understand customer needs and pain points
3. Recommend appropriate AI solutions
4. Generate professional quotes based on customer requirements
5. Handle objections professionally
6. Schedule demos and follow-ups

Key information about TechSpark AI:
- We provide AI Agent Marketplace with pre-built solutions
- Services: Sales AI, Support AI, Marketing AI, HR AI, Finance AI
- Pricing: Free tier, Pro ($99/month), Enterprise (custom)
- Implementation time: 5 minutes to deploy
- ROI: 3-5x cost reduction within 6 months

Always be helpful, professional, and focus on customer success.
"""
    
    def chat(self, user_message: str) -> str:
        """
        Send a message to the Sales Agent and get a response
        
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
    
    def generate_quote(self, 
                      customer_name: str,
                      company_name: str,
                      agents_needed: list,
                      monthly_volume: int) -> Dict[str, Any]:
        """
        Generate a professional quote for the customer
        
        Args:
            customer_name: Customer name
            company_name: Company name
            agents_needed: List of agents (e.g., ['Sales AI', 'Support AI'])
            monthly_volume: Expected monthly usage volume
            
        Returns:
            Quote dictionary
        """
        # Pricing calculation
        base_price = 99  # Pro plan base price
        agent_multiplier = len(agents_needed) * 0.5
        volume_discount = max(0, (monthly_volume - 1000) / 10000 * 0.1)
        
        monthly_cost = base_price * (1 + agent_multiplier) * (1 - volume_discount)
        annual_cost = monthly_cost * 12
        
        # Estimated savings (3-5x ROI)
        estimated_savings = monthly_cost * 4 * 12  # 4x ROI annually
        
        quote = {
            "quote_id": f"QT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "customer_name": customer_name,
            "company_name": company_name,
            "agents": agents_needed,
            "monthly_cost": round(monthly_cost, 2),
            "annual_cost": round(annual_cost, 2),
            "estimated_annual_savings": round(estimated_savings, 2),
            "roi_multiplier": "4x",
            "implementation_time": "5 minutes",
            "created_at": datetime.now().isoformat(),
            "valid_until": datetime.now().strftime('%Y-%m-%d')
        }
        
        self.quotes.append(quote)
        return quote
    
    def save_customer_data(self, customer_info: Dict[str, Any]) -> bool:
        """
        Save customer information for follow-up
        
        Args:
            customer_info: Customer information dictionary
            
        Returns:
            Success status
        """
        try:
            self.customer_data = customer_info
            return True
        except Exception as e:
            print(f"Error saving customer data: {str(e)}")
            return False
    
    def get_conversation_summary(self) -> str:
        """
        Get a summary of the conversation
        
        Returns:
            Conversation summary
        """
        if not self.conversation_history:
            return "No conversation history"
        
        summary = f"Conversation Summary ({len(self.conversation_history)} messages)\n"
        summary += f"Agent: {self.agent_name}\n"
        summary += "-" * 50 + "\n"
        
        for msg in self.conversation_history:
            role = "Customer" if msg["role"] == "user" else "Agent"
            content = msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"]
            summary += f"{role}: {content}\n"
        
        return summary
    
    def export_quote_as_json(self, quote_id: str) -> Optional[str]:
        """
        Export quote as JSON
        
        Args:
            quote_id: Quote ID
            
        Returns:
            JSON string or None
        """
        for quote in self.quotes:
            if quote["quote_id"] == quote_id:
                return json.dumps(quote, indent=2)
        return None


def main():
    """
    Main function demonstrating Sales Agent usage
    """
    print("=" * 60)
    print("TechSpark AI - Sales Agent Example")
    print("=" * 60)
    
    # Initialize Sales Agent
    agent = SalesAgent()
    
    # Example conversation
    print("\n📞 Starting Sales Agent Conversation\n")
    
    # Customer inquiry 1
    customer_message_1 = "Hi, I'm interested in AI solutions for my e-commerce business. We need help with customer support."
    print(f"Customer: {customer_message_1}")
    response_1 = agent.chat(customer_message_1)
    print(f"Agent: {response_1}\n")
    
    # Customer inquiry 2
    customer_message_2 = "What's the cost and how quickly can we implement it?"
    print(f"Customer: {customer_message_2}")
    response_2 = agent.chat(customer_message_2)
    print(f"Agent: {response_2}\n")
    
    # Generate quote
    print("=" * 60)
    print("📋 Generating Quote\n")
    
    quote = agent.generate_quote(
        customer_name="John Smith",
        company_name="TechStore Thailand",
        agents_needed=["Support AI", "Sales AI"],
        monthly_volume=5000
    )
    
    print(f"Quote ID: {quote['quote_id']}")
    print(f"Customer: {quote['customer_name']} ({quote['company_name']})")
    print(f"Agents: {', '.join(quote['agents'])}")
    print(f"Monthly Cost: ${quote['monthly_cost']}")
    print(f"Annual Cost: ${quote['annual_cost']}")
    print(f"Estimated Annual Savings: ${quote['estimated_annual_savings']}")
    print(f"ROI: {quote['roi_multiplier']}")
    print(f"Implementation Time: {quote['implementation_time']}\n")
    
    # Save customer data
    print("=" * 60)
    print("💾 Saving Customer Data\n")
    
    customer_info = {
        "name": "John Smith",
        "company": "TechStore Thailand",
        "email": "john@techstore.co.th",
        "phone": "+66-2-xxx-xxxx",
        "industry": "E-commerce",
        "company_size": "50-100 employees",
        "budget": "$2000-5000/month",
        "timeline": "Immediate"
    }
    
    if agent.save_customer_data(customer_info):
        print("✅ Customer data saved successfully\n")
    
    # Display conversation summary
    print("=" * 60)
    print("📊 Conversation Summary\n")
    print(agent.get_conversation_summary())
    
    # Export quote
    print("\n" + "=" * 60)
    print("📤 Exporting Quote as JSON\n")
    quote_json = agent.export_quote_as_json(quote['quote_id'])
    print(quote_json)
    
    print("\n" + "=" * 60)
    print("✅ Sales Agent Example Completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
