# TechSpark AI Platform

> **AI Agent Marketplace for Thai SMEs** - ทำให้ SME ไทยเข้าถึง AI ได้ง่ายๆ ด้วยราคาที่ประหยัด

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/techspark-ai/techspark-platform?style=social)](https://github.com/techspark-ai/techspark-platform)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![React](https://img.shields.io/badge/React-19-blue.svg)](https://react.dev/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black.svg)](https://nextjs.org/)

---

## 🎯 ภาพรวม

**TechSpark AI** เป็นแพลตฟอร์ม Marketplace ที่เชื่อมต่อ Developers และ SME Businesses เพื่อให้ SME สามารถใช้ AI Agents ได้ง่ายๆ โดยไม่ต้องเขียนโค้ด

### ✨ ลักษณะเด่น

- 🚀 **No-Code Deployment** - SME สามารถใช้ AI ได้ทันที โดยไม่ต้องเขียนโค้ด
- 💰 **Revenue Sharing Model** - Developers ได้ 70% ของรายได้
- ⚡ **Fast to Market** - Launch ได้ใน 1 สัปดาห์ ด้วย OpenAI API
- 🇹🇭 **Local First** - ออกแบบสำหรับ SME ไทย ใช้ภาษาไทยได้ดี
- 💬 **Chat Interface** - ใช้งานง่ายเหมือนการพูดคุยกับ AI

---

## 📦 โครงสร้างโปรเจกต์

```
techspark-platform/
├── frontend/                    # Next.js Landing Page + Chat UI
│   ├── app/
│   ├── components/
│   ├── pages/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   └── README.md
├── agents-library/              # AI Agents Templates & Examples
│   ├── sales-agent/
│   ├── support-agent/
│   ├── marketing-agent/
│   ├── hr-agent/
│   ├── finance-agent/
│   ├── templates/
│   └── README.md
├── docs/                        # Documentation
│   ├── setup-guide.md
│   ├── api-reference.md
│   ├── architecture.md
│   ├── contributing.md
│   └── examples/
├── LICENSE                      # MIT License
├── README.md                    # This file
└── .gitignore
```

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- npm หรือ pnpm
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/techspark-ai/techspark-platform.git
cd techspark-platform

# Install dependencies
cd frontend
npm install

# Run development server
npm run dev
```

เปิด [http://localhost:3000](http://localhost:3000) ในเบราว์เซอร์

---

## 📚 Documentation

- **[Setup Guide](./docs/setup-guide.md)** - วิธีการ Setup และ Deploy
- **[API Reference](./docs/api-reference.md)** - API Documentation
- **[Architecture](./docs/architecture.md)** - System Architecture
- **[Agents Library](./agents-library/README.md)** - AI Agents Templates

---

## 🤖 AI Agents ตัวอย่าง

TechSpark Platform มาพร้อม AI Agents Templates สำหรับ SME:

### 1. **Sales AI** 💼
ตอบคำถามลูกค้า + สร้างใบเสนอราคา

### 2. **Support AI** 🎧
ตอบคำถามลูกค้า 24/7 ในภาษาไทย

### 3. **Marketing AI** 📱
สร้างโพสต์ Facebook + Email Campaign

### 4. **HR AI** 👥
ตอบคำถามพนักงาน + สรุป Leave Request

### 5. **Finance AI** 💰
วิเคราะห์ใบเสร็จ + สรุปรายงาน

---

## 💡 Use Cases

### สำหรับ SME
- ✅ ตอบคำถามลูกค้าอัตโนมัติ
- ✅ สร้างเนื้อหา Marketing
- ✅ วิเคราะห์ข้อมูลธุรกิจ
- ✅ จัดการ HR Operations

### สำหรับ Developers
- ✅ สร้าง Custom AI Agents
- ✅ ได้รับรายได้จาก Revenue Sharing
- ✅ ไม่ต้องกังวล Infrastructure

---

## 🔧 Tech Stack

### Frontend
- **Next.js 15** - React Framework
- **React 19** - UI Library
- **Tailwind CSS 4** - Styling
- **TypeScript** - Type Safety
- **Framer Motion** - Animations

### Backend (Private)
- **Node.js/Python** - Server Runtime
- **Express.js/FastAPI** - Web Framework
- **PostgreSQL** - Database
- **OpenAI API** - AI Engine
- **Stripe** - Payment Processing

---

## 📊 Pricing

| Plan | Price | Features |
|------|-------|----------|
| **Free Trial** | $0 | 5 messages/day, 14 days access |
| **Starter** | $29/month | 100 messages, 1 Agent |
| **Professional** | $99/month | Unlimited messages, 5 Agents |
| **Enterprise** | Custom | Unlimited everything, Dedicated support |

---

## 🤝 Contributing

เราต้อนรับการ Contribute จาก Community! 

### วิธีการ Contribute

1. Fork repository นี้
2. สร้าง feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

อ่านรายละเอียดเพิ่มเติมใน [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📋 Roadmap

- [x] Landing Page
- [x] Marketplace UI
- [x] Agents Library Templates
- [ ] Backend API (Private)
- [ ] Payment Integration
- [ ] Analytics Dashboard
- [ ] Mobile App
- [ ] Multi-language Support

---

## 📄 License

Project นี้ใช้ **MIT License** - ดูรายละเอียดใน [LICENSE](./LICENSE) file

---

## 🙋 Support

- 📧 **Email**: support@techspark.ai
- 💬 **Discord**: [Join Community](https://discord.gg/techspark)
- 🐛 **Issues**: [GitHub Issues](https://github.com/techspark-ai/techspark-platform/issues)
- 📖 **Docs**: [Documentation](./docs)

---

## 🌟 Acknowledgments

- OpenAI สำหรับ GPT-4 API
- Next.js Community
- React Community
- Tailwind CSS Team

---

## 📈 Statistics

- ⭐ GitHub Stars: [View](https://github.com/techspark-ai/techspark-platform)
- 📦 NPM Downloads: [View](https://www.npmjs.com/package/techspark-platform)
- 👥 Contributors: [View](https://github.com/techspark-ai/techspark-platform/graphs/contributors)

---

## 🎯 Vision

ทำให้ AI เข้าถึงได้สำหรับทุก SME ในประเทศไทย โดยไม่ต้องมีทีม Tech ที่มีค่าใช้จ่ายสูง

**มาสร้าง AI Future สำหรับ SME ไทยด้วยกัน! 🚀**

---

**Made with ❤️ by [TechSpark AI](https://techspark.ai)**
