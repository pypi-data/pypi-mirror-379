# SIDS: Selective Interface Design System 🚀

[![PyPI version](https://badge.fury.io/py/sids.svg)](https://badge.fury.io/py/sids)
[![Python Support](https://img.shields.io/pypi/pyversions/sids.svg)](https://pypi.org/project/sids/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

SIDS (Selective Interface Design System) integrates **TailwindCSS** with **Python** for building beautiful GUIs everywhere - web apps, desktop applications, and Jupyter notebooks.

## 🎯 Features

- **Declarative Python API** - Build UIs like React, but in Python
- **TailwindCSS Integration** - Beautiful, responsive styling out of the box
- **Multi-Platform Rendering** - Deploy to Flask, FastAPI, Jupyter, or Tkinter
- **Component Library** - Pre-built buttons, cards, forms, and more
- **CLI Tools** - Easy project setup and development

## 🚀 Quick Start

### Installation

```bash
pip install sids
```

### Basic Example

```python
import sids as ui

# Create an app
app = ui.App()

# Define your UI
with app.page("Dashboard"):
    ui.H1("Welcome to SIDS! 🎉", classes="text-blue-600")
    ui.Button(
        "Click Me", 
        color="blue",
        on_click=lambda: print("Hello from SIDS!")
    )
    ui.Card(
        "This is a beautiful card styled with Tailwind!",
        classes="bg-gradient-to-r from-purple-500 to-pink-500"
    )

# Run anywhere
app.run("flask")    # Web app
app.run("jupyter")  # Jupyter notebook
app.run("tkinter")  # Desktop app
```

## 📦 Installation Options

```bash
# Basic installation
pip install sids

# With FastAPI support
pip install sids[fastapi]

# With Jupyter support  
pip install sids[jupyter]

# With everything
pip install sids[all]

# For development
pip install sids[dev]
```

## 🛠️ CLI Usage

```bash
# Initialize a new SIDS project
sids init my-app

# Run development server
sids run

# Build for production
sids build
```

## 🏗️ Architecture

SIDS provides a unified API that renders to multiple backends:

```
┌─────────────────┐
│   Python API    │  ← Your Code Here
├─────────────────┤
│   SIDS Core     │  ← Component System
├─────────────────┤
│    Adapters     │  ← Backend Integration
├─────┬─────┬─────┤
│Flask│Jptr │Tkntr│  ← Render Targets
└─────┴─────┴─────┘
```

## 📚 Documentation

- [Getting Started Guide](docs/getting-started.md)
- [Component Reference](docs/components.md)
- [Adapter Guide](docs/adapters.md)
- [API Documentation](docs/api.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [TailwindCSS](https://tailwindcss.com/)
- Inspired by [Streamlit](https://streamlit.io/) and [React](https://reactjs.org/)
- Python packaging with [setuptools](https://setuptools.pypa.io/)