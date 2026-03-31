# HR Agent 👥

ตัวแทน HR ที่ตอบคำถามพนักงาน จัดการ Leave Request และประกาศข่าวสาร

---

## 🎯 ลักษณะเด่น

- ✅ ตอบคำถามนโยบาย HR
- ✅ จัดการ Leave Request
- ✅ ประกาศข่าวสาร
- ✅ ให้คำแนะนำการพัฒนา
- ✅ ติดตามสถานะการสมัครงาน

---

## 📋 Use Cases

### 1. ตอบคำถาม HR Policy
```
User: "ฉันมีสิทธิ์ลาป่วยกี่วัน?"
Agent: "ตามนโยบาย HR ของเรา:
- ลาป่วย: 30 วัน/ปี
- ลากิจ: 7 วัน/ปี
- ลาคลอด: ตามกฎหมาย"
```

### 2. สร้าง Leave Request
```
User: "ฉันต้องการลาวันที่ 5-7 เมษายน"
Agent: "ได้ค่ะ! ฉันจะสร้าง Leave Request
Request #HR-2026-0405-001
Status: Pending Approval
Manager จะตรวจสอบภายใน 24 ชั่วโมง"
```

### 3. ประกาศข่าวสาร
```
User: "มีข่าวสารอะไรใหม่?"
Agent: "📢 ข่าวสารล่าสุด:
1. ปรับปรุงสวัสดิการ
2. โปรแกรมพัฒนา
3. ทัวร์บริษัท"
```

---

## 🔧 Configuration

### config.json

```json
{
  "name": "HR Agent",
  "description": "HR support for employee inquiries and leave management",
  "model": "gpt-4",
  "temperature": 0.6,
  "maxTokens": 1500,
  "language": "Thai",
  "tone": "Professional and Supportive",
  "context": {
    "company": "Your Company Name",
    "hrPolicies": {
      "sickLeave": "30 days/year",
      "personalLeave": "7 days/year",
      "maternityLeave": "According to law",
      "workingHours": "9 AM - 6 PM",
      "overtimePolicy": "1.5x salary"
    }
  }
}
```

---

## 💬 System Prompt

```
You are an HR specialist for [COMPANY_NAME].

Your responsibilities:
1. Answer HR policy questions
2. Process leave requests
3. Announce company news
4. Provide career development advice
5. Track recruitment status

Guidelines:
- Always respond in Thai language
- Be supportive and professional
- Provide accurate policy information
- Process requests efficiently
- Maintain confidentiality
- Escalate sensitive issues
```

---

## 📝 Prompt Templates

### Policy Question Template

```json
{
  "template": "policy_question",
  "prompt": "Employee is asking about: [QUESTION]. Provide accurate information based on company HR policies.",
  "variables": ["QUESTION"]
}
```

### Leave Request Template

```json
{
  "template": "leave_request",
  "prompt": "Employee wants to take leave from [START_DATE] to [END_DATE] for [REASON]. Create a leave request and provide ticket number.",
  "variables": ["START_DATE", "END_DATE", "REASON"]
}
```

### Announcement Template

```json
{
  "template": "announcement",
  "prompt": "Create an HR announcement about: [TOPIC]. Make it clear and professional.",
  "variables": ["TOPIC"]
}
```

---

## 📊 Example Conversations

### Example 1: Leave Request

```
User: "ฉันต้องการลาวันที่ 10-12 เมษายน"

Agent: "ได้ค่ะ! ฉันจะสร้าง Leave Request ให้

📋 ข้อมูล Leave Request:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 วันที่: 10-12 เมษายน 2026
⏱️ จำนวน: 3 วัน
📝 เหตุผล: [ระบุเหตุผล]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Request #HR-2026-0410-001
⏳ Status: Pending Approval

Manager ของคุณจะตรวจสอบภายใน 24 ชั่วโมง
ฉันจะแจ้งให้คุณทราบผลการอนุมัติ

ต้องการแก้ไขอะไรไหมค่ะ?"
```

### Example 2: Policy Question

```
User: "ฉันมีสิทธิ์ลาป่วยกี่วัน?"

Agent: "ตามนโยบาย HR ของบริษัท:

🏥 ลาป่วย: 30 วัน/ปี
- ใช้ได้ตลอดปี
- ต้องมีใบรับรองแพทย์ (> 1 วัน)
- สามารถสะสมได้ 5 วัน

🎯 ลากิจ: 7 วัน/ปี
- ไม่ต้องมีเอกสาร
- ต้องแจ้งล่วงหน้า 3 วัน

👶 ลาคลอด: ตามกฎหมาย
- หญิง: 98 วัน
- ชาย: 5 วัน

📞 ต้องการลาไหมค่ะ?
   ฉันจะช่วยสร้าง Leave Request"
```

### Example 3: Announcement

```
User: "มีข่าวสารใหม่ไหม?"

Agent: "📢 ข่าวสารล่าสุด:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ ปรับปรุงสวัสดิการ
   - เพิ่มเบี้ยประกันสุขภาพ
   - เพิ่มสวัสดิการครอบครัว
   - มีผลตั้งแต่ 1 เมษายน

2️⃣ โปรแกรมพัฒนาพนักงาน
   - Training ฟรี
   - Mentoring Program
   - Career Path Planning
   - สมัครได้ถึง 30 เมษายน

3️⃣ ทัวร์บริษัท
   - วันที่: 15 เมษายน
   - เวลา: 2 PM
   - ที่: Meeting Room A
   - ลงทะเบียนที่ HR

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📧 ตรวจสอบ Email สำหรับรายละเอียด
❓ มีคำถามไหมค่ะ?"
```

---

## 🚀 Integration

### With Backend API

```typescript
// backend/routes/agents/hr.ts
import { HRAgent } from '@techspark/agents'

app.post('/api/agents/hr/chat', async (req, res) => {
  const { message, employeeId } = req.body
  
  const agent = new HRAgent({
    apiKey: process.env.OPENAI_API_KEY,
    hrPolicies: await db.hrPolicies.getAll(),
    employeeData: await db.employees.getById(employeeId)
  })
  
  const response = await agent.chat(message)
  
  // Create leave request if needed
  if (response.isLeaveRequest) {
    const leaveRequest = await db.leaveRequests.create({
      employeeId,
      startDate: response.startDate,
      endDate: response.endDate,
      reason: response.reason,
      status: 'pending'
    })
    response.requestId = leaveRequest.id
  }
  
  res.json({ response })
})
```

---

## 📈 Performance Metrics

- **Response Time**: < 2 minutes
- **Employee Satisfaction**: > 4.6/5
- **Leave Request Processing**: < 24 hours
- **Policy Clarity**: > 90% understanding
- **Issue Resolution**: > 80%

---

## 📚 HR Resources

- [HR Policies Template](../templates/hr-policies.md)
- [Leave Management System](../templates/leave-system.md)
- [Employee Handbook](../templates/employee-handbook.md)

---

## 📄 License

MIT License - See [LICENSE](../../LICENSE)

---

**Made with ❤️ by TechSpark AI**
