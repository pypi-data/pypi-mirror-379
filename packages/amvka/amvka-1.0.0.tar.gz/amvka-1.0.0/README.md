# 🎯 Amvka - AI Command Assistant

[![PyPI version](https://badge.fury.io/py/amvka.svg)](https://badge.fury.io/py/amvka)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/amvka)](https://pepy.tech/project/amvka)

> **🚀 No more memorizing commands! Just tell me what you want to do.**

Amvka is an intelligent AI-powered command-line assistant that converts natural language into shell commands. Simply describe what you want to do in plain English, and Amvka will suggest the exact command for you.

## 🚀 Quick Start

```bash
# Install amvka
pip install amvka

# Configure your API key
amvka config

# Start using natural language!
amvka "show me all Python files"
amvka "check system memory usage" 
amvka "create a backup of this directory"
```

## ✨ Features

- 🤖 **AI-Powered**: Uses Google Gemini or OpenAI to understand natural language
- 🔒 **Safety First**: Built-in safety checks and confirmation prompts
- ⚡ **Easy Setup**: Simple configuration process
- 🎯 **Smart Suggestions**: Contextual and accurate command suggestions
- 🛡️ **Secure Execution**: Sandboxed command execution with timeout protection
- 🌍 **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Installation

#### Option 1: Install via apt-get (Recommended)

```bash
# Add the Amvka repository (setup instructions coming soon)
sudo apt-get update
sudo apt-get install amvka
```

#### Option 2: Install from source

```bash
# Clone the repository
git clone https://github.com/amvka/amvka.git
cd amvka

# Install dependencies
pip3 install -r requirements.txt

# Install the package
pip3 install .
```

### Initial Setup

After installation, you need to configure your API key:

```bash
amvka config
```

This will guide you through:
1. Choosing your AI provider (Google Gemini or OpenAI)
2. Setting up your API key
3. Configuring basic preferences

### Usage Examples

```bash
# File operations
amvka show me the files in this folder
# Suggests: ls -la

amvka create a new file called hello.txt
# Suggests: touch hello.txt

amvka find all Python files in the current directory
# Suggests: find . -name "*.py"

# System information
amvka what is my current directory
# Suggests: pwd

amvka show me system information
# Suggests: uname -a

# Git operations
amvka show me the git status
# Suggests: git status

amvka commit all changes with message "fix bug"
# Suggests: git commit -am "fix bug"

# Package management
amvka install python package requests
# Suggests: pip install requests

# Text processing
amvka count lines in all text files
# Suggests: wc -l *.txt
```

### Command Line Options

```bash
amvka [OPTIONS] QUERY

Options:
  -y, --yes        Auto-confirm command execution (skip confirmation)
  --dry-run        Show suggested command without executing
  -v, --version    Show version information
  --help           Show help message

Commands:
  config           Configure API settings
    --reset        Reset configuration
    --show         Show current configuration
```

## 🔧 Configuration

### API Providers

Amvka supports two AI providers:

#### Google Gemini (Recommended)
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Run `amvka config` and paste your key

#### OpenAI
1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign in to your OpenAI account
3. Create a new API key
4. Run `amvka config` and paste your key

### Configuration File

Your configuration is stored in `~/.amvka/config.json`:

```json
{
  "provider": "gemini",
  "api_key": "your-api-key-here",
  "model": "gemini-pro",
  "safety_confirmation": true
}
```

### Managing Configuration

```bash
# Show current configuration
amvka config --show

# Reset configuration
amvka config --reset

# Reconfigure
amvka config
```

## 🛡️ Safety Features

Amvka prioritizes safety with multiple protection layers:

### 1. Command Validation
- Whitelist of safe commands
- Pattern-based dangerous command detection
- User confirmation for unknown commands

### 2. Execution Safety
- 30-second timeout for all commands
- Sandboxed execution environment
- No direct root access

### 3. Dangerous Command Detection
Commands containing these patterns are blocked:
- `rm -rf /` (recursive deletion of root)
- `sudo rm` (elevated deletion)
- `dd if=` (disk writing operations)
- `mkfs.` (filesystem formatting)
- `shutdown`/`reboot` (system control)
- And many more...

### 4. User Confirmation
- Always asks for confirmation before execution (unless `-y` flag is used)
- Shows the exact command that will be executed
- Option to cancel at any time

## 🔍 How It Works

1. **Input**: You provide a natural language query
2. **Processing**: Amvka sends your query to the configured AI provider
3. **Generation**: The AI generates an appropriate shell command
4. **Validation**: Amvka validates the command for safety
5. **Confirmation**: You review and confirm the command
6. **Execution**: The command is executed securely

## 📝 Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/amvka/amvka.git
cd amvka

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e .[dev]
```

### Building Debian Package

```bash
# Install build dependencies
sudo apt-get install build-essential debhelper dh-python python3-setuptools

# Build the package
dpkg-buildpackage -us -uc

# Install the built package
sudo dpkg -i ../amvka_1.0.0-1_all.deb
```

### Running Tests

```bash
# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=amvka tests/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Areas for Contribution
- Additional AI provider support
- Enhanced safety checks
- More comprehensive command validation
- Better error handling
- Documentation improvements

## 📋 Requirements

- Python 3.7 or higher
- Internet connection (for AI API calls)
- Linux or macOS (Windows support coming soon)

### Python Dependencies
- `requests>=2.31.0`
- `google-generativeai>=0.3.0` (for Gemini)
- `openai>=1.0.0` (for OpenAI)
- `click>=8.0.0`
- `colorama>=0.4.0`

## ⚠️ Important Disclaimers

### Safety Notice
- **Always review commands before execution**
- Amvka is designed to be safe, but AI can make mistakes
- Never run commands you don't understand
- Be extra cautious with file operations and system commands

### API Usage
- You are responsible for your API usage and costs
- Monitor your API usage on your provider's dashboard
- Keep your API keys secure and never share them

### Limitations
- Requires internet connection for AI processing
- Subject to AI provider rate limits
- Command suggestions may not always be optimal
- Some complex operations may require manual command crafting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/amvka/amvka/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/amvka/amvka/discussions)
- 📖 **Documentation**: [GitHub Wiki](https://github.com/amvka/amvka/wiki)

## 🎯 Roadmap

- [ ] Windows support
- [ ] Plugin system for custom commands
- [ ] Command history and favorites
- [ ] Integration with more AI providers
- [ ] GUI version
- [ ] Shell completion support
- [ ] Command explanation mode

---

**Made with ❤️ by the Amvka Team**

*Amvka - Making the command line more accessible, one natural language query at a time.*