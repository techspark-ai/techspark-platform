# TechSpark AI - Agents Library

ไลบรารี่ AI Agents Templates สำหรับ TechSpark Platform

---

## 🤖 Available Agents

### 1. **Sales Agent** 💼
ตอบคำถามลูกค้า + สร้างใบเสนอราคา

**Use Cases:**
- ตอบคำถามเกี่ยวกับสินค้า/บริการ
- สร้างใบเสนอราคา
- ติดตามการขาย

**Prompts:**
```json
{
  "system": "You are a professional sales representative...",
  "templates": {
    "greeting": "สวัสดีค่ะ! ยินดีต้อนรับสู่...",
    "product_info": "ผลิตภัณฑ์ของเรามี...",
    "quote": "ใบเสนอราคา..."
  }
}
```

---

### 2. **Support Agent** 🎧
ตอบคำถามลูกค้า 24/7 ในภาษาไทย

**Use Cases:**
- ตอบคำถาม FAQ
- แก้ปัญหาทั่วไป
- ส่งต่อไปยัง Human Agent

**Features:**
- Multi-language Support
- Ticket Creation
- Escalation Handling

---

### 3. **Marketing Agent** 📱
สร้างเนื้อหา Marketing

**Use Cases:**
- สร้างโพสต์ Facebook
- สร้าง Email Campaign
- สร้าง Social Media Content

**Templates:**
- Facebook Post
- Email Newsletter
- Instagram Caption
- LinkedIn Article

---

### 4. **HR Agent** 👥
จัดการ HR Operations

**Use Cases:**
- ตอบคำถามพนักงาน
- สรุป Leave Request
- ประกาศข่าวสาร

**Features:**
- Leave Management
- Policy Q&A
- Announcements

---

### 5. **Finance Agent** 💰
วิเคราะห์ข้อมูลการเงิน

**Use Cases:**
- วิเคราะห์ใบเสร็จ
- สรุปรายงานการเงิน
- ติดตามค่าใช้จ่าย

**Reports:**
- Monthly Summary
- Expense Analysis
- Revenue Report

---

## 📦 Directory Structure

```
agents-library/
├── sales-agent/
│   ├── README.md
│   ├── prompts.json
│   ├── examples.md
│   └── config.json
├── support-agent/
│   ├── README.md
│   ├── prompts.json
│   ├── examples.md
│   └── config.json
├── marketing-agent/
│   ├── README.md
│   ├── prompts.json
│   ├── examples.md
│   └── config.json
├── hr-agent/
│   ├── README.md
│   ├── prompts.json
│   ├── examples.md
│   └── config.json
├── finance-agent/
│   ├── README.md
│   ├── prompts.json
│   ├── examples.md
│   └── config.json
└── templates/
    ├── base-agent.json
    └── prompt-template.md
```

---

## 🚀 Quick Start

### Using an Agent

```javascript
import { SalesAgent } from '@techspark/agents'

const agent = new SalesAgent({
  apiKey: process.env.OPENAI_API_KEY,
  model: 'gpt-4'
})

const response = await agent.chat('ผลิตภัณฑ์ของคุณคืออะไร?')
console.log(response)
```

### Creating Custom Agent

```javascript
import { BaseAgent } from '@techspark/agents'

class CustomAgent extends BaseAgent {
  constructor(config) {
    super(config)
    this.systemPrompt = 'Your custom system prompt...'
  }

  async processMessage(message) {
    // Custom processing logic
    return await this.chat(message)
  }
}
```

---

## 📝 Prompt Structure

### System Prompt
```
You are a professional [Agent Type] for [Company Name].
Your responsibilities:
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

Guidelines:
- Always respond in Thai language
- Be professional and helpful
- Escalate to human if needed
```

### Context Template
```json
{
  "company": "Company Name",
  "industry": "Industry",
  "language": "Thai",
  "tone": "Professional",
  "context": {
    "products": [],
    "policies": [],
    "faq": []
  }
}
```

---

## 🔧 Configuration

### Agent Config
```json
{
  "name": "Sales Agent",
  "description": "Handles sales inquiries",
  "model": "gpt-4",
  "temperature": 0.7,
  "maxTokens": 2000,
  "systemPrompt": "...",
  "context": {
    "products": [],
    "pricing": []
  }
}
```

---

## 📚 Examples

### Sales Agent Example

**User:** "ราคาของ Product A เท่าไหร่?"

**Agent:** "สินค้า Product A ของเรามีราคา 999 บาท ซึ่งรวมค่าจัดส่งแล้ว คุณสนใจเลยหรือต้องการข้อมูลเพิ่มเติม?"

### Support Agent Example

**User:** "ฉันจะคืนสินค้าได้ไหม?"

**Agent:** "ได้ค่ะ! นโยบายการคืนสินค้าของเรา: 
- ภายใน 30 วัน
- สินค้าต้องอยู่ในสภาพดี
- มีใบเสร็จ

ต้องการความช่วยเหลือเพิ่มเติมไหมค่ะ?"

---

## 🎯 Best Practices

### Prompt Engineering
1. **Be Specific** - ระบุบทบาทและความรับผิดชอบอย่างชัดเจน
2. **Provide Context** - ให้ข้อมูลพื้นฐานที่เพียงพอ
3. **Set Guidelines** - กำหนดวิธีการตอบสนอง
4. **Test & Iterate** - ทดสอบและปรับปรุงอย่างต่อเนื่อง

### Performance
1. **Use Caching** - Cache คำตอบที่ซ้ำกัน
2. **Batch Requests** - รวมคำขอเข้าด้วยกัน
3. **Monitor Costs** - ติดตามค่าใช้งาน API
4. **Optimize Tokens** - ลดการใช้ Tokens

---

## 🔌 Integration

### With Backend API

```typescript
// backend/routes/agents.ts
import { SalesAgent } from '@techspark/agents'

app.post('/api/agents/sales/chat', async (req, res) => {
  const agent = new SalesAgent(config)
  const response = await agent.chat(req.body.message)
  res.json(response)
})
```

### With Frontend

```typescript
// frontend/hooks/useAgent.ts
const { response, loading } = useAgent('sales', message)
```

---

## 📊 Monitoring

### Metrics to Track
- Response Time
- Token Usage
- Error Rate
- User Satisfaction
- Conversion Rate

### Logging

```javascript
agent.on('message', (msg) => {
  console.log(`[${new Date()}] User: ${msg}`)
})

agent.on('response', (res) => {
  console.log(`[${new Date()}] Agent: ${res}`)
})
```

---

## 🚀 Deployment

### Docker

```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY . .
RUN npm install

EXPOSE 3000
CMD ["npm", "start"]
```

### Environment Variables

```env
OPENAI_API_KEY=sk-...
AGENT_MODEL=gpt-4
AGENT_TEMPERATURE=0.7
AGENT_MAX_TOKENS=2000
```

---

## 🤝 Contributing

ต้องการสร้าง Agent ใหม่?

1. สร้าง Folder ใน `agents-library/`
2. เพิ่ม:
   - `README.md` - อธิบาย Agent
   - `prompts.json` - Prompt templates
   - `examples.md` - Usage examples
   - `config.json` - Configuration
3. Submit PR

---

## 📚 Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Best Practices](./templates/best-practices.md)

---

## 📄 License

MIT License - ดูรายละเอียดใน [LICENSE](../LICENSE)

---

**Made with ❤️ by TechSpark AI**
