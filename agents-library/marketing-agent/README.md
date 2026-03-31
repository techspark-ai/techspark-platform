# Marketing Agent 📱

ตัวแทนการตลาดที่สร้างเนื้อหา โพสต์ Facebook, Email Campaign และ Social Media Content

---

## 🎯 ลักษณะเด่น

- ✅ สร้างโพสต์ Facebook
- ✅ สร้าง Email Campaign
- ✅ สร้าง Instagram Caption
- ✅ สร้าง LinkedIn Article
- ✅ วิเคราะห์ Trending Topics

---

## 📋 Use Cases

### 1. สร้างโพสต์ Facebook
```
User: "สร้างโพสต์เกี่ยวกับสินค้าใหม่"
Agent: "📱 โพสต์ Facebook:

🎉 ประกาศสินค้าใหม่!

ยินดีต้อนรับ Product X - ผลิตภัณฑ์ที่ปฏิวัติวงการ!

✨ ลักษณะเด่น:
• Feature 1
• Feature 2
• Feature 3

🎁 โปรโมชั่น: ลด 20% สำหรับ 100 คนแรก!

👉 สั่งเลยวันนี้ [Link]

#NewProduct #TechSpark"
```

### 2. สร้าง Email Campaign
```
User: "สร้าง Email Campaign สำหรับ Newsletter"
Agent: "📧 Email Campaign:

Subject: 🎉 ลด 30% สำหรับสมาชิก!

Dear [Name],

ขอบคุณที่เป็นสมาชิก TechSpark!
[Content]
[CTA Button]"
```

### 3. สร้าง Content Calendar
```
User: "สร้าง Content Calendar สำหรับเดือนนี้"
Agent: "📅 Content Calendar:

Week 1: Product Showcase
Week 2: Customer Testimonials
Week 3: Educational Content
Week 4: Promotional Campaign"
```

---

## 🔧 Configuration

### config.json

```json
{
  "name": "Marketing Agent",
  "description": "Content creation for social media and email marketing",
  "model": "gpt-4",
  "temperature": 0.8,
  "maxTokens": 2000,
  "language": "Thai",
  "tone": "Creative and Engaging",
  "context": {
    "company": "Your Company Name",
    "brandVoice": "Professional yet friendly",
    "targetAudience": "Thai SMEs",
    "platforms": ["Facebook", "Instagram", "LinkedIn", "Email"],
    "contentTypes": ["Product Launch", "Promotion", "Educational", "Testimonial"]
  }
}
```

---

## 💬 System Prompt

```
You are a creative marketing specialist for [COMPANY_NAME].

Your responsibilities:
1. Create engaging social media content
2. Write compelling email campaigns
3. Generate content calendar ideas
4. Analyze trending topics
5. Optimize content for different platforms

Guidelines:
- Always respond in Thai language
- Create engaging and shareable content
- Include relevant hashtags and emojis
- Optimize for each platform
- Include clear call-to-action
- Follow brand guidelines
- Keep content authentic and relatable
```

---

## 📝 Prompt Templates

### Facebook Post Template

```json
{
  "template": "facebook_post",
  "prompt": "Create an engaging Facebook post about [TOPIC]. Include emojis, hashtags, and a clear call-to-action. Make it shareable and engaging for Thai audience.",
  "variables": ["TOPIC"]
}
```

### Email Campaign Template

```json
{
  "template": "email_campaign",
  "prompt": "Write an email campaign for [CAMPAIGN_TYPE]. Include subject line, body content, and CTA. Make it compelling and conversion-focused.",
  "variables": ["CAMPAIGN_TYPE"]
}
```

### Content Calendar Template

```json
{
  "template": "content_calendar",
  "prompt": "Create a monthly content calendar with [NUMBER] posts. Include topics, posting times, and content types.",
  "variables": ["NUMBER"]
}
```

---

## 📊 Example Content

### Example 1: Facebook Post

```
🎉 ประกาศสินค้าใหม่! 🎉

ยินดีต้อนรับ TechSpark AI Platform - ที่ทำให้ AI ใกล้ตัวคุณมากขึ้น!

✨ ไม่ต้องเขียนโค้ด
✨ ใช้งานง่าย
✨ ราคาประหยัด

🚀 เริ่มต้นฟรี 14 วัน - ไม่ต้องใส่บัตรเครดิต!

👉 ลองใช้เลยวันนี้: [Link]

#AI #TechSpark #SME #ไทย
```

### Example 2: Email Campaign

```
📧 Email Subject: 🎁 ลด 30% สำหรับสมาชิก!

---

Dear [Customer Name],

ขอบคุณที่เป็นสมาชิก TechSpark AI Platform!

เพื่อแสดงความขอบคุณ เรามีส่วนลด 30% สำหรับคุณ

🎁 ส่วนลด 30%
⏰ ใช้ได้ 7 วันเท่านั้น
💰 ประหยัดได้ถึง 3,000 บาท

👉 อ้างอิง Coupon Code: THANKYOU30

[Button: Redeem Now]

ขอบคุณและหวังว่าจะได้บริการคุณต่อไป

Best regards,
TechSpark AI Team
```

### Example 3: Instagram Caption

```
🤖 AI ไม่ยากอีกต่อไป!

TechSpark AI Platform ทำให้ SME ไทยสามารถใช้ AI ได้ง่ายๆ

✅ ไม่ต้องมีทีม Tech
✅ ใช้งานง่าย
✅ ราคาประหยัด

👉 ลิงก์ใน Bio

#AI #TechSpark #SME #Thailand #Innovation
```

---

## 🚀 Integration

### With Backend API

```typescript
// backend/routes/agents/marketing.ts
import { MarketingAgent } from '@techspark/agents'

app.post('/api/agents/marketing/create-content', async (req, res) => {
  const { contentType, topic, platform } = req.body
  
  const agent = new MarketingAgent({
    apiKey: process.env.OPENAI_API_KEY,
    brandGuidelines: await db.brandGuidelines.get()
  })
  
  const content = await agent.generateContent({
    type: contentType,
    topic,
    platform
  })
  
  res.json({ content })
})
```

---

## 📈 Performance Metrics

- **Engagement Rate**: > 5%
- **Click-Through Rate**: > 2%
- **Conversion Rate**: > 1%
- **Share Rate**: > 3%
- **Comment Rate**: > 2%

---

## 🎨 Content Types

### Product Launch
- Teaser posts
- Feature highlights
- Pricing information
- Limited-time offers

### Educational Content
- How-to guides
- Tips and tricks
- Industry insights
- Case studies

### Promotional Content
- Flash sales
- Bundle offers
- Seasonal promotions
- Loyalty rewards

### Testimonials & Social Proof
- Customer reviews
- Success stories
- Before & after
- User-generated content

---

## 📚 Resources

- [Social Media Best Practices](../templates/social-media-best-practices.md)
- [Email Marketing Guide](../templates/email-marketing-guide.md)
- [Content Calendar Template](../templates/content-calendar.json)

---

## 📄 License

MIT License - See [LICENSE](../../LICENSE)

---

**Made with ❤️ by TechSpark AI**
