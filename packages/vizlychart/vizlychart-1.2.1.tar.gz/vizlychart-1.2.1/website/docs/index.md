# VizlyChart Documentation

## The Advanced AI-Powered Visualization Library

VizlyChart is a next-generation Python visualization library that combines traditional charting with AI-powered features, unified backend switching, and enterprise-grade capabilities. Built for modern data science, machine learning, and business applications.

## 🚀 Key Features

### Core Visualization
- **50+ Chart Types**: From basic plots to advanced financial analysis
- **Pure Python Backend**: No matplotlib or plotly dependencies
- **High Performance**: GPU-accelerated rendering when available
- **Real-time Capable**: Live data streaming and updates

### 3D Interaction System
- **Advanced Camera Controls**: Orbit, fly, and first-person navigation
- **Gesture Recognition**: Multi-touch and mouse interaction
- **Object Manipulation**: 3D selection, transformation, and gizmos
- **VR/AR Support**: Immersive visualization capabilities

### Professional Features
- **Financial Analysis**: Technical indicators, candlestick charts
- **Engineering CAE**: Mesh visualization, field analysis
- **Web Components**: Interactive dashboards and galleries
- **Export Options**: PNG, SVG, PDF, and web formats

## 📚 Documentation Sections

### Getting Started
- [Installation Guide](installation.md)
- [Quick Start Tutorial](quickstart.md)
- [Basic Examples](examples/basic.md)

### API Reference
- [Chart Types](api/charts.md)
- [3D Interaction](api/interaction3d.md)
- [Core Rendering](api/rendering.md)
- [Web Components](api/web.md)

### Advanced Topics
- [Performance Optimization](advanced/performance.md)
- [Custom Chart Development](advanced/custom-charts.md)
- [3D Scene Management](advanced/3d-scenes.md)
- [Real-time Applications](advanced/realtime.md)

### Tutorials
- [Financial Visualization](tutorials/financial.md)
- [Engineering Applications](tutorials/engineering.md)
- [Interactive Dashboards](tutorials/dashboards.md)
- [VR/AR Development](tutorials/vr-ar.md)

### Examples
- [Chart Gallery](examples/gallery.md)
- [Sample Applications](examples/applications.md)
- [Integration Examples](examples/integration.md)

## 🎯 Quick Example

```python
import vizlychart as vc
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Create and customize chart
chart = vc.LineChart()
chart.plot(x, y, label="Noisy Sine Wave")
chart.set_title("My First VizlyChart")
chart.set_xlabel("Time")
chart.set_ylabel("Amplitude")
chart.show()
```

## 🎮 3D Interaction Example

```python
import plotx

# Create 3D interactive scene
scene = plotx.Scene3D()

# Add camera controller
camera = plotx.OrbitController()
scene.set_camera(camera)

# Add objects
for i in range(10):
    obj = plotx.Cube(position=[i*2, 0, 0])
    scene.add_object(obj)

# Enable interaction
scene.enable_selection(mode="multiple")
scene.enable_manipulation(transforms=["translate", "rotate"])

# Start interactive session
scene.run()
```

## 📈 Performance Comparison

| Feature | PlotX | Plotly | Matplotlib | VTK |
|---------|-------|--------|------------|-----|
| Rendering Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| 3D Interaction | ⭐⭐⭐⭐⭐ | ⭐⭐ | ❌ | ⭐⭐⭐⭐ |
| Web Integration | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Dependencies | ✅ None | ❌ Many | ❌ Many | ❌ Many |
| VR/AR Support | ⭐⭐⭐⭐⭐ | ❌ | ❌ | ⭐⭐ |
| Learning Curve | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |

## 🏗️ Architecture Overview

VizlyChart is built with a modular architecture that enables powerful features while maintaining simplicity:

```
VizlyChart Framework
├── Core Charts (LineChart, ScatterChart, BarChart)
├── AI Module
│   ├── Natural Language Processing
│   ├── Smart Chart Selection
│   └── Intelligent Styling
├── Backend System
│   ├── Matplotlib Backend
│   ├── Plotly Backend
│   └── Pure Python Backend
├── Advanced Visualizations
│   ├── ML Charts (SHAP, Feature Importance)
│   ├── Causal Charts (DAG, Confounders)
│   └── Statistical Charts
├── Enterprise Features
│   ├── Export Engine (PowerPoint, Excel, PDF)
│   ├── Branding System
│   └── Compliance Tools
└── Performance Engine
    ├── GPU Acceleration
    ├── Multi-threading
    └── Optimization
```

## 🌟 What Makes VizlyChart Different?

### AI-First Approach
The first visualization library with comprehensive AI integration for chart generation, smart recommendations, and natural language styling.

### Universal Backend Support
Switch between matplotlib, Plotly, and pure Python backends with the same API - unprecedented flexibility.

### Enterprise Ready
Professional exports, branding, compliance tracking, and audit trails built for business environments.

### ML-Focused Design
Native support for machine learning visualizations including SHAP analysis, causal inference, and model explainability.

### Performance Optimized
GPU acceleration and intelligent optimization for datasets from small to massive scale.

## 📱 Platform Support

- **Desktop**: Windows, macOS, Linux
- **Web Browsers**: Chrome, Firefox, Safari, Edge
- **Cloud**: AWS, GCP, Azure compatible
- **Notebooks**: Jupyter, Google Colab, VS Code
- **Enterprise**: On-premise and cloud deployment

## 🎓 Learning Resources

- [Getting Started Guide](getting-started/installation.md)
- [Interactive Examples](examples/index.md)
- [AI Features Tutorial](features/ai-features.md)
- [Best Practices](examples/best-practices.md)

## 🤝 Community & Support

- **GitHub**: [vizlychart/vizlychart](https://github.com/vizlychart/vizlychart)
- **Issues**: Report bugs and feature requests
- **Discussions**: Community Q&A and examples
- **Documentation**: This site and inline help

## 📄 License

VizlyChart is released under the MIT License. See [LICENSE](../LICENSE) for details.

---

**Ready to get started?** Check out our [Installation Guide](getting-started/installation.md) or explore the [Examples](examples/index.md)!