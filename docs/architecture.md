# TechSpark AI - System Architecture

สถาปัตยกรรมระบบของ TechSpark AI Platform

---

## 🏗️ High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Browser                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Frontend (Next.js + React)                      │
│  - Landing Page                                             │
│  - Marketplace UI                                           │
│  - Chat Interface                                           │
│  - User Dashboard                                           │
└────────────────────────┬────────────────────────────────────┘
                         │ (HTTPS)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│           Backend API (Node.js/Python)                       │
│  - Authentication                                           │
│  - Agent Management                                         │
│  - Chat Processing                                          │
│  - Payment Processing                                       │
└────────────────────────┬────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   ┌─────────┐    ┌──────────┐    ┌────────────┐
   │Database │    │OpenAI API│    │Stripe API  │
   │(PostgreSQL)  │(GPT-4)   │    │(Payments)  │
   └─────────┘    └──────────┘    └────────────┘
```

---

## 📱 Frontend Architecture

### Technology Stack
- **Framework**: Next.js 15
- **UI Library**: React 19
- **Styling**: Tailwind CSS 4
- **Language**: TypeScript
- **State Management**: React Context API
- **Animations**: Framer Motion

### Directory Structure

```
frontend/
├── app/                     # Next.js App Directory
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page
│   ├── marketplace/        # Marketplace page
│   ├── developers/         # Developers page
│   ├── contact/            # Contact page
│   └── api/                # API routes
├── components/             # Reusable components
│   ├── Navbar.tsx
│   ├── Footer.tsx
│   ├── ChatInterface.tsx
│   ├── AgentCard.tsx
│   └── ...
├── lib/                    # Utility functions
│   ├── mockAgents.ts
│   ├── api.ts
│   └── utils.ts
├── styles/                 # Global styles
│   └── globals.css
└── public/                 # Static assets
```

### Component Hierarchy

```
App
├── Navbar
├── Main Content
│   ├── Hero Section
│   ├── Features
│   ├── Marketplace
│   │   ├── AgentCard
│   │   ├── AgentCard
│   │   └── ...
│   ├── Testimonials
│   └── CTA
├── ChatInterface
└── Footer
```

---

## 🔧 Backend Architecture

### Technology Stack
- **Runtime**: Node.js 18+
- **Framework**: Express.js / FastAPI
- **Language**: TypeScript / Python
- **Database**: PostgreSQL
- **Cache**: Redis
- **Authentication**: JWT

### API Endpoints

```
POST   /api/auth/register          # User registration
POST   /api/auth/login             # User login
GET    /api/agents                 # List all agents
GET    /api/agents/:id             # Get agent details
POST   /api/chat                   # Send message to agent
GET    /api/user/profile           # Get user profile
POST   /api/payments/create        # Create payment
GET    /api/analytics              # Get analytics
```

### Database Schema

```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  password_hash VARCHAR NOT NULL,
  name VARCHAR NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Agents table
