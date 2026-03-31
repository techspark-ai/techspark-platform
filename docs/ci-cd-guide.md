# CI/CD Pipeline Guide

คู่มือการใช้งาน GitHub Actions CI/CD Pipeline สำหรับ TechSpark Platform

---

## 📚 Table of Contents

1. [Overview](#overview)
2. [Workflows](#workflows)
3. [Setup Instructions](#setup-instructions)
4. [Environment Variables](#environment-variables)
5. [Secrets Management](#secrets-management)
6. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

TechSpark Platform ใช้ GitHub Actions สำหรับ Continuous Integration/Continuous Deployment (CI/CD)

### ✨ Features

- ✅ Automated Testing
- ✅ Code Quality Checks
- ✅ Security Scanning
- ✅ Automated Deployment
- ✅ Release Management
- ✅ Documentation Publishing

### 🔄 Pipeline Flow

```
Push Code
    ↓
├─ Lint & Test
│  ├─ ESLint
│  ├─ TypeScript Check
│  ├─ Unit Tests
│  └─ Build
├─ Code Quality
│  ├─ SonarQube
│  ├─ Dependency Check
│  └─ License Check
├─ Security
│  ├─ Vulnerability Scan
│  └─ SBOM Generation
└─ Deploy (if main branch)
   ├─ Build Frontend
   ├─ Deploy to Vercel
   └─ Create Release
```

---

## 🔄 Workflows

### 1. Lint & Test (`lint-and-test.yml`)

**Trigger**: Push to main/develop, Pull Request

**Jobs**:
- **lint**: ESLint, TypeScript, Prettier
- **test**: Unit tests, Coverage
- **build**: Build artifacts
- **security**: Vulnerability scanning
- **documentation**: Documentation validation

**Status Badge**:
```markdown
![Lint & Test](https://github.com/techspark-ai/techspark-platform/workflows/Lint%20&%20Test/badge.svg)
```

### 2. Deploy (`deploy.yml`)

**Trigger**: Push to main, Manual trigger

**Jobs**:
- Build Frontend
- Deploy to Vercel
- Create GitHub Release
- Notify Slack

**Environment Variables**:
```
NEXT_PUBLIC_API_URL
NEXT_PUBLIC_OPENAI_API_KEY
```

### 3. Code Quality (`code-quality.yml`)

**Trigger**: Push to main/develop, Pull Request

**Jobs**:
- SonarQube Analysis
- Dependency Check
- License Verification
- Performance Analysis
- Accessibility Check

### 4. Release (`release.yml`)

**Trigger**: Push tag (v*), Manual trigger

**Jobs**:
- Create Release Notes
- Publish Release
- Update CHANGELOG
- Deploy Documentation
- Announce Release

### 5. PR Checks (`pr-checks.yml`)

**Trigger**: Pull Request

**Jobs**:
- PR Title Validation
- PR Description Check
- File Changes Check
- Commit Lint
- Dependency Check
- Code Review Hints

---

## 🚀 Setup Instructions

### Step 1: Enable GitHub Actions

1. Go to Repository Settings
2. Click "Actions" → "General"
3. Enable "Allow all actions and reusable workflows"

### Step 2: Configure Secrets

Add the following secrets to GitHub:

```
Settings → Secrets and variables → Actions
```

**Required Secrets**:
```
VERCEL_TOKEN          # Vercel deployment token
VERCEL_ORG_ID         # Vercel organization ID
VERCEL_PROJECT_ID     # Vercel project ID
SLACK_WEBHOOK         # Slack webhook URL (optional)
SONAR_TOKEN           # SonarQube token (optional)
```

**Environment Variables**:
```
NEXT_PUBLIC_API_URL
NEXT_PUBLIC_OPENAI_API_KEY
```

### Step 3: Configure Branch Protection

1. Go to Repository Settings
2. Click "Branches"
3. Add rule for "main":
   - ✅ Require status checks to pass
   - ✅ Require branches to be up to date
   - ✅ Dismiss stale reviews

---

## 🔐 Secrets Management

### Adding Secrets

```bash
# Using GitHub CLI
gh secret set SECRET_NAME --body "secret_value"

# Or via GitHub UI
Settings → Secrets and variables → Actions → New repository secret
```

### Using Secrets in Workflows

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

### Secret Best Practices

- ✅ Never commit secrets
- ✅ Use GitHub Secrets
- ✅ Rotate secrets regularly
- ✅ Use minimal permissions
- ✅ Audit secret access

---

## 📊 Workflow Status

### View Workflow Status

1. Go to Repository
2. Click "Actions" tab
3. View workflow runs

### Status Badges

Add to README:

```markdown
![Lint & Test](https://github.com/techspark-ai/techspark-platform/workflows/Lint%20&%20Test/badge.svg)
![Deploy](https://github.com/techspark-ai/techspark-platform/workflows/Deploy/badge.svg)
![Code Quality](https://github.com/techspark-ai/techspark-platform/workflows/Code%20Quality/badge.svg)
```

---

## 🔍 Monitoring

### GitHub Actions Dashboard

- View all workflow runs
- Check job status
- Review logs
- Download artifacts

### Notifications

- Email notifications (default)
- Slack notifications (optional)
- Custom webhooks

---

## 🐛 Troubleshooting

### Common Issues

#### 1. Build Fails

```bash
# Check logs
# Go to Actions → Failed workflow → View logs

# Common causes:
- Missing dependencies
- Environment variables not set
- Node version mismatch
```

#### 2. Deployment Fails

```bash
# Check Vercel logs
# Verify secrets are set correctly
# Check branch protection rules
```

#### 3. Tests Fail

```bash
# Run tests locally
npm run test

# Check test configuration
# Review test output in GitHub Actions
```

### Debug Mode

Enable debug logging:

```yaml
env:
  ACTIONS_STEP_DEBUG: true
```

---

## 📈 Performance Optimization

### Caching

```yaml
- uses: actions/setup-node@v4
  with:
    cache: 'npm'
```

### Parallel Jobs

```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
  job2:
    runs-on: ubuntu-latest
```

### Conditional Steps

```yaml
- if: github.ref == 'refs/heads/main'
  run: npm run deploy
```

---

## 🔄 Updating Workflows

### Modify Workflow

1. Edit `.github/workflows/*.yml`
2. Commit and push
3. Changes take effect immediately

### Best Practices

- ✅ Test changes in feature branch
- ✅ Use workflow syntax validation
- ✅ Document changes
- ✅ Keep workflows simple
- ✅ Use reusable workflows

---

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Actions Marketplace](https://github.com/marketplace?type=actions)

---

## 🎯 Next Steps

1. **Setup Secrets**: Add required secrets to GitHub
2. **Configure Branch Protection**: Protect main branch
3. **Monitor Workflows**: Check Actions tab
4. **Optimize Performance**: Add caching and parallel jobs
5. **Integrate Notifications**: Setup Slack/email

---

## 📞 Support

- 📧 Email: support@techspark.ai
- 💬 Discord: [Join Community](https://discord.gg/techspark)
- 🐛 Issues: [GitHub Issues](https://github.com/techspark-ai/techspark-platform/issues)

---

**Happy Automating! 🚀**
