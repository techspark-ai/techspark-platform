# Contributing to TechSpark AI Platform

ขอบคุณที่สนใจที่จะ Contribute ให้กับ TechSpark AI Platform! 🎉

---

## 📋 Code of Conduct

เราเชื่อในการสร้างชุมชนที่เป็นมิตร ให้เคารพ และรวมถึงทุกคน

- ✅ เป็นมิตรและเคารพต่อสมาชิกอื่น
- ✅ ยอมรับความคิดเห็นที่แตกต่าง
- ✅ ให้ข้อเสนอแนะที่สร้างสรรค์
- ❌ ห้ามการ騷扰 การเหยียดหยาม หรือการทำร้ายต่อใจ

---

## 🚀 วิธีการ Contribute

### 1. Fork Repository

```bash
# ไปที่ GitHub และ Click "Fork" button
# หรือใช้ GitHub CLI
gh repo fork techspark-ai/techspark-platform --clone
```

### 2. สร้าง Feature Branch

```bash
cd techspark-platform
git checkout -b feature/your-feature-name
```

**ชื่อ Branch ที่ดี:**
- `feature/add-new-agent` - สำหรับ Feature ใหม่
- `fix/bug-description` - สำหรับ Bug Fix
- `docs/update-readme` - สำหรับ Documentation
- `refactor/improve-code` - สำหรับ Code Refactoring

### 3. ทำการเปลี่ยนแปลง

```bash
# Edit files
# Test your changes
# Commit with meaningful messages
git add .
git commit -m "feat: add new sales agent template"
```

**Commit Message Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat` - Feature ใหม่
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code style (formatting, semicolons, etc)
- `refactor` - Code refactoring
- `perf` - Performance improvement
- `test` - Adding tests

**ตัวอย่าง:**
```
feat(agents): add marketing agent template

- Add email campaign generation
- Add social media post creation
- Add analytics tracking

Closes #123
```

### 4. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 5. สร้าง Pull Request

- ไปที่ GitHub Repository
- Click "Compare & pull request"
- กรอกรายละเอียด PR
- Submit

**PR Description Template:**
```markdown
## Description
ระบุสิ่งที่คุณเปลี่ยนแปลง

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Related Issues
Closes #(issue number)

## Testing
ระบุวิธีการทดสอบ

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
```

---

## 🏗️ Development Setup

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

### Running Tests

```bash
# Run all tests
npm run test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

### Code Quality

```bash
# Lint code
npm run lint

# Format code
npm run format

# Type check
npm run type-check
```

---

## 📁 Project Structure

```
frontend/
├── app/                 # Next.js app directory
├── components/          # Reusable components
├── pages/              # Page components
├── styles/             # Global styles
├── lib/                # Utility functions
├── public/             # Static assets
└── package.json

agents-library/
├── sales-agent/        # Sales Agent template
├── support-agent/      # Support Agent template
├── templates/          # Base templates
└── README.md

docs/
├── setup-guide.md      # Setup documentation
├── api-reference.md    # API docs
├── architecture.md     # System architecture
└── examples/           # Code examples
```

---

## 🎯 Types of Contributions

### 🐛 Bug Reports

ถ้าคุณพบ Bug:

1. ตรวจสอบว่า Bug นี้ยังไม่มีใน Issues
2. สร้าง Issue ใหม่ด้วย:
   - ชื่อที่ชัดเจน
   - ขั้นตอนในการ Reproduce
   - Expected behavior
   - Actual behavior
   - Screenshots (ถ้ามี)

### ✨ Feature Requests

ถ้าคุณมีไอเดีย Feature ใหม่:

1. สร้าง Issue ใหม่ด้วย Label `enhancement`
2. ระบุ:
   - ปัญหาที่ Feature นี้แก้ไข
   - วิธีการใช้งาน
   - ตัวอย่าง

### 📖 Documentation

ช่วยปรับปรุง Documentation:

1. ตรวจสอบ Typos
2. ชี้แจง Instructions
3. เพิ่ม Examples
4. อัปเดต API Reference

### 🤖 AI Agents Templates

สร้าง AI Agent Template ใหม่:

1. สร้าง Folder ใน `agents-library/`
2. เพิ่ม:
   - `README.md` - อธิบาย Agent
   - `prompts.json` - Prompt templates
   - `examples.md` - Usage examples
3. Submit PR

---

## ✅ Quality Standards

### Code Style

- ใช้ TypeScript สำหรับ Type Safety
- ใช้ Prettier สำหรับ Formatting
- ใช้ ESLint สำหรับ Linting
- ตั้งชื่อตัวแปรให้ชัดเจน

### Testing

- เพิ่ม Unit Tests สำหรับ Features ใหม่
- ตรวจสอบ Edge Cases
- Coverage ต้อง ≥ 80%

### Documentation

- เพิ่ม JSDoc Comments
- อัปเดต README
- เพิ่ม Examples

---

## 🔍 Review Process

1. **Automated Checks**
   - Tests ต้อง Pass
   - Linting ต้อง Pass
   - Coverage ต้อง ≥ 80%

2. **Code Review**
   - Maintainers จะ Review Code
   - อาจขอให้ทำการเปลี่ยนแปลง
   - Approve เมื่อ OK

3. **Merge**
   - PR จะ Merge เมื่อ Approved
   - Squash commits เป็น 1 commit

---

## 📚 Resources

- [GitHub Docs](https://docs.github.com/)
- [Git Tutorial](https://git-scm.com/doc)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev/)

---

## 💬 Questions?

- 📧 Email: support@techspark.ai
- 💬 Discord: [Join Community](https://discord.gg/techspark)
- 🐛 Issues: [GitHub Issues](https://github.com/techspark-ai/techspark-platform/issues)

---

## 🎉 Thank You!

ขอบคุณที่ Contribute ให้กับ TechSpark AI Platform! 

**Your contributions make TechSpark AI better for everyone! 🚀**

---

**Happy Contributing! 💻**
