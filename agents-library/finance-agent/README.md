# Finance Agent 💰

ตัวแทนการเงินที่วิเคราะห์ใบเสร็จ สรุปรายงานการเงิน และติดตามค่าใช้จ่าย

---

## 🎯 ลักษณะเด่น

- ✅ วิเคราะห์ใบเสร็จ (Invoice)
- ✅ สรุปรายงานการเงิน
- ✅ ติดตามค่าใช้จ่าย
- ✅ ทำนายแนวโน้มรายได้
- ✅ จัดการงบประมาณ

---

## 📋 Use Cases

### 1. วิเคราะห์ใบเสร็จ
```
User: "วิเคราะห์ใบเสร็จเดือนมีนาคม"
Agent: "📊 วิเคราะห์ใบเสร็จ:
- รายได้รวม: 500,000 บาท
- ค่าใช้จ่าย: 300,000 บาท
- กำไร: 200,000 บาท
- Margin: 40%"
```

### 2. สรุปรายงานรายเดือน
```
User: "สรุปรายงานการเงินเดือนนี้"
Agent: "📈 รายงานการเงิน:
- Revenue: 500,000 บาท
- Expenses: 300,000 บาท
- Profit: 200,000 บาท
- Growth: +15% YoY"
```

### 3. ติดตามค่าใช้จ่าย
```
User: "ค่าใช้จ่ายเดือนนี้เกินงบประมาณไหม?"
Agent: "✅ ค่าใช้จ่ายอยู่ในงบประมาณ:
- งบประมาณ: 350,000 บาท
- ใช้ไป: 300,000 บาท
- เหลือ: 50,000 บาท"
```

---

## 🔧 Configuration

### config.json

```json
{
  "name": "Finance Agent",
  "description": "Financial analysis and reporting for business insights",
  "model": "gpt-4",
  "temperature": 0.5,
  "maxTokens": 2000,
  "language": "Thai",
  "tone": "Professional and Analytical",
  "context": {
    "company": "Your Company Name",
    "currency": "THB",
    "fiscalYear": "Calendar Year",
    "reportingFrequency": "Monthly",
    "budgetCategories": [
      "Salaries",
      "Operations",
      "Marketing",
      "Technology",
      "Other"
    ]
  }
}
```

---

## 💬 System Prompt

```
You are a financial analyst for [COMPANY_NAME].

Your responsibilities:
1. Analyze invoices and receipts
2. Generate financial reports
3. Track expenses and budgets
4. Forecast revenue trends
5. Provide financial insights

Guidelines:
- Always respond in Thai language
- Provide accurate financial data
- Use clear visualizations
- Include actionable insights
- Maintain confidentiality
- Follow accounting standards
- Present data professionally
```

---

## 📝 Prompt Templates

### Invoice Analysis Template

```json
{
  "template": "invoice_analysis",
  "prompt": "Analyze the following invoice data: [INVOICE_DATA]. Provide breakdown by category, identify trends, and highlight any anomalies.",
  "variables": ["INVOICE_DATA"]
}
```

### Financial Report Template

```json
{
  "template": "financial_report",
  "prompt": "Generate a monthly financial report for [MONTH]. Include revenue, expenses, profit, growth rate, and recommendations.",
  "variables": ["MONTH"]
}
```

### Budget Analysis Template

```json
{
  "template": "budget_analysis",
  "prompt": "Compare actual expenses against budget for [PERIOD]. Identify variances and provide recommendations.",
  "variables": ["PERIOD"]
}
```

---

## 📊 Example Reports

### Example 1: Monthly Financial Report

