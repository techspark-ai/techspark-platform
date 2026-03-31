# TechSpark AI - Frontend

Frontend ของ TechSpark AI Platform สร้างด้วย Next.js 15 + React 19 + Tailwind CSS

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- npm หรือ pnpm

### Installation

```bash
cd frontend
npm install
npm run dev
```

เปิด [http://localhost:3000](http://localhost:3000)

---

## 📁 Project Structure

```
frontend/
├── app/                 # Next.js App Directory
│   ├── layout.tsx
│   ├── page.tsx
│   └── ...
├── components/          # Reusable React Components
│   ├── Navbar.tsx
│   ├── Footer.tsx
│   ├── ChatInterface.tsx
│   └── ...
├── pages/              # Page Components
│   ├── marketplace.tsx
│   ├── developers.tsx
│   └── ...
├── lib/                # Utility Functions
│   ├── mockAgents.ts
│   └── ...
├── styles/             # Global Styles
│   └── globals.css
├── public/             # Static Assets
└── package.json
```

---

## 🛠️ Available Scripts

```bash
# Development
npm run dev              # Start dev server

# Production
npm run build            # Build for production
npm start                # Start production server

# Code Quality
npm run lint             # Run ESLint
npm run format           # Format code with Prettier
npm run type-check       # Check TypeScript types

# Testing
npm run test             # Run tests
npm run test:watch       # Run tests in watch mode
```

---

## 🎨 Tech Stack

- **Framework**: Next.js 15
- **UI Library**: React 19
- **Styling**: Tailwind CSS 4
- **Language**: TypeScript
- **Animations**: Framer Motion
- **Icons**: Lucide React

---

## 📦 Key Dependencies

```json
{
  "next": "^15.0.0",
  "react": "^19.0.0",
  "tailwindcss": "^4.0.0",
  "typescript": "^5.0.0",
  "framer-motion": "^10.0.0"
}
```

---

## 🔧 Configuration

### Environment Variables

สร้าง `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:3001
NEXT_PUBLIC_OPENAI_API_KEY=your_key_here
```

### Tailwind CSS

ตั้งค่าใน `tailwind.config.ts`:

```typescript
import type { Config } from 'tailwindcss'

export default {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
} satisfies Config
```

---

## 📝 Pages

### Home Page (`/`)
- Hero Section
- Features Overview
- Testimonials
- Call to Action

### Marketplace (`/marketplace`)
- AI Agents Grid
- Search & Filter
- Agent Details
- Pricing

### Developers (`/developers`)
- Developer Resources
- API Documentation
- Revenue Sharing Info

### Contact (`/contact`)
- Contact Form
- Demo Booking
- Live Chat

---

## 🧩 Components

### Navbar
- Navigation Links
- Logo
- CTA Button

### Footer
- Links
- Newsletter Signup
- Social Media

### ChatInterface
- Message Display
- Input Field
- AI Response

### AgentCard
- Agent Info
- Pricing
- Call to Action

---

## 🎯 Features

- ✅ Responsive Design
- ✅ Dark Theme
- ✅ Smooth Animations
- ✅ SEO Optimized
- ✅ PWA Support
- ✅ TypeScript Support

---

## 🚀 Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Docker

```bash
# Build image
docker build -t techspark-frontend .

# Run container
docker run -p 3000:3000 techspark-frontend
```

### Manual

```bash
# Build
npm run build

# Start
npm start
```

---

## 📚 Resources

- [Next.js Docs](https://nextjs.org/docs)
- [React Docs](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [TypeScript](https://www.typescriptlang.org/)

---

## 🤝 Contributing

ดูรายละเอียดใน [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## 📄 License

MIT License - ดูรายละเอียดใน [LICENSE](../LICENSE)

---

**Made with ❤️ by TechSpark AI**
