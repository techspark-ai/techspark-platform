import { Button } from "@/components/ui/button";
import { ArrowRight, TrendingUp, Zap, Users, BarChart3, Shield, Rocket } from "lucide-react";
import { motion } from "framer-motion";

/**
 * TechSpark AI - Investor Landing Page
 * Professional landing page designed to attract and convert investors
 * Focus: Clear value proposition, market opportunity, business model, and competitive advantage
 */

export default function Home() {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: { staggerChildren: 0.1, delayChildren: 0.2 },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.6 } },
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900" style={{
      backgroundImage: 'url(https://d2xsxph8kpxj0f.cloudfront.net/310519663496874200/ZDN9K2guyK2RqsP2Budb3V/techspark-hero-bg-YpdDq8dXu8YwEfahX2BnTx.webp)',
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundAttachment: 'fixed'
    }}>
      {/* Navigation */}
      <nav className="sticky top-0 z-40 backdrop-blur-md bg-slate-900/80 border-b border-slate-700/50">
        <div className="container flex items-center justify-between py-4">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-br from-cyan-400 to-blue-600 rounded-lg flex items-center justify-center">
              <Rocket className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold text-white">TechSpark AI</span>
          </div>
          <div className="hidden md:flex items-center gap-8">
            <a href="#opportunity" className="text-slate-300 hover:text-white transition-colors text-sm">
              Market Opportunity
            </a>
            <a href="#features" className="text-slate-300 hover:text-white transition-colors text-sm">
              Features
            </a>
            <a href="#model" className="text-slate-300 hover:text-white transition-colors text-sm">
              Business Model
            </a>
            <Button variant="default" size="sm" className="bg-cyan-500 hover:bg-cyan-600">
              Schedule Demo
            </Button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="container py-20 md:py-32 relative z-10">
        <motion.div
          className="max-w-4xl"
          variants={containerVariants}
          initial="hidden"
          animate="visible"
        >
          <motion.div variants={itemVariants} className="mb-6 inline-flex items-center gap-2 px-4 py-2 rounded-full bg-cyan-500/10 border border-cyan-500/30">
            <Zap className="w-4 h-4 text-cyan-400" />
            <span className="text-sm text-cyan-300 font-medium">The Operating System of AI Workforce</span>
          </motion.div>

          <motion.h1
            variants={itemVariants}
            className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight"
          >
            Every Business Deserves <span className="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">AI Employees</span>
          </motion.h1>

          <motion.p
            variants={itemVariants}
            className="text-xl text-slate-300 mb-8 max-w-2xl leading-relaxed"
          >
            TechSpark AI is the App Store for AI Agents. We empower SMEs to hire, deploy, and manage AI agents in 5 minutes—no coding required. We're building the future of work.
          </motion.p>

          <motion.div variants={itemVariants} className="flex flex-col sm:flex-row gap-4">
            <Button size="lg" className="bg-cyan-500 hover:bg-cyan-600 text-white font-semibold">
              Invest Now <ArrowRight className="ml-2 w-5 h-5" />
            </Button>
            <Button size="lg" variant="outline" className="border-slate-600 text-white hover:bg-slate-800">
              View Pitch Deck
            </Button>
          </motion.div>

          <motion.div variants={itemVariants} className="mt-12 grid grid-cols-3 gap-8 pt-12 border-t border-slate-700/50">
            <div>
              <div className="text-3xl font-bold text-cyan-400 mb-2">$10B+</div>
              <p className="text-slate-400 text-sm">TAM in Southeast Asia</p>
            </div>
            <div>
              <div className="text-3xl font-bold text-cyan-400 mb-2">3-5x</div>
              <p className="text-slate-400 text-sm">ROI for SME customers</p>
            </div>
            <div>
              <div className="text-3xl font-bold text-cyan-400 mb-2">20-30%</div>
              <p className="text-slate-400 text-sm">Commission from developers</p>
            </div>
          </motion.div>
        </motion.div>
      </section>

      {/* Market Opportunity Section */}
      <section id="opportunity" className="container py-20 md:py-32 relative z-10 bg-gradient-to-b from-slate-900/95 to-slate-800/95 rounded-3xl my-12 px-8 md:px-12 py-16">
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          className="max-w-4xl"
        >
          <motion.div variants={itemVariants} className="mb-12">
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Massive Market Opportunity
            </h2>
            <p className="text-xl text-slate-300 leading-relaxed">
              SMEs across Southeast Asia struggle with operational costs and lack technical expertise. TechSpark AI solves this by providing ready-made AI solutions that reduce costs by 40-60% while improving efficiency.
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 gap-8">
            <motion.div
              variants={itemVariants}
              className="bg-gradient-to-br from-slate-800 to-slate-700/50 border border-slate-600/50 rounded-2xl p-8"
            >
              <Users className="w-12 h-12 text-cyan-400 mb-4" />
              <h3 className="text-2xl font-bold text-white mb-3">Target Market</h3>
              <p className="text-slate-300 leading-relaxed">
                <strong>SME Businesses:</strong> 5M+ SMEs in Thailand, Indonesia, Vietnam, Philippines seeking cost-effective AI solutions without technical overhead.
              </p>
            </motion.div>

            <motion.div
              variants={itemVariants}
              className="bg-gradient-to-br from-slate-800 to-slate-700/50 border border-slate-600/50 rounded-2xl p-8"
            >
              <TrendingUp className="w-12 h-12 text-cyan-400 mb-4" />
              <h3 className="text-2xl font-bold text-white mb-3">Growth Drivers</h3>
              <p className="text-slate-300 leading-relaxed">
                <strong>AI Adoption:</strong> 87% of businesses plan AI investments. TechSpark AI captures this demand with a no-code, low-risk entry point.
              </p>
            </motion.div>
          </div>
        </motion.div>
      </section>

      {/* Features Section */}
      <section id="features" className="container py-20 md:py-32 relative z-10">
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
        >
          <motion.div variants={itemVariants} className="mb-12 text-center">
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Three Pillars of TechSpark AI
            </h2>
            <p className="text-xl text-slate-300 max-w-2xl mx-auto">
              We combine the best of App Store, Zapier, and AI Employees into one platform
            </p>
          </motion.div>

          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: Rocket,
                title: "AI Agent Marketplace",
                description: "Browse, install, and deploy AI agents in seconds. Sales AI, Support AI, Marketing AI—all ready to use.",
                color: "from-cyan-500 to-blue-500",
              },
              {
                icon: Zap,
                title: "No-Code AI Builder",
                description: "Create custom AI agents with drag-and-drop workflows. No coding skills required. Deploy instantly.",
                color: "from-blue-500 to-purple-500",
              },
              {
                icon: BarChart3,
                title: "AI Workforce Dashboard",
                description: "Monitor performance, track ROI, and manage all your AI agents from one unified control center.",
                color: "from-purple-500 to-pink-500",
              },
            ].map((feature, idx) => (
              <motion.div
                key={idx}
                variants={itemVariants}
                className="bg-gradient-to-br from-slate-800 to-slate-700/50 border border-slate-600/50 rounded-2xl p-8 hover:border-slate-500/80 transition-all duration-300"
              >
                <div className={`w-14 h-14 rounded-xl bg-gradient-to-br ${feature.color} flex items-center justify-center mb-6`}>
                  <feature.icon className="w-7 h-7 text-white" />
                </div>
                <h3 className="text-2xl font-bold text-white mb-3">{feature.title}</h3>
                <p className="text-slate-300 leading-relaxed">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* Business Model Section */}
      <section id="model" className="container py-20 md:py-32 relative z-10 bg-gradient-to-b from-slate-900/95 to-slate-800/95 rounded-3xl my-12 px-8 md:px-12 py-16">
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          className="max-w-4xl"
        >
          <motion.div variants={itemVariants} className="mb-12">
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Multiple Revenue Streams
            </h2>
            <p className="text-xl text-slate-300 leading-relaxed">
              TechSpark AI generates revenue from multiple sources, creating a resilient and scalable business model.
            </p>
          </motion.div>

          <div className="space-y-6">
            {[
              {
                title: "Commission from Marketplace",
                description: "20-30% commission on every AI agent sold in our marketplace",
                value: "20-30%",
              },
              {
                title: "Subscription Plans",
                description: "Monthly/yearly subscriptions (Free, Pro, Enterprise) based on usage",
                value: "Recurring",
              },
              {
                title: "Usage-Based Pricing",
                description: "Charges for API calls, tokens, and automation runs",
                value: "Variable",
              },
              {
                title: "Custom AI Solutions",
                description: "Premium service for building bespoke AI agents for enterprises",
                value: "10K-100K+",
              },
            ].map((item, idx) => (
              <motion.div
                key={idx}
                variants={itemVariants}
                className="bg-gradient-to-r from-slate-800/50 to-slate-700/30 border border-slate-600/50 rounded-xl p-6 flex items-center justify-between hover:border-slate-500/80 transition-all"
              >
                <div>
                  <h3 className="text-lg font-semibold text-white mb-2">{item.title}</h3>
                  <p className="text-slate-400">{item.description}</p>
                </div>
                <div className="text-right">
                  <div className="text-2xl font-bold text-cyan-400">{item.value}</div>
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* Competitive Advantage Section */}
      <section className="container py-20 md:py-32 relative z-10">
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
        >
          <motion.div variants={itemVariants} className="mb-12 text-center">
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Why TechSpark AI Wins
            </h2>
            <p className="text-xl text-slate-300 max-w-2xl mx-auto">
              We're not just another AI tool. We're the complete ecosystem for AI workforce adoption.
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 gap-8">
            {[
              {
                icon: Shield,
                title: "First-Mover Advantage",
                description: "First AI Agent Marketplace in Southeast Asia tailored for SMEs",
              },
              {
                icon: Users,
                title: "Developer Ecosystem",
                description: "Revenue sharing model attracts top AI builders and creates network effects",
              },
              {
                icon: Zap,
                title: "No-Code Accessibility",
                description: "Democratizes AI creation—anyone can build and deploy agents",
              },
              {
                icon: TrendingUp,
                title: "Proven Market Fit",
                description: "Solving real pain points: cost reduction, efficiency, ease of use",
              },
            ].map((item, idx) => (
              <motion.div
                key={idx}
                variants={itemVariants}
                className="flex gap-4"
              >
                <div className="flex-shrink-0">
                  <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-cyan-500/20 to-blue-500/20 border border-cyan-500/30 flex items-center justify-center">
                    <item.icon className="w-6 h-6 text-cyan-400" />
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-semibold text-white mb-2">{item.title}</h3>
                  <p className="text-slate-400">{item.description}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* CTA Section */}
      <section className="container py-20 md:py-32 relative z-10">
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          className="bg-gradient-to-r from-cyan-600/20 to-blue-600/20 border border-cyan-500/30 rounded-3xl p-12 md:p-16 text-center"
        >
          <motion.h2 variants={itemVariants} className="text-4xl md:text-5xl font-bold text-white mb-6">
            Ready to Invest in the Future of Work?
          </motion.h2>
          <motion.p variants={itemVariants} className="text-xl text-slate-300 mb-8 max-w-2xl mx-auto">
            Join us in building the Operating System for AI Workforce. Let's transform how businesses operate.
          </motion.p>
          <motion.div variants={itemVariants} className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="bg-cyan-500 hover:bg-cyan-600 text-white font-semibold">
              Schedule Investor Call <ArrowRight className="ml-2 w-5 h-5" />
            </Button>
            <Button size="lg" variant="outline" className="border-slate-500 text-white hover:bg-slate-800">
              Download Pitch Deck
            </Button>
          </motion.div>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-700/50 mt-20 relative z-10 bg-slate-900/95 backdrop-blur-md">
        <div className="container py-12">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <div className="w-6 h-6 bg-gradient-to-br from-cyan-400 to-blue-600 rounded-lg flex items-center justify-center">
                  <Rocket className="w-4 h-4 text-white" />
                </div>
                <span className="font-bold text-white">TechSpark AI</span>
              </div>
              <p className="text-slate-400 text-sm">The Operating System of AI Workforce</p>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Product</h4>
              <ul className="space-y-2 text-sm text-slate-400">
                <li><a href="#" className="hover:text-white transition-colors">Marketplace</a></li>
                <li><a href="#" className="hover:text-white transition-colors">AI Builder</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Dashboard</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Company</h4>
              <ul className="space-y-2 text-sm text-slate-400">
                <li><a href="#" className="hover:text-white transition-colors">About</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Blog</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Legal</h4>
              <ul className="space-y-2 text-sm text-slate-400">
                <li><a href="#" className="hover:text-white transition-colors">Privacy</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Terms</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-700/50 pt-8 text-center text-slate-400 text-sm">
            <p>&copy; 2026 TechSpark AI. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
