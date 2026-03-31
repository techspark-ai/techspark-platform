"""
TechSpark AI - Marketing Agent Example Implementation
Basic implementation of a Marketing AI Agent using OpenAI API

This example demonstrates:
- Content generation for social media
- Campaign planning
- Email marketing
- Analytics tracking
"""

import os
import json
from typing import Optional, Dict, Any, List
from datetime import datetime
import openai

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

class MarketingAgent:
    """
    Marketing AI Agent for content creation and campaign management
    """
    
    def __init__(self, agent_name: str = "Marketing Agent"):
        """
        Initialize the Marketing Agent
        
        Args:
            agent_name: Name of the agent
        """
        self.agent_name = agent_name
        self.campaigns = []
        self.content_calendar = []
        self.analytics = {}
        
        # System prompt for the Marketing Agent
        self.system_prompt = """
You are a professional Marketing Agent for TechSpark AI Platform. Your role is to:
1. Create engaging social media content
2. Plan marketing campaigns
3. Generate email marketing content
4. Analyze marketing metrics
5. Provide marketing strategy recommendations
6. Create compelling ad copy

Marketing Guidelines:
- Focus on benefits: Cost reduction, ease of use, time savings
- Target audience: Thai SMEs, business owners, decision makers
- Key messaging: "Every Business Deserves AI Employees"
- Tone: Professional, friendly, inspiring
- Call-to-action: Try free, Schedule demo, Learn more

Platform highlights:
- 5-minute deployment
- No coding required
- 3-5x ROI
- 24/7 support
- Pre-built AI agents

Always create content that resonates with target audience and drives engagement.
"""
    
    def generate_social_content(self,
                               platform: str,
                               topic: str,
                               tone: str = "professional") -> Dict[str, Any]:
        """
        Generate social media content
        
        Args:
            platform: Social platform (facebook, twitter, linkedin, instagram)
            topic: Content topic
            tone: Content tone
            
        Returns:
            Generated content dictionary
        """
        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {
                        "role": "user",
                        "content": f"Generate {tone} {platform} content about: {topic}"
                    }
                ],
                temperature=0.8,
                max_tokens=300
            )
            
            content = response.choices[0].message.content
            
            # Format based on platform
            if platform.lower() == "twitter":
                content = content[:280]  # Twitter character limit
            elif platform.lower() == "facebook":
                content = content[:1000]  # Facebook limit
            
            post = {
                "post_id": f"POST-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "platform": platform,
                "topic": topic,
                "content": content,
                "tone": tone,
                "created_at": datetime.now().isoformat(),
                "status": "draft",
                "engagement_metrics": {
                    "likes": 0,
                    "shares": 0,
                    "comments": 0,
                    "reach": 0
                }
            }
            
            self.content_calendar.append(post)
            return post
            
        except Exception as e:
            return {"error": str(e)}
    
    def generate_email_campaign(self,
                               campaign_name: str,
                               audience: str,
                               subject: str,
                               goal: str) -> Dict[str, Any]:
        """
        Generate email marketing campaign
        
        Args:
            campaign_name: Campaign name
            audience: Target audience
            subject: Email subject
            goal: Campaign goal
            
        Returns:
            Campaign dictionary
        """
        try:
            # Call OpenAI API for email body
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {
                        "role": "user",
                        "content": f"Create professional email body for: {goal}. Audience: {audience}"
                    }
                ],
                temperature=0.7,
                max_tokens=400
            )
            
            email_body = response.choices[0].message.content
            
            campaign = {
                "campaign_id": f"CAMP-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "campaign_name": campaign_name,
                "audience": audience,
                "subject": subject,
                "email_body": email_body,
                "goal": goal,
                "created_at": datetime.now().isoformat(),
                "status": "draft",
                "scheduled_date": None,
                "metrics": {
                    "sent": 0,
                    "opened": 0,
                    "clicked": 0,
                    "converted": 0
                }
            }
            
            self.campaigns.append(campaign)
            return campaign
            
        except Exception as e:
            return {"error": str(e)}
    
    def schedule_post(self, post_id: str, scheduled_date: str) -> bool:
        """
        Schedule a social media post
        
        Args:
            post_id: Post ID
            scheduled_date: Scheduled date (YYYY-MM-DD HH:MM:SS)
            
        Returns:
            Success status
        """
        for post in self.content_calendar:
            if post["post_id"] == post_id:
                post["status"] = "scheduled"
                post["scheduled_date"] = scheduled_date
                return True
        return False
    
    def publish_post(self, post_id: str) -> bool:
        """
        Publish a social media post
        
        Args:
            post_id: Post ID
            
        Returns:
            Success status
        """
        for post in self.content_calendar:
            if post["post_id"] == post_id:
                post["status"] = "published"
                post["published_at"] = datetime.now().isoformat()
                return True
        return False
    
    def update_engagement_metrics(self,
                                 post_id: str,
                                 likes: int = 0,
                                 shares: int = 0,
                                 comments: int = 0,
                                 reach: int = 0) -> bool:
        """
        Update post engagement metrics
        
        Args:
            post_id: Post ID
            likes: Number of likes
            shares: Number of shares
            comments: Number of comments
            reach: Post reach
            
        Returns:
            Success status
        """
        for post in self.content_calendar:
            if post["post_id"] == post_id:
                post["engagement_metrics"]["likes"] = likes
                post["engagement_metrics"]["shares"] = shares
                post["engagement_metrics"]["comments"] = comments
                post["engagement_metrics"]["reach"] = reach
                return True
        return False
    
    def get_campaign_performance(self, campaign_id: str) -> Optional[Dict[str, Any]]:
        """
        Get campaign performance metrics
        
        Args:
            campaign_id: Campaign ID
            
        Returns:
            Campaign metrics or None
        """
        for campaign in self.campaigns:
            if campaign["campaign_id"] == campaign_id:
                metrics = campaign["metrics"]
                if metrics["sent"] > 0:
                    open_rate = (metrics["opened"] / metrics["sent"]) * 100
                    click_rate = (metrics["clicked"] / metrics["sent"]) * 100
                    conversion_rate = (metrics["converted"] / metrics["sent"]) * 100
                else:
                    open_rate = click_rate = conversion_rate = 0
                
                return {
                    "campaign_id": campaign_id,
                    "campaign_name": campaign["campaign_name"],
                    "metrics": metrics,
                    "open_rate": round(open_rate, 2),
                    "click_rate": round(click_rate, 2),
                    "conversion_rate": round(conversion_rate, 2)
                }
        return None
    
    def get_content_calendar(self) -> List[Dict[str, Any]]:
        """Get content calendar"""
        return sorted(self.content_calendar, key=lambda x: x["created_at"])
    
    def get_campaigns(self) -> List[Dict[str, Any]]:
        """Get all campaigns"""
        return sorted(self.campaigns, key=lambda x: x["created_at"])


