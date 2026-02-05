# Contributing to GitHub Copilot Command Demo

Thank you for your interest in contributing! This repository is designed to showcase advanced GitHub Copilot techniques for AI-augmented development.

## 🎯 What We're Looking For

We welcome contributions that demonstrate:
- **Novel use cases** for GitHub Copilot
- **Advanced techniques** beyond basic autocomplete
- **Production-ready patterns** that solve real problems
- **Clear demonstrations** suitable for 1-10 minute demos
- **Measurable impact** (time savings, quality improvements, etc.)

## 📝 How to Contribute

### Adding a New Example

Each example should follow this structure:

```
examples/your-example-name/
├── instruction.md    # Detailed examples with prompts and outputs
└── command.md        # Copilot commands and workflows
```

#### instruction.md Template

```markdown
# [Example Name] - Instructions

## Overview
Brief description of what this example demonstrates (1-2 sentences).

## GitHub Copilot Instructions

### Instruction 1: [Specific Use Case]

**Prompt:**
```
[The exact prompt to give to GitHub Copilot]
```

**[Before/Input Code if applicable]:**
```[language]
[Code example]
```

**Expected Output:**
```[language]
[Generated code with comments explaining key parts]
```

**[Explanation of what changed and why it's valuable]**

[Repeat for 3-5 instructions]

## Tips for Using GitHub Copilot
[Best practices specific to this example]

## Advanced Use Cases
[More complex scenarios]
```

#### command.md Template

```markdown
# [Example Name] - Commands

## Overview
Brief description of slash commands and workflows.

## Slash Commands

### /[command] - [Purpose]

**Usage:**
```
[Exact command syntax]
```

**Expected Output:**
```[language]
[Example output]
```

## Demo Workflow (X minutes)

### Step 1: [Action] (time)
[Detailed steps]

[Repeat for demo flow]

## Advanced Techniques
[Complex workflows and combinations]
```

### Example Ideas We'd Love to See

- **Infrastructure as Code:** Convert Docker Compose to Kubernetes manifests
- **Database Migrations:** Generate migrations from schema changes
- **GraphQL to REST:** Convert GraphQL queries to REST endpoints
- **Legacy Code Modernization:** Upgrade old patterns to modern equivalents
- **Accessibility Improvements:** Add ARIA labels and semantic HTML
- **Internationalization:** Generate translation files and i18n setup
- **CI/CD Pipeline Generation:** Create GitHub Actions/GitLab CI configs
- **Microservices Scaffolding:** Generate service boilerplate
- **Error Handling Patterns:** Add comprehensive error handling
- **Logging and Monitoring:** Add observability to code

## 🎨 Style Guidelines

### Writing Style
- **Be concise:** Get to the point quickly
- **Be specific:** Include exact commands and expected outputs
- **Be practical:** Focus on real-world use cases
- **Be measurable:** Include metrics when possible (time saved, speedup, etc.)

### Code Examples
- **Use realistic examples:** Not "foo/bar" but actual use cases
- **Include context:** Show enough code to understand the problem
- **Add comments:** Explain non-obvious parts
- **Follow best practices:** Generated code should be production-quality

### Documentation
- **Clear headings:** Use markdown hierarchy properly
- **Code blocks:** Always specify language for syntax highlighting
- **Examples:** Show both before and after when applicable
- **Metrics:** Include performance numbers, time savings, etc.

## ✅ Checklist Before Submitting

- [ ] Tested the example with GitHub Copilot
- [ ] Verified all commands work as documented
- [ ] Included both instruction.md and command.md
- [ ] Added entry to main README.md
- [ ] Included realistic, production-ready examples
- [ ] Added metrics or measurable improvements
- [ ] Followed the directory structure
- [ ] Used proper markdown formatting
- [ ] Spell-checked documentation
- [ ] Code examples are well-formatted

## 🚀 Submission Process

1. **Fork the repository**
2. **Create a branch:** `git checkout -b feature/your-example-name`
3. **Add your example** following the structure above
4. **Update README.md** to include your example in the overview
5. **Test everything** to ensure it works
6. **Commit your changes:** `git commit -m "Add [example name] demo"`
7. **Push to your fork:** `git push origin feature/your-example-name`
8. **Open a Pull Request** with:
   - Clear title: "Add [Example Name] Demo"
   - Description of what the example demonstrates
   - Why it's valuable for demos
   - Any special setup required

## 📋 PR Review Criteria

We'll review PRs based on:

### Quality
- [ ] Example is clear and well-documented
- [ ] Code follows best practices
- [ ] Commands work as described
- [ ] Suitable for live demo

### Completeness
- [ ] Both instruction.md and command.md included
- [ ] Multiple examples/instructions provided
- [ ] Tips and best practices included
- [ ] Demo workflow documented

### Impact
- [ ] Demonstrates advanced Copilot usage
- [ ] Solves real-world problem
- [ ] Shows measurable improvement
- [ ] Unique contribution (not duplicate)

### Documentation
- [ ] Clear and concise writing
- [ ] Proper markdown formatting
- [ ] Code examples well-formatted
- [ ] README.md updated

## 🎓 Tips for Great Contributions

### Do's ✅
- **Test thoroughly:** Make sure everything works
- **Be specific:** Exact prompts and commands
- **Show impact:** Include metrics and comparisons
- **Keep it real:** Use realistic, practical examples
- **Add context:** Explain why this matters

### Don'ts ❌
- **Don't submit untested examples**
- **Don't use trivial "hello world" examples**
- **Don't forget to update README.md**
- **Don't include deprecated patterns**
- **Don't skip documentation**

## 🐛 Reporting Issues

Found a problem with an existing example?

1. **Check if it's already reported** in Issues
2. **Open a new issue** with:
   - Which example has the problem
   - What you expected vs. what happened
   - Steps to reproduce
   - Your environment (VS Code version, Copilot version)

## 💬 Questions?

- Open a discussion in GitHub Discussions
- Tag existing contributors for feedback
- Ask in Issues if you're unsure about a contribution

## 📜 Code of Conduct

- Be respectful and professional
- Focus on constructive feedback
- Help others learn
- Celebrate contributions

## 🏆 Recognition

Contributors will be:
- Listed in README.md acknowledgments
- Credited in their example's documentation
- Mentioned in release notes

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this project (MIT License).

---

Thank you for helping make this the best resource for GitHub Copilot mastery! 🚀

## Example Contribution

Want to see what a good contribution looks like? Check out:
- `examples/sql-to-elasticsearch/` - Comprehensive with multiple examples
- `examples/security-scanner/` - Practical real-world use cases
- `examples/performance-optimization/` - Includes metrics and benchmarks

These can serve as templates for your contributions!
