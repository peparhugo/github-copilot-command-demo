# Quick Start Guide

Get started with GitHub Copilot in PyCharm in 5 minutes!

## 1. Install GitHub Copilot Plugin (2 minutes)

1. Open PyCharm
2. Press `Ctrl+Alt+S` (Windows/Linux) or `Cmd+,` (macOS) to open Settings
3. Go to `Plugins` → `Marketplace`
4. Search for **"GitHub Copilot"**
5. Click `Install` and restart PyCharm

## 2. Sign In to GitHub (1 minute)

1. After restart, look for the GitHub Copilot icon in the bottom status bar
2. Click it and select **"Sign in to GitHub"**
3. Follow the browser authentication flow
4. Return to PyCharm - icon should show "Ready"

## 3. Try Your First Copilot Suggestion (2 minutes)

### Example 1: Simple Function
1. Create a new Python file: `test_copilot.py`
2. Type this comment and press Enter:
   ```python
   # Function to calculate fibonacci sequence
   ```
3. Press `Tab` to accept Copilot's suggestion
4. See the magic! ✨

### Example 2: Generate Tests
1. Write a function in your file
2. Below it, type:
   ```python
   # test function for fibonacci
   ```
3. Accept the test function Copilot generates
4. Run the test!

## 4. Essential Keyboard Shortcuts

- **Accept suggestion**: `Tab`
- **Reject suggestion**: `Esc`
- **Next suggestion**: `Alt + ]` (Windows/Linux) or `Option + ]` (macOS)
- **Previous suggestion**: `Alt + [` (Windows/Linux) or `Option + [` (macOS)

## 5. Try the Examples

Run the included examples to see Copilot in action:

```bash
# Clone this repository
git clone https://github.com/peparhugo/github-copilot-command-demo.git
cd github-copilot-command-demo

# Run basic examples
python examples/basic_examples.py

# Run data processing examples
python examples/data_processing.py

# Run tests
python -m unittest examples.test_examples
```

## Next Steps

1. Read the [full README](README.md) for comprehensive setup instructions
2. Check out [Advanced Tips](docs/advanced_tips.md) for power user techniques
3. Experiment with the examples in the `examples/` directory
4. Try using Copilot in your own projects!

## Tips for Success

1. **Write clear comments** - Copilot works best with descriptive intent
2. **Use type hints** - They help Copilot understand what you need
3. **Review suggestions** - Always verify the generated code
4. **Iterate** - Accept partial suggestions and refine

## Common Issues

### "Copilot not showing suggestions"
- Check if the status bar icon shows "Ready"
- Ensure you're editing a Python file (`.py` extension)
- Try triggering manually: `Alt + \` (Windows/Linux) or `Option + \` (macOS)

### "Suggestions are low quality"
- Add more context in comments
- Include type hints
- Provide example inputs/outputs in comments

### "Copilot is disabled"
- Check your GitHub Copilot subscription is active
- Sign out and sign back in
- Check Settings → Tools → GitHub Copilot → Enable GitHub Copilot

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [PyCharm GitHub Copilot Guide](https://www.jetbrains.com/help/pycharm/github-copilot.html)
- [This Repository's Full Documentation](README.md)

---

**Ready to accelerate your Python development? Start coding with Copilot now!** 🚀