def main():
    """
    Main function demonstrating Marketing Agent usage
    """
    print("=" * 60)
    print("TechSpark AI - Marketing Agent Example")
    print("=" * 60)
    
    # Initialize Marketing Agent
    agent = MarketingAgent()
    
    # Generate social media content
    print("\n📱 Generating Social Media Content\n")
    
    facebook_post = agent.generate_social_content(
        platform="facebook",
        topic="AI agents for e-commerce businesses",
        tone="professional"
    )
    
    print(f"Platform: {facebook_post['platform']}")
    print(f"Topic: {facebook_post['topic']}")
    print(f"Content:\n{facebook_post['content']}\n")
    
    # Generate email campaign
    print("=" * 60)
    print("📧 Generating Email Campaign\n")
    
    email_campaign = agent.generate_email_campaign(
        campaign_name="Q2 2026 Launch Campaign",
        audience="Thai SME business owners",
        subject="Introducing TechSpark AI - Your AI Workforce Solution",
        goal="Drive sign-ups for free trial"
    )
    
    print(f"Campaign: {email_campaign['campaign_name']}")
    print(f"Subject: {email_campaign['subject']}")
    print(f"Goal: {email_campaign['goal']}")
    print(f"Email Body:\n{email_campaign['email_body']}\n")
    
    # Schedule post
    print("=" * 60)
    print("📅 Scheduling Post\n")
    
    scheduled_date = "2026-04-05 10:00:00"
    if agent.schedule_post(facebook_post['post_id'], scheduled_date):
        print(f"✅ Post scheduled for {scheduled_date}\n")
    
    # Publish post
    print("=" * 60)
    print("🚀 Publishing Post\n")
    
    if agent.publish_post(facebook_post['post_id']):
        print(f"✅ Post published successfully\n")
    
    # Update engagement metrics
    print("=" * 60)
    print("📊 Updating Engagement Metrics\n")
    
    agent.update_engagement_metrics(
        post_id=facebook_post['post_id'],
        likes=245,
        shares=38,
        comments=52,
        reach=3500
    )
    
    print(f"Likes: 245")
    print(f"Shares: 38")
    print(f"Comments: 52")
    print(f"Reach: 3,500\n")
    
    # Get content calendar
    print("=" * 60)
    print("📋 Content Calendar\n")
    
    calendar = agent.get_content_calendar()
    for post in calendar:
        print(f"- {post['post_id']}: {post['topic']} ({post['status']})")
    
    print("\n" + "=" * 60)
    print("✅ Marketing Agent Example Completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
