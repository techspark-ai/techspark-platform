# Sales Agent 💼

ตัวแทนขายอัตโนมัติที่ตอบคำถามลูกค้า สร้างใบเสนอราคา และติดตามการขาย

---

## 🎯 ลักษณะเด่น

- ✅ ตอบคำถามเกี่ยวกับสินค้า/บริการ
- ✅ สร้างใบเสนอราคา (Quote)
- ✅ ติดตามการขาย
- ✅ ให้คำแนะนำการขาย
- ✅ จัดการ Lead Qualification

---

## 📋 Use Cases

### 1. ตอบคำถามสินค้า
```
User: "ผลิตภัณฑ์ A มีขนาดเท่าไหร่?"
Agent: "ผลิตภัณฑ์ A มีขนาด 3 รุ่น: Small, Medium, Large..."
```

### 2. สร้างใบเสนอราคา
```
User: "ฉันต้องการสั่ง 100 ชิ้น"
Agent: "ใบเสนอราคา:
- ราคาต่อหน่วย: 500 บาท
- จำนวน: 100 ชิ้น
- รวม: 50,000 บาท
- ส่วนลด 10%: 45,000 บาท"
```

### 3. ติดตามการขาย
```
User: "ฉันสนใจสินค้านี้ แต่ต้องคิดก่อน"
Agent: "ไม่เป็นไร ฉันจะส่งข้อมูลเพิ่มเติมให้คุณ
และติดตามอีกครั้งในวันพรุ่งนี้"
```

---

## 🔧 Configuration

### config.json

```json
{
  "name": "Sales Agent",
  "description": "Professional sales representative for customer inquiries",
  "model": "gpt-4",
  "temperature": 0.7,
  "maxTokens": 2000,
  "language": "Thai",
  "tone": "Professional and Friendly",
  "context": {
    "company": "Your Company Name",
    "industry": "Your Industry",
    "products": [
      {
        "id": "prod_001",
        "name": "Product A",
        "price": 500,
        "description": "High-quality product..."
      }
    ],
    "policies": {
      "discount": "10% for bulk orders",
      "warranty": "1 year warranty",
      "delivery": "Free shipping for orders > 5000 baht"
    }
  }
}
```

---

## 💬 System Prompt

```
You are a professional sales representative for [Company Name].

Your responsibilities:
1. Answer customer questions about products and services
2. Provide product recommendations based on customer needs
3. Create professional quotations
4. Handle objections professionally
5. Follow up on leads

Guidelines:
- Always respond in Thai language
- Be professional, friendly, and helpful
- Provide accurate product information
- Offer relevant discounts and promotions
- If you don't know something, offer to connect with a specialist
- Always end with a clear call to action

Company Information:
- Products: [List of products]
- Pricing: [Pricing information]
- Policies: [Company policies]
- Special Offers: [Current promotions]
```

---

## 📝 Prompt Templates

### Product Inquiry Template

```json
{
  "template": "product_inquiry",
  "prompt": "Customer is asking about [PRODUCT_NAME]. Provide detailed information including features, specifications, pricing, and availability. Suggest related products if relevant.",
  "variables": ["PRODUCT_NAME"]
}
```

### Quote Generation Template

```json
{
  "template": "quote_generation",
  "prompt": "Generate a professional quotation for the following items: [ITEMS]. Include unit prices, quantities, subtotal, applicable discounts, and total. Format as a professional quote.",
  "variables": ["ITEMS"]
}
```

### Objection Handling Template

```json
{
  "template": "objection_handling",
  "prompt": "Customer has the following objection: [OBJECTION]. Address their concern professionally and provide solutions or alternatives.",
  "variables": ["OBJECTION"]
}
```

---

## 📊 Example Conversations

### Example 1: Product Inquiry

```
User: "สินค้าของคุณมีการรับประกันไหม?"

Agent: "ใช่ค่ะ! ผลิตภัณฑ์ทั้งหมดของเรามีการรับประกัน 1 ปี ซึ่งครอบคลุม:
- ข้อบกพร่องจากการผลิต
- ความเสียหายจากการใช้งานตามปกติ
- การซ่อมแซมฟรี

นอกจากนี้ เรายังให้บริการ After-Sales Support ตลอดเวลา
ต้องการข้อมูลเพิ่มเติมหรือต้องการสั่งซื้อไหมค่ะ?"
```