```
📊 รายงานการเงินประจำเดือน มีนาคม 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 สรุปรายได้ - Revenue Summary
┌─────────────────────────────────┐
│ รายได้รวม (Total Revenue)       │
│ 500,000 บาท                     │
│ ↑ 15% vs Feb                    │
│ ↑ 25% vs Mar 2025               │
└─────────────────────────────────┘

💸 สรุปค่าใช้จ่าย - Expense Summary
┌─────────────────────────────────┐
│ ค่าใช้จ่ายรวม (Total Expenses)   │
│ 300,000 บาท                     │
│ ↑ 5% vs Feb                     │
│ ↓ 10% vs Mar 2025               │
└─────────────────────────────────┘

📈 กำไร - Profit
┌─────────────────────────────────┐
│ กำไรสุทธิ (Net Profit)          │
│ 200,000 บาท                     │
│ Profit Margin: 40%              │
│ ↑ 20% vs Feb                    │
└─────────────────────────────────┘

📋 รายละเอียดค่าใช้จ่าย - Expense Breakdown
┌──────────────────────┬──────────┬─────────┐
│ หมวดหมู่              │ จำนวน    │ %       │
├──────────────────────┼──────────┼─────────┤
│ เงินเดือน            │ 150,000  │ 50%     │
│ ค่าดำเนินการ         │ 80,000   │ 27%     │
│ การตลาด             │ 50,000   │ 17%     │
│ อื่นๆ                │ 20,000   │ 6%      │
└──────────────────────┴──────────┴─────────┘

💡 ข้อเสนอแนะ - Recommendations
✅ รายได้เพิ่มขึ้นดี ต่อเนื่องเพิ่มเติม
⚠️ ค่าดำเนินการเพิ่มขึ้น ควรตรวจสอบ
✅ Profit Margin ดี ยังคงรักษาไว้

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Example 2: Budget vs Actual

```
📊 เปรียบเทียบงบประมาณกับค่าใช้จ่ายจริง

┌────────────────┬──────────┬──────────┬─────────┐
│ หมวดหมู่        │ งบประมาณ │ ใช้ไป    │ สถานะ   │
├────────────────┼──────────┼──────────┼─────────┤
│ เงินเดือน      │ 150,000  │ 150,000  │ ✅ OK   │
│ ค่าดำเนินการ   │ 100,000  │ 80,000   │ ✅ OK   │
│ การตลาด        │ 60,000   │ 50,000   │ ✅ OK   │
│ เทคโนโลยี      │ 40,000   │ 20,000   │ ✅ OK   │
│ อื่นๆ          │ 50,000   │ 20,000   │ ✅ OK   │
├────────────────┼──────────┼──────────┼─────────┤
│ รวม            │ 400,000  │ 320,000  │ ✅ OK   │
└────────────────┴──────────┴──────────┴─────────┘

✅ สถานะ: อยู่ในงบประมาณ
💰 เหลือ: 80,000 บาท (20%)
📈 Efficiency: 80%
```

### Example 3: Revenue Forecast

```
📈 ทำนายรายได้ 3 เดือนข้างหน้า

┌──────────┬──────────┬──────────┐
│ เดือน    │ ทำนาย    │ เปอร์เซ็นต์│
├──────────┼──────────┼──────────┤
│ เมษายน   │ 525,000  │ ↑ 5%     │
│ พฤษภาคม  │ 550,000  │ ↑ 5%     │
│ มิถุนายน  │ 580,000  │ ↑ 5%     │
└──────────┴──────────┴──────────┘

📊 Trend: ✅ Positive
💡 Recommendation: ✅ Continue current strategy
```

---

## 🚀 Integration

### With Backend API

```typescript
// backend/routes/agents/finance.ts
import { FinanceAgent } from '@techspark/agents'

app.post('/api/agents/finance/analyze', async (req, res) => {
  const { reportType, period } = req.body
  
  const agent = new FinanceAgent({
    apiKey: process.env.OPENAI_API_KEY,
    financialData: await db.financialData.get(period)
  })
  
  const report = await agent.generateReport({
    type: reportType,
    period
  })
  
  res.json({ report })
})
```

---

## 📈 Key Metrics

- **Revenue Growth**: Track month-over-month
- **Profit Margin**: Target > 30%
- **Expense Ratio**: Keep < 70%
- **Cash Flow**: Monitor weekly
- **Budget Variance**: Keep < 10%

---

## 📚 Financial Resources

- [Accounting Standards](../templates/accounting-standards.md)
- [Budget Template](../templates/budget-template.json)
- [Financial Report Template](../templates/financial-report.md)

---

## 📄 License

MIT License - See [LICENSE](../../LICENSE)

---

**Made with ❤️ by TechSpark AI**
