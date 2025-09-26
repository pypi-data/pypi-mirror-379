# Installation Guide

This guide will help you install VizlyChart and set up your environment for visualization development.

## Requirements

VizlyChart supports Python 3.8+ and works on all major platforms:

- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Operating Systems**: Windows, macOS, Linux
- **Memory**: Minimum 2GB RAM (4GB+ recommended for large datasets)

## Basic Installation

### Using pip (Recommended)

```bash
# Install the latest stable version
pip install vizlychart
```

### Using conda

```bash
# Install from conda-forge
conda install -c conda-forge vizlychart
```

## Installation Options

VizlyChart offers several installation options depending on your needs:

### Core Installation (Minimal)
```bash
# Basic charting functionality only
pip install vizlychart
```

**Includes:**
- Basic chart types (Line, Scatter, Bar, etc.)
- Core rendering engine
- Basic export options (PNG, SVG)

### Standard Installation
```bash
# Most common features
pip install vizlychart[standard]
```

**Includes:**
- All core features
- AI chart generation
- Backend switching (matplotlib, plotly)
- Enhanced export options

### Enterprise Installation
```bash
# Full enterprise features
pip install vizlychart[enterprise]
```

**Includes:**
- All standard features
- PowerPoint and Excel export
- Advanced branding and theming
- Compliance and audit tools
- Enterprise security features

### Full Installation
```bash
# Everything included
pip install vizlychart[all]
```

**Includes:**
- All available features
- GPU acceleration support
- Advanced ML visualizations
- Complete AI functionality
- All export formats
- Performance optimizations

## Development Installation

If you want to contribute to VizlyChart or need the latest development features:

```bash
# Clone the repository
git clone https://github.com/vizlychart/vizlychart.git
cd vizlychart

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e .[dev]
```

## Verifying Installation

After installation, verify that VizlyChart is working correctly:

```python
import vizlychart as vc
print(f"VizlyChart version: {vc.__version__}")

# Create a simple test chart
import numpy as np
x = np.linspace(0, 10, 50)
y = np.sin(x)

chart = vc.LineChart()
chart.plot(x, y, label="Test Chart")
chart.set_title("Installation Test")
print("✅ VizlyChart installed successfully!")
```

## Optional Dependencies

Some features require additional packages. Install them as needed:

### For AI Features
```bash
pip install transformers torch
```

### For GPU Acceleration
```bash
# NVIDIA GPUs
pip install cupy-cuda11x

# Or for CPU-optimized performance
pip install numba
```

### For Enhanced Exports
```bash
# PowerPoint export
pip install python-pptx

# Excel export
pip install openpyxl xlsxwriter

# Advanced PDF
pip install reportlab
```

### For Web Features
```bash
pip install flask dash streamlit
```

## Platform-Specific Notes

### Windows
- Install Visual C++ Build Tools if you encounter compilation errors
- Use Anaconda or Miniconda for easier dependency management

### macOS
- Install Xcode Command Line Tools: `xcode-select --install`
- For M1/M2 Macs, use conda for optimal performance

### Linux
- Install development headers: `sudo apt-get install python3-dev`
- For GPU acceleration, ensure CUDA drivers are installed

## Virtual Environments

We strongly recommend using virtual environments:

### Using venv
```bash
python -m venv vizly_env
source vizly_env/bin/activate  # On Windows: vizly_env\Scripts\activate
pip install vizlychart[standard]
```

### Using conda
```bash
conda create -n vizly_env python=3.10
conda activate vizly_env
pip install vizlychart[standard]
```

## Troubleshooting

### Common Issues

**Import Error: No module named 'vizlychart'**
```bash
# Ensure you're in the correct environment
pip list | grep vizlychart
# If not found, reinstall
pip install vizlychart
```

**Backend Issues**
```bash
# Install specific backends if needed
pip install matplotlib plotly
```

**Performance Issues**
```bash
# Install performance packages
pip install numba cython
```

**Export Issues**
```bash
# Install export dependencies
pip install python-pptx openpyxl reportlab
```

### Getting Help

If you encounter issues:

1. Check our [FAQ](../troubleshooting/faq.md)
2. Search [GitHub Issues](https://github.com/vizlychart/vizlychart/issues)
3. Create a new issue with:
   - Your Python version (`python --version`)
   - VizlyChart version (`import vizlychart; print(vizlychart.__version__)`)
   - Operating system
   - Full error message

## What's Next?

After successful installation:

1. **[Quick Start Tutorial](quickstart.md)** - Create your first chart
2. **[Basic Concepts](concepts.md)** - Learn VizlyChart fundamentals
3. **[Examples](../examples/index.md)** - Explore code examples
4. **[API Reference](../api/core.md)** - Detailed documentation

## Upgrading

To upgrade to the latest version:

```bash
# Upgrade to latest stable
pip install --upgrade vizlychart

# Upgrade with all features
pip install --upgrade vizlychart[all]
```

To check for updates:
```python
import vizlychart as vc
print(f"Current version: {vc.__version__}")
# Check GitHub releases for latest version
```

---

**Ready to start?** Continue to the [Quick Start Tutorial](quickstart.md) to create your first chart!