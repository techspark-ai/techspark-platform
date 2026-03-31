# TechSpark AI - Setup Guide

คู่มือการ Setup และ Deploy TechSpark AI Platform

---

## 📋 Prerequisites

### System Requirements
- **OS**: macOS, Linux, หรือ Windows (WSL2)
- **Node.js**: 18.0.0 หรือสูงกว่า
- **npm**: 9.0.0 หรือสูงกว่า
- **Git**: 2.0.0 หรือสูงกว่า

### Accounts Required
- GitHub Account
- OpenAI Account (สำหรับ API Key)
- Stripe Account (สำหรับ Payment - Optional)

---

## 🚀 Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/techspark-ai/techspark-platform.git
cd techspark-platform
```

### Step 2: Install Dependencies

```bash
# Install frontend dependencies
cd frontend
npm install

# Back to root
cd ..
```

### Step 3: Setup Environment Variables

สร้าง `.env.local` ในโฟลเดอร์ `frontend/`:

```env
# OpenAI Configuration
NEXT_PUBLIC_OPENAI_API_KEY=sk-your-api-key-here

# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:3001

# Analytics (Optional)
NEXT_PUBLIC_ANALYTICS_ID=your-analytics-id
```

### Step 4: Run Development Server

```bash
cd frontend
npm run dev
```

เปิด [http://localhost:3000](http://localhost:3000) ในเบราว์เซอร์

---

## 🔧 Configuration

### Frontend Configuration

#### Tailwind CSS

ตั้งค่าใน `frontend/tailwind.config.ts`:

```typescript
import type { Config } from 'tailwindcss'

export default {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0ea5e9',
        secondary: '#1e293b',
      },
    },
  },
  plugins: [],
} satisfies Config
```

#### Next.js Configuration

ตั้งค่าใน `frontend/next.config.ts`:

```typescript
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**',
      },
    ],
  },
}

export default nextConfig
```

---

## 🌐 Environment Variables

### Development

```env
# Frontend
NEXT_PUBLIC_API_URL=http://localhost:3001
NEXT_PUBLIC_OPENAI_API_KEY=sk-test-key

# Backend (Private)
DATABASE_URL=postgresql://user:password@localhost:5432/techspark
OPENAI_API_KEY=sk-test-key
JWT_SECRET=your-secret-key
STRIPE_SECRET_KEY=sk_test_xxxxx
```

### Production

```env
# Frontend
NEXT_PUBLIC_API_URL=https://api.techspark.ai
NEXT_PUBLIC_OPENAI_API_KEY=sk-prod-key

# Backend (Private)
DATABASE_URL=postgresql://prod-user:prod-pass@prod-db:5432/techspark_prod
OPENAI_API_KEY=sk-prod-key
JWT_SECRET=your-prod-secret-key
STRIPE_SECRET_KEY=sk_live_xxxxx
NODE_ENV=production
```

---

## 📦 Project Structure

```
techspark-platform/
├── frontend/                    # Next.js Frontend
│   ├── app/
│   ├── components/
│   ├── pages/
│   ├── public/
│   ├── styles/
│   ├── lib/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   └── next.config.ts
├── agents-library/              # AI Agents Templates
│   ├── sales-agent/
│   ├── support-agent/
│   ├── marketing-agent/
│   ├── hr-agent/
│   ├── finance-agent/
│   └── templates/
├── docs/                        # Documentation
│   ├── setup-guide.md
│   ├── api-reference.md
│   ├── architecture.md
│   └── examples/
├── LICENSE
├── README.md
└── .gitignore
```

---

## 🛠️ Development Workflow

### Running Development Server

```bash
cd frontend
npm run dev
```

### Building for Production

```bash
cd frontend
npm run build
npm start
```

### Running Tests

```bash
cd frontend
npm run test
npm run test:watch
npm run test:coverage
```

### Code Quality

```bash
# Linting
npm run lint

# Formatting
npm run format

# Type Checking
npm run type-check
```

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t techspark-frontend:latest .
```

### Run Docker Container

```bash
docker run -p 3000:3000 \
  -e NEXT_PUBLIC_API_URL=http://localhost:3001 \
  -e NEXT_PUBLIC_OPENAI_API_KEY=sk-xxx \
  techspark-frontend:latest
```

### Docker Compose

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:3001
      NEXT_PUBLIC_OPENAI_API_KEY: ${OPENAI_API_KEY}

  backend:
    build: ./backend
    ports:
      - "3001:3001"
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/techspark
      OPENAI_API_KEY: ${OPENAI_API_KEY}

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: techspark
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## 🚀 Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Netlify

```bash
# Install Netlify CLI
npm i -g netlify-cli

# Deploy
netlify deploy
```

### Self-Hosted

```bash
# Build
npm run build

# Start
npm start
```

---

## 🔐 Security

### Environment Variables
- ❌ ไม่ต้อง Commit `.env` files
- ✅ ใช้ `.env.example` สำหรับ Template
- ✅ ใช้ Secrets Management ของ Hosting Platform

### API Keys
- ✅ ใช้ Environment Variables
- ✅ Rotate keys อย่างสม่ำเสมอ
- ✅ ใช้ Rate Limiting

### CORS
```typescript
// backend/middleware/cors.ts
const corsOptions = {
  origin: process.env.FRONTEND_URL,
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
}
```

---

## 🧪 Testing

### Unit Tests

```bash
npm run test
```

### Integration Tests

```bash
npm run test:integration
```

### E2E Tests

```bash
npm run test:e2e
```

---

## 📊 Monitoring

### Application Monitoring
- Sentry สำหรับ Error Tracking
- LogRocket สำหรับ Session Replay
- Google Analytics สำหรับ User Analytics

### Performance Monitoring
- Lighthouse
- Web Vitals
- Performance API

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Or use different port
PORT=3001 npm run dev
```

### Node Modules Issues

```bash
# Clear cache
npm cache clean --force

# Reinstall
rm -rf node_modules package-lock.json
npm install
```

### Build Errors

```bash
# Check TypeScript errors
npm run type-check

# Check linting errors
npm run lint
```

---

## 📚 Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [TypeScript](https://www.typescriptlang.org/docs/)
- [OpenAI API](https://platform.openai.com/docs)

---

## 🆘 Support

- 📧 Email: support@techspark.ai
- 💬 Discord: [Join Community](https://discord.gg/techspark)
- 🐛 Issues: [GitHub Issues](https://github.com/techspark-ai/techspark-platform/issues)

---

**Happy Coding! 🚀**