CREATE TABLE agents (
  id UUID PRIMARY KEY,
  name VARCHAR NOT NULL,
  description TEXT,
  type VARCHAR NOT NULL,
  pricing DECIMAL,
  created_by UUID REFERENCES users(id),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Conversations table
CREATE TABLE conversations (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  agent_id UUID REFERENCES agents(id),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Messages table
CREATE TABLE messages (
  id UUID PRIMARY KEY,
  conversation_id UUID REFERENCES conversations(id),
  role VARCHAR NOT NULL, -- 'user' or 'assistant'
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Payments table
CREATE TABLE payments (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  amount DECIMAL NOT NULL,
  status VARCHAR NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🤖 AI Engine Architecture

### OpenAI Integration

```
User Message
    ↓
Message Processing
    ↓
Prompt Construction
    ├── System Prompt
    ├── Context
    └── User Message
    ↓
OpenAI API Call
    ↓
Response Processing
    ↓
Store in Database
    ↓
Return to User
```

### Prompt Structure

```
System Prompt:
"You are a professional [Agent Type] for [Company].
Your role is to [responsibilities].
Guidelines: [guidelines]"

Context:
{
  "company": "Company Name",
  "products": [...],
  "policies": [...]
}

User Message:
"User question here"
```

---

## 🔐 Authentication Flow

```
┌──────────────┐
│   User       │
└──────┬───────┘
       │
       ▼
┌──────────────────────────┐
│ Login/Register           │
│ (Email + Password)       │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Verify Credentials       │
│ (Backend)                │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Generate JWT Token       │
│ (Expires in 24h)         │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Store Token in Browser   │
│ (localStorage/cookie)    │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Include Token in         │
│ API Requests             │
└──────────────────────────┘
```

---

## 💳 Payment Flow

```
User Selects Plan
    ↓
Create Stripe Session
    ↓
Redirect to Stripe Checkout
    ↓
User Completes Payment
    ↓
Stripe Webhook
    ↓
Update User Subscription
    ↓
Grant Access to Features
```

---

## 📊 Data Flow

### Chat Message Flow

```
Frontend                Backend              OpenAI
   │                       │                   │
   ├─ Send Message ───────>│                   │
   │                       ├─ Construct Prompt─>
   │                       │                   │
   │                       │<─ Get Response ───┤
   │                       │                   │
   │                       ├─ Store in DB      │
   │                       │                   │
   │<─ Return Response ────┤                   │
   │                       │                   │
```

---

## 🔄 Deployment Architecture

### Development Environment

```
Local Machine
├── Frontend (npm run dev)
├── Backend (npm run dev)
└── Database (Docker)
```

### Production Environment

```
CDN (Vercel/Netlify)
    ↓
Frontend (Static + SSR)
    ↓
API Gateway
    ↓
Backend Services
    ├── API Server
    ├── Cache (Redis)
    └── Database (PostgreSQL)
    ↓
External Services
├── OpenAI API
├── Stripe API
└── Email Service
```

---

## 🔌 Integration Points

### External APIs

1. **OpenAI API**
   - Endpoint: `https://api.openai.com/v1/chat/completions`
   - Authentication: API Key
   - Rate Limit: 3,500 RPM

2. **Stripe API**
   - Endpoint: `https://api.stripe.com/v1/...`
   - Authentication: API Key
   - Webhooks: Payment events

3. **Email Service** (SendGrid/AWS SES)
   - Endpoint: Email delivery
   - Authentication: API Key

---

## 📈 Scalability Considerations

### Horizontal Scaling

```
Load Balancer
    ├── Backend Server 1
    ├── Backend Server 2
    └── Backend Server N
         ↓
    Shared Database
    Shared Cache (Redis)
```

### Caching Strategy

```
User Request
    ↓
Check Cache (Redis)
    ├─ Hit: Return cached response
    └─ Miss: Query Database
         ↓
    Update Cache
    Return Response
```

### Database Optimization

- Indexing on frequently queried columns
- Connection pooling
- Query optimization
- Read replicas for scaling reads

---

## 🔒 Security Architecture

### Layers of Security

```
1. HTTPS/TLS Encryption
2. API Authentication (JWT)
3. Rate Limiting
4. Input Validation
5. SQL Injection Prevention (Parameterized Queries)
6. XSS Protection
7. CORS Configuration
8. Environment Variables for Secrets
```

---

## 📊 Monitoring & Logging

### Application Monitoring

```
Frontend
├── Sentry (Error Tracking)
├── LogRocket (Session Replay)
└── Google Analytics (User Analytics)

Backend
├── Application Logs
├── Error Tracking (Sentry)
├── Performance Monitoring
└── Database Query Logs
```

---

## 🚀 Performance Optimization

### Frontend Optimization
- Code splitting
- Image optimization
- Lazy loading
- Caching strategies
- CDN delivery

### Backend Optimization
- Database indexing
- Query optimization
- Caching (Redis)
- API response compression
- Connection pooling

---

## 📚 Resources

- [System Design Patterns](https://refactoring.guru/design-patterns)
- [Microservices Architecture](https://microservices.io/)
- [Database Design](https://www.postgresql.org/docs/)

---

**Made with ❤️ by TechSpark AI**
