# GitHub Copilot Commands Demo for PyCharm

This repository demonstrates how to configure and use GitHub Copilot commands in PyCharm to expedite your IDE development process.

> **🚀 New to GitHub Copilot?** Check out the [Quick Start Guide](QUICKSTART.md) to get up and running in 5 minutes!

## Table of Contents
- [Prerequisites](#prerequisites)
- [PyCharm Setup](#pycharm-setup)
- [GitHub Copilot Configuration](#github-copilot-configuration)
- [Essential Copilot Commands](#essential-copilot-commands)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Usage Examples](#usage-examples)
- [Best Practices](#best-practices)

## Prerequisites

1. **PyCharm Professional or Community Edition** (2021.2 or later)
2. **GitHub Copilot Subscription** - Individual, Business, or Enterprise
3. **Python 3.7+** installed on your system

## PyCharm Setup

### 1. Install GitHub Copilot Plugin

1. Open PyCharm
2. Go to `File` → `Settings` (Windows/Linux) or `PyCharm` → `Preferences` (macOS)
3. Navigate to `Plugins`
4. Search for "GitHub Copilot"
5. Click `Install`
6. Restart PyCharm when prompted

### 2. Sign in to GitHub Copilot

1. After restart, you'll see a GitHub Copilot icon in the status bar
2. Click the icon and select `Sign in to GitHub`
3. Authorize PyCharm to access your GitHub account
4. Complete the authentication flow in your browser

### 3. Verify Installation

- Look for the GitHub Copilot icon in the bottom right status bar
- Icon should show "Ready" status when active

## GitHub Copilot Configuration

### Settings Configuration

Navigate to `Settings` → `Tools` → `GitHub Copilot`:

```
☑ Enable GitHub Copilot
☑ Show completions automatically
☐ Enable Copilot for [specific languages]
```

### Customize Behavior

- **Inline Completion Delay**: Adjust how quickly suggestions appear (default: 300ms)
- **Languages**: Enable/disable for specific languages
- **Excluded Files**: Add patterns for files where Copilot should be disabled

## Essential Copilot Commands

### 1. Inline Code Suggestions
- **Accept Suggestion**: `Tab`
- **Reject Suggestion**: `Esc`
- **Next Suggestion**: `Alt + ]` (Windows/Linux) or `Option + ]` (macOS)
- **Previous Suggestion**: `Alt + [` (Windows/Linux) or `Option + [` (macOS)

### 2. Copilot Chat Commands

Open Copilot Chat: `Ctrl + Shift + A` → Type "GitHub Copilot Chat"

Common chat commands:
```
/explain - Explain selected code
/tests - Generate unit tests
/fix - Suggest fixes for problems
/doc - Generate documentation
/simplify - Simplify complex code
```

### 3. Context-Aware Features

- **Function Generation**: Write a function signature with a descriptive name and comments
- **Test Generation**: Use `/tests` command or write test function names
- **Code Refactoring**: Highlight code and ask Copilot to refactor
- **Documentation**: Type `"""` for docstrings and let Copilot complete

## Keyboard Shortcuts

### Default PyCharm + Copilot Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Accept Inline Suggestion | `Tab` | `Tab` |
| Dismiss Suggestion | `Esc` | `Esc` |
| Next Suggestion | `Alt + ]` | `Option + ]` |
| Previous Suggestion | `Alt + [` | `Option + [` |
| Open Copilot Chat | `Ctrl + Shift + A` then search | `Cmd + Shift + A` then search |
| Trigger Suggestion | `Alt + \` | `Option + \` |

### Custom Keymap Configuration

1. Go to `Settings` → `Keymap`
2. Search for "GitHub Copilot"
3. Right-click on any action to assign a custom shortcut

## Usage Examples

### Example 1: Function Generation

```python
# Type a descriptive comment
# Function to calculate fibonacci sequence up to n terms

# Copilot will suggest:
def fibonacci(n):
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
```

### Example 2: Test Generation

```python
# Use /tests command in Copilot Chat or:
# test_fibonacci function

# Copilot suggests:
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), [])
    
    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), [0])
    
    def test_fibonacci_five(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
```

### Example 3: API Client Generation

```python
# Class to handle REST API calls to JSONPlaceholder

# Copilot will generate complete API client class
```

See the `examples/` directory for more detailed examples.

## Best Practices

### 1. Write Clear Comments
- Descriptive comments help Copilot understand intent
- Use natural language to describe what you want

### 2. Provide Context
- Keep related code in the same file for better suggestions
- Use meaningful variable and function names

### 3. Review Suggestions
- Always review Copilot suggestions before accepting
- Verify logic, security, and performance implications

### 4. Iterative Refinement
- Accept partial suggestions and refine with comments
- Use chat commands for complex refactoring

### 5. Security Considerations
- Review generated code for security vulnerabilities
- Don't commit sensitive data in comments
- Validate input handling and authentication logic

### 6. Testing
- Use `/tests` command to generate comprehensive tests
- Review and adjust test coverage
- Ensure tests are meaningful and not just boilerplate

## Project Structure

```
github-copilot-command-demo/
├── README.md                      # This file
├── .gitignore                     # Python/PyCharm gitignore
├── examples/                      # Example use cases
│   ├── basic_examples.py         # Basic Copilot usage
│   ├── api_client.py             # REST API client example
│   ├── data_processing.py        # Data processing examples
│   └── test_examples.py          # Generated tests examples
├── docs/                          # Additional documentation
│   └── advanced_tips.md          # Advanced Copilot tips
└── .idea/                         # PyCharm configuration (optional)
```

## Troubleshooting

### Copilot Not Working
1. Check status bar icon - should show "Ready"
2. Verify GitHub Copilot subscription is active
3. Try signing out and back in
4. Check if file type is enabled in settings

### No Suggestions Appearing
1. Ensure `Show completions automatically` is enabled
2. Check if file is not in excluded patterns
3. Try triggering manually with `Alt + \` / `Option + \`

### Poor Quality Suggestions
1. Provide more context in comments
2. Use more descriptive names
3. Keep related code nearby
4. Try rephrasing your comments

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [PyCharm Documentation](https://www.jetbrains.com/help/pycharm/)
- [GitHub Copilot in PyCharm Guide](https://www.jetbrains.com/help/pycharm/github-copilot.html)

## Contributing

Feel free to contribute additional examples or tips! Create a pull request with your improvements.

## License

MIT License - Feel free to use this demo for learning and reference.