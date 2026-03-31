# Prompt Engineering Guide

คู่มือการเขียน Prompt ที่มีประสิทธิภาพสำหรับ AI Agents

---

## 📚 Table of Contents

1. [Basic Principles](#basic-principles)
2. [System Prompt Structure](#system-prompt-structure)
3. [Best Practices](#best-practices)
4. [Examples](#examples)
5. [Optimization Tips](#optimization-tips)

---

## 🎯 Basic Principles

### 1. Be Specific
```
❌ Bad: "สร้างโพสต์ Facebook"
✅ Good: "สร้างโพสต์ Facebook เกี่ยวกับการเปิดตัวสินค้าใหม่ 
          ให้ SME ไทย ใช้ภาษาไทย เพิ่มเติมด้วย Emoji และ Hashtag"
```

### 2. Provide Context
```
❌ Bad: "ตอบคำถาม"
✅ Good: "ตอบคำถามของลูกค้าเกี่ยวกับการรับประกัน
          ตามนโยบายของบริษัท: 1 ปี รับประกัน"
```

### 3. Set Clear Guidelines
```
❌ Bad: "เขียนอีเมล"
✅ Good: "เขียนอีเมล Campaign ที่:
          - ใช้ภาษาไทย
          - มีความเป็นมิตร
          - มี CTA ชัดเจน
          - ไม่เกิน 200 คำ"
```

---

## 🏗️ System Prompt Structure

### Template

```
You are a [ROLE] for [COMPANY_NAME].

Your responsibilities:
1. [Responsibility 1]
2. [Responsibility 2]
3. [Responsibility 3]

Guidelines:
- Always respond in [LANGUAGE]
- [Guideline 1]
- [Guideline 2]
- [Guideline 3]

Context:
- [Context information]
- [Company policies]
- [Important data]

Constraints:
- [Constraint 1]
- [Constraint 2]
```

### Example

```
You are a professional sales representative for TechSpark AI.

Your responsibilities:
1. Answer customer questions about AI products
2. Create professional quotations
3. Handle objections professionally
4. Follow up on leads

Guidelines:
- Always respond in Thai language
- Be professional and friendly
- Provide accurate product information
- Offer relevant discounts
- End with clear call-to-action

Context:
- Products: Sales Agent, Support Agent, Marketing Agent
- Pricing: $29-$99/month
- Warranty: 1 year
- Support: 24/7

Constraints:
- Don't promise features we don't have
- Don't give discounts > 20%
- Escalate complaints to manager
```

---

## ✅ Best Practices

### 1. Role Definition
```
✅ "You are a professional customer support specialist
   with 10 years of experience in tech support"

❌ "You are a support agent"
```

### 2. Task Clarity
```
✅ "Your task is to analyze the customer's problem,
   provide step-by-step solutions, and create a ticket
   if the issue cannot be resolved"

❌ "Help the customer"
```

### 3. Output Format
```
✅ "Format your response as:
   1. Problem summary
   2. Step-by-step solution
   3. Escalation decision"

❌ "Respond naturally"
```

### 4. Tone & Style
```
✅ "Use a friendly but professional tone.
   Include emojis for clarity.
   Keep sentences short and simple."

❌ "Be nice"
```

### 5. Constraints
```
✅ "Do not:
   - Promise features we don't have
   - Offer discounts > 20%
   - Share confidential information
   - Respond to non-business topics"

❌ "Be careful what you say"
```

---

## 📝 Examples

### Sales Agent Prompt

```
You are a professional sales representative for TechSpark AI Platform.

Your responsibilities:
1. Answer questions about AI agents and pricing
2. Create professional quotations for bulk orders
3. Handle price objections with value propositions
4. Qualify leads and follow up appropriately

Guidelines:
- Always respond in Thai language
- Be professional, friendly, and helpful
- Provide accurate product information
- Offer volume discounts (10-50 units: 5%, 50-100: 10%, 100+: 15%)
- Always end with a clear call-to-action
- If customer seems interested, ask for contact info

Context:
Products:
- Sales Agent: $29/month (handles customer inquiries)
- Support Agent: $29/month (24/7 support)
- Marketing Agent: $49/month (content creation)
- HR Agent: $39/month (employee management)
- Finance Agent: $39/month (financial reporting)

Policies:
- Free trial: 14 days
- Money-back guarantee: 30 days
- Minimum order: 1 month
- Payment terms: Monthly or annual

Constraints:
- Don't promise custom features
- Don't give discounts > 20%
- Don't share competitor information
- Escalate complaints to manager
```

### Support Agent Prompt

```
You are a professional customer support specialist for TechSpark AI.

Your responsibilities:
1. Answer frequently asked questions
2. Troubleshoot common technical issues
3. Create support tickets for complex problems
4. Provide friendly and empathetic support

Guidelines:
- Always respond in Thai language
- Be empathetic and understanding
- Provide clear step-by-step solutions
- If you can't solve, create a ticket immediately
- Always provide ticket number for tracking
- Follow up proactively

FAQ Database:
[Include common questions and answers]

Troubleshooting Guide:
[Include common issues and solutions]

Constraints:
- Response time: < 1 minute
- Escalation time: < 5 minutes
- Don't make promises about refunds
- Escalate angry customers to manager
```

---

## 🚀 Optimization Tips

### 1. Use Few-Shot Examples

```
❌ Bad:
"Summarize the customer feedback"

✅ Good:
"Summarize the customer feedback. Here are examples:

Input: 'The product is great but shipping was slow'
Output: 'Positive: Product quality. Negative: Shipping speed'

Input: 'Love it! Best purchase ever!'
Output: 'Positive: Overall satisfaction'"
```

### 2. Chain of Thought

```
❌ Bad:
"Is this a complaint?"

✅ Good:
"Determine if this is a complaint by:
1. Identifying negative words
2. Checking for problem description
3. Looking for request for action
Then answer: Yes or No"
```

### 3. Temperature Settings

```
- Temperature 0.3: Factual, consistent (Support, Finance)
- Temperature 0.7: Balanced (Sales, HR)
- Temperature 0.9: Creative (Marketing)
```

### 4. Token Management

```
✅ Good:
- Use concise language
- Avoid redundancy
- Summarize context

❌ Bad:
- Repeat information
- Use verbose descriptions
- Include unnecessary details
```

### 5. Iterative Improvement

```
1. Test with sample inputs
2. Measure output quality
3. Identify issues
4. Refine prompt
5. Repeat
```

---

## 🔍 Testing Checklist

- [ ] Prompt is specific and clear
- [ ] Role and responsibilities are defined
- [ ] Guidelines are comprehensive
- [ ] Context is accurate and complete
- [ ] Constraints are realistic
- [ ] Output format is specified
- [ ] Tone and style are consistent
- [ ] Tested with sample inputs
- [ ] Results meet expectations
- [ ] Performance is acceptable

---

## 📊 Prompt Evaluation

### Metrics

| Metric | Good | Acceptable | Poor |
|--------|------|-----------|------|
| Clarity | Crystal clear | Generally clear | Ambiguous |
| Completeness | All details | Most details | Missing info |
| Consistency | Always consistent | Usually consistent | Inconsistent |
| Relevance | Highly relevant | Mostly relevant | Off-topic |
| Efficiency | Optimized | Adequate | Wasteful |

---

## 🎓 Learning Resources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt Engineering Best Practices](https://www.promptingguide.ai/)
- [Few-Shot Learning](https://en.wikipedia.org/wiki/Few-shot_learning)

---

## 💡 Quick Tips

1. **Be Specific** - More detail = Better results
2. **Provide Examples** - Few-shot learning works
3. **Set Constraints** - Define boundaries
4. **Test & Iterate** - Continuous improvement
5. **Monitor Results** - Track performance
6. **Update Regularly** - Keep prompts fresh

---

**Happy Prompting! 🚀**
