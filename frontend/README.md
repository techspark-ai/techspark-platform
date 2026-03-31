# TechSpark AI - Frontend

Professional landing page and web application for TechSpark AI Platform.

## 📋 Overview

This is the frontend for TechSpark AI Platform - an AI Agent Marketplace designed to help Thai SMEs adopt AI technology without technical expertise.

**Live Demo**: https://techspark-ai.vercel.app

## 🏗️ Architecture

```
frontend/
├── src/
│   ├── pages/           # Page components
│   │   └── Home.tsx     # Main landing page
│   ├── components/      # Reusable UI components
│   │   ├── ui/          # shadcn/ui components
│   │   ├── Navbar.tsx
│   │   └── Footer.tsx
│   ├── contexts/        # React contexts
│   ├── hooks/           # Custom React hooks
│   ├── lib/             # Utility functions
│   ├── App.tsx          # Main app component
│   ├── main.tsx         # React entry point
│   └── index.css        # Global styles
├── public/              # Static assets
│   ├── favicon.ico
│   └── robots.txt
└── package.json         # Dependencies
```

## 🚀 Features

### Hero Section
- **Compelling Headline**: "Every Business Deserves AI Employees"
- **Value Proposition**: Clear explanation of TechSpark AI
- **Call-to-Action**: Invest Now & View Pitch Deck buttons
- **Key Metrics**: TAM, ROI, Commission information
- **Animated Background**: Professional gradient with parallax effect

### Market Opportunity Section
- **Target Market**: 5M+ SMEs in Southeast Asia
- **Growth Drivers**: 87% of businesses plan AI investments
- **Market Size**: $10B+ TAM in Southeast Asia
- **Competitive Advantages**: Cost reduction, ease of use, no technical expertise required

### Features Section (Three Pillars)
1. **AI Agent Marketplace**
   - Browse and deploy AI agents in seconds
   - Pre-built solutions (Sales, Support, Marketing)
   - Instant deployment

2. **No-Code AI Builder**
   - Drag-and-drop workflow builder
   - Custom AI agent creation
   - No coding required

3. **AI Workforce Dashboard**
   - Performance monitoring
   - ROI tracking
   - Unified control center

### Business Model Section
- **Commission from Marketplace**: 20-30% per agent sold
- **Subscription Plans**: Free, Pro, Enterprise tiers
- **Usage-Based Pricing**: API calls, tokens, automation runs
- **Custom Solutions**: Premium service for enterprises

### Team Section
- Team member profiles
- Expertise and background
- Social links and contact

### CTA Section
- Investment opportunities
- Demo scheduling
- Contact information
- Newsletter signup

## 🛠️ Tech Stack

- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS 4** - Styling
- **shadcn/ui** - UI components
- **Framer Motion** - Animations
- **Lucide React** - Icons
- **Wouter** - Routing
- **Vite** - Build tool

## 📦 Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🎨 Design System

### Colors
- **Primary**: Cyan (#06B6D4)
- **Secondary**: Blue (#3B82F6)
- **Accent**: Purple (#A855F7)
- **Background**: Slate (#0F172A)
- **Text**: White/Slate (#E2E8F0)

### Typography
- **Headlines**: Bold, large sizes (5xl-7xl)
- **Body**: Regular, readable sizes (base-xl)
- **Code**: Monospace font (Monaco, Menlo)

### Components
- **Buttons**: Primary, Secondary, Outline variants
- **Cards**: Feature, Stat, Testimonial cards
- **Navigation**: Sticky header with responsive menu
- **Sections**: Hero, Features, CTA sections

## 📱 Responsive Design

- **Mobile-first approach**
- **Breakpoints**:
  - sm: 640px
  - md: 768px
  - lg: 1024px
  - xl: 1280px
- **Flexible layouts**
- **Touch-friendly interactions**

## 🎬 Animations

- **Fade-in animations**: Elements fade in on load
- **Staggered children**: Sequential animation of child elements
- **Scroll-triggered animations**: Animations trigger on scroll
- **Hover effects**: Interactive hover states
- **Smooth transitions**: 0.3s-0.6s transition durations

## 🔗 Integration

### API Endpoints
```
POST /api/demo       - Schedule demo
POST /api/invest     - Investment inquiry
POST /api/contact    - Contact form
GET  /api/agents     - List AI agents
```

### Third-party Services
- **Vercel**: Deployment platform
- **GitHub**: Version control
- **Analytics**: User tracking
- **Email Service**: Notifications

## 📊 Performance

- **Optimized Images**: WebP format, lazy loading
- **Code Splitting**: Route-based code splitting
- **Lazy Loading**: Component-level lazy loading
- **Minified Assets**: Production build optimization
- **CDN Delivery**: Vercel Edge Network

### Lighthouse Scores
- Performance: 95+
- Accessibility: 95+
- Best Practices: 95+
- SEO: 100

## ♿ Accessibility

- **Semantic HTML**: Proper heading hierarchy
- **ARIA Labels**: Screen reader support
- **Keyboard Navigation**: Full keyboard support
- **Color Contrast**: WCAG AA compliance
- **Focus Indicators**: Visible focus states

## 🧪 Testing

```bash
# Run tests
npm run test

# Run tests with coverage
npm run test:coverage

# E2E tests
npm run test:e2e

# Type checking
npm run type-check
```

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

### Manual Deployment
```bash
# Build
npm run build

# Start
npm start
```

## 📚 Documentation

- [Setup Guide](../docs/setup-guide.md)
- [Architecture](../docs/architecture.md)
- [CI/CD Guide](../docs/ci-cd-guide.html)
- [Contributing](../CONTRIBUTING.md)

## 🤝 Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - See [LICENSE](../LICENSE)

## 🔗 Links

- **Repository**: https://github.com/techspark-ai/techspark-platform
- **Website**: https://techspark.ai
- **Documentation**: https://techspark-ai.github.io/techspark-platform
- **Live Demo**: https://techspark-ai.vercel.app

## 📧 Support

- **Email**: support@techspark.ai
- **Discord**: https://discord.gg/techspark
- **Issues**: https://github.com/techspark-ai/techspark-platform/issues
- **Discussions**: https://github.com/techspark-ai/techspark-platform/discussions

## 🎯 Roadmap

### Q2 2026
- [ ] AI Agent Marketplace MVP
- [ ] No-Code Builder Beta
- [ ] Dashboard v1.0

### Q3 2026
- [ ] Advanced Analytics
- [ ] Custom Agent Builder
- [ ] Enterprise Features

### Q4 2026
- [ ] Mobile App
- [ ] API v2.0
- [ ] Global Expansion

---

Made with ❤️ by TechSpark AI Team

**Last Updated**: March 31, 2026