### Example 2: Quote Generation

```
User: "ฉันต้องการสั่ง Product A 50 ชิ้น และ Product B 30 ชิ้น"

Agent: "ขอบคุณที่สนใจค่ะ! นี่คือใบเสนอราคา:

📋 ใบเสนอราคา
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
รายการ              จำนวน    ราคา/หน่วย    รวม
Product A           50 ชิ้น   500 บาท        25,000 บาท
Product B           30 ชิ้น   300 บาท        9,000 บาท
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
รวมย่อย                                      34,000 บาท
ส่วนลด (10%)                                 -3,400 บาท
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
รวมทั้งสิ้น                                   30,600 บาท
ค่าจัดส่ง                                     ฟรี
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎁 โปรโมชั่น: ซื้อเลย วันนี้ ลด 10% เพิ่มเติม!

ใบเสนอราคานี้มีผลบังคับใช้ 7 วัน
ต้องการยืนยันการสั่งซื้อไหมค่ะ?"
```

### Example 3: Lead Follow-up

```
User: "ขอบคุณค่ะ ฉันต้องคิดก่อน"

Agent: "ไม่เป็นไรค่ะ! ฉันเข้าใจว่าการตัดสินใจต้องใช้เวลา

ฉันจะส่งข้อมูลเพิ่มเติมให้คุณ:
📧 ใบเสนอราคาฉบับเต็ม
📊 เปรียบเทียบกับสินค้าอื่น
💬 ตัวอย่างจากลูกค้าอื่น

และฉันจะติดตามอีกครั้งในวันพรุ่งนี้
หากมีคำถามเพิ่มเติม สามารถติดต่อฉันได้ตลอดเวลา

ขอบคุณที่สนใจค่ะ!"
```

---

## 🚀 Integration

### With Backend API

```typescript
// backend/routes/agents/sales.ts
import { SalesAgent } from '@techspark/agents'

app.post('/api/agents/sales/chat', async (req, res) => {
  const { message, context } = req.body
  
  const agent = new SalesAgent({
    apiKey: process.env.OPENAI_API_KEY,
    config: context.config
  })
  
  const response = await agent.chat(message)
  
  // Store conversation
  await db.conversations.create({
    userId: req.user.id,
    agentType: 'sales',
    message,
    response,
    timestamp: new Date()
  })
  
  res.json({ response })
})
```

### With Frontend

```typescript
// frontend/hooks/useSalesAgent.ts
import { useAgent } from '@/hooks/useAgent'

export function useSalesAgent() {
  const { response, loading, error } = useAgent('sales')
  
  return {
    response,
    loading,
    error,
    sendMessage: (message: string) => {
      // Send to API
    }
  }
}
```

---

## 📈 Performance Metrics

Track these metrics to measure effectiveness:

- **Response Time**: < 2 seconds
- **Customer Satisfaction**: > 4.5/5
- **Quote Acceptance Rate**: > 30%
- **Lead Conversion Rate**: > 15%
- **Average Order Value**: Track growth

---

## 🔄 Continuous Improvement

### Monitor & Optimize

1. **Analyze Conversations**
   - What questions are most common?
   - Where do customers drop off?
   - What objections need better handling?

2. **Update Prompts**
   - Refine responses based on feedback
   - Add new product information
   - Improve objection handling

3. **A/B Testing**
   - Test different greeting messages
   - Test different discount strategies
   - Measure impact on conversion

---

## 🤝 Best Practices

1. **Be Accurate** - Always provide correct product information
2. **Be Responsive** - Reply quickly to customer inquiries
3. **Be Professional** - Maintain professional tone
4. **Be Helpful** - Go extra mile to help customers
5. **Be Honest** - Don't oversell or make false claims

---

## 📚 Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Sales Best Practices](../templates/sales-best-practices.md)

---

## 📄 License

MIT License - See [LICENSE](../../LICENSE)

---

**Made with ❤️ by TechSpark AI**
