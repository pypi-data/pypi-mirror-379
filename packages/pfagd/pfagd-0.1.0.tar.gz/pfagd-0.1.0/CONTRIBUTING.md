# Contributing to PFAGD

We're excited that you're interested in contributing to PFAGD (Python for Android Game Development)! This document will guide you through the process.

## 🚀 Quick Start for Contributors

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pfagd.git
   cd pfagd
   ```
3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .[dev]
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
5. **Make your changes** and test them
6. **Submit a pull request**

## 🛠️ Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- A code editor (VS Code, PyCharm, etc.)

### Installation for Development
```bash
# Clone the repository
git clone https://github.com/pfagd/pfagd.git
cd pfagd

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e .[dev]

# Verify installation
pfagd --version
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pfagd

# Run specific test file
pytest tests/test_engine.py

# Run tests for specific component
pytest tests/ -k "test_scene"
```

### Testing Your Changes
```bash
# Test CLI commands
pfagd scaffold test-project
cd test-project
pfagd run main.py --debug

# Test building
pfagd build-desktop main.py
```

## 📁 Project Structure

```
pfagd/
├── pfagd/                 # Main package
│   ├── engine/           # Game engine core
│   ├── ui/               # UI components
│   ├── assets/           # Asset management
│   ├── cli/              # Command-line interface
│   └── monetization/     # Monetization features
├── tests/                # Test suite
├── examples/             # Example projects
├── docs/                 # Documentation
├── setup.py              # Package configuration
└── README.md             # Project overview
```

## 🎯 Areas for Contribution

### High Priority
- **Bug fixes** - Check our [Issues](https://github.com/pfagd/pfagd/issues)
- **Documentation improvements**
- **Example games and tutorials**
- **Testing coverage expansion**
- **Performance optimizations**

### Feature Areas
- **Engine improvements** - Physics, rendering, audio
- **UI components** - New widgets, themes, layouts
- **Platform support** - iOS, web deployment
- **Build system** - Optimization, new platforms
- **Monetization** - New ad networks, payment systems

### Beginner Friendly
- **Documentation fixes** - Typos, clarity improvements
- **Example projects** - Simple games demonstrating features
- **Unit tests** - Test coverage for existing code
- **Code comments** - Improving code documentation

## 📝 Code Style

### Python Code Style
- Follow **PEP 8** style guide
- Use **type hints** where possible
- Write **docstrings** for all public functions/classes
- Maximum line length: **88 characters** (Black formatter)

### Example:
```python
def create_sprite(image_path: str, position: tuple = (0, 0)) -> Sprite:
    """Create a new sprite with the given image and position.
    
    Args:
        image_path: Path to the sprite image file
        position: Initial (x, y) position for the sprite
        
    Returns:
        Sprite: The created sprite object
        
    Raises:
        FileNotFoundError: If image_path doesn't exist
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    return Sprite(image_path, position)
```

### Formatting Tools
```bash
# Format code with Black
black pfagd/ tests/

# Sort imports
isort pfagd/ tests/

# Check style with flake8
flake8 pfagd/ tests/

# Type checking with mypy
mypy pfagd/
```

## 🐛 Bug Reports

### Before Submitting
1. **Search existing issues** to avoid duplicates
2. **Test with latest version** of PFAGD
3. **Create minimal reproduction** example

### Bug Report Template
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Environment:**
- OS: [e.g., Windows 10, Ubuntu 20.04]
- Python version: [e.g., 3.9.7]
- PFAGD version: [e.g., 0.1.0]
- Device: [if mobile-related]

**Additional context**
Any other context about the problem.
```

## 💡 Feature Requests

### Feature Request Template
```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Other solutions you've considered.

**Additional context**
Any other context or screenshots.
```

## 🔄 Pull Request Process

### Before Submitting
1. **Fork** the repository
2. **Create feature branch** from `main`
3. **Make changes** with proper commit messages
4. **Add tests** for new functionality
5. **Update documentation** if needed
6. **Ensure all tests pass**

### Commit Message Format
```
type(scope): short description

Longer description if needed

Fixes #issue_number
```

Examples:
```
feat(engine): add sprite animation system
fix(cli): resolve import error in scaffold command
docs(readme): update installation instructions
test(assets): add unit tests for asset manager
```

### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have tested the changes on [Windows/Linux/Mac]

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
```

## 📚 Documentation

### Types of Documentation
- **API Documentation** - Code docstrings
- **User Guides** - Tutorials and how-tos
- **Developer Guides** - Internal architecture
- **Examples** - Working code samples

### Writing Documentation
- Use **clear, simple language**
- Provide **code examples**
- Include **expected output**
- Test all **commands and code**

## 🏷️ Release Process

### Versioning
We use [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Steps
1. Update version in `pfagd/version.py`
2. Update `CHANGELOG.md`
3. Create release PR
4. Tag release after merge
5. Publish to PyPI
6. Create GitHub release

## 🆘 Getting Help

- **Discussions**: [GitHub Discussions](https://github.com/pfagd/pfagd/discussions)
- **Issues**: [GitHub Issues](https://github.com/pfagd/pfagd/issues)
- **Discord**: [Join our Discord](https://discord.gg/pfagd)
- **Email**: dev@pfagd.org

## 📄 License

By contributing to PFAGD, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for their contributions
- **Special thanks** in documentation

Thank you for contributing to PFAGD! 🎮🚀