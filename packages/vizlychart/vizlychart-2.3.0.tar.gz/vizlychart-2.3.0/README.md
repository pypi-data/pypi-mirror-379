# VizlyChart

A Python visualization library focused on performance and professional output quality.

## Features

- **Fast rendering**: Optimized SVG generation with performance improvements over baseline matplotlib workflows
- **Professional output**: Clean typography with customizable fonts and spacing
- **GPU acceleration support**: Optional CuPy integration for data processing acceleration
- **Multiple chart types**: Line charts, scatter plots, bar charts, and 3D surfaces
- **Engineering utilities**: Specialized charts for technical applications

## Installation

```bash
pip install vizlychart
```

For GPU acceleration (requires NVIDIA GPU):
```bash
pip install vizlychart[gpu]
```

For extended functionality with matplotlib integration:
```bash
pip install vizlychart[extended]
```

## Quick Start

```python
import vizlychart as vc
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create and customize chart
chart = vc.LineChart()
chart.plot(x, y, label='sin(x)')
chart.set_title('Sample Chart')
chart.set_labels('X-axis', 'Y-axis')

# Save as SVG
chart.save('output.svg')
```

## Performance

VizlyChart focuses on practical performance improvements:
- SVG-first rendering for scalable output
- Memory-efficient processing for large datasets
- Optional GPU acceleration for data preprocessing

## Requirements

- Python 3.7+
- NumPy 1.24+

Optional dependencies:
- CuPy (GPU acceleration)
- Matplotlib (extended compatibility)
- SciPy (engineering functions)

## Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. Clone the repository:
```bash
git clone https://github.com/vizlychart/vizlychart.git
cd vizlychart
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .[dev]
```

### Running Tests

```bash
pytest
```

### Code Style

We use Black for formatting and Ruff for linting:
```bash
black src tests
ruff check src tests
```

### Ways to Contribute

- **Bug reports**: Open an issue describing the problem with minimal reproduction steps
- **Feature requests**: Suggest new chart types or functionality improvements
- **Documentation**: Help improve examples, docstrings, or tutorials
- **Code contributions**: Fix bugs, implement features, or optimize performance
- **Testing**: Add test cases or improve test coverage

### Pull Request Guidelines

1. Fork the repository and create a feature branch
2. Write tests for new functionality
3. Ensure all tests pass and code follows style guidelines
4. Update documentation if needed
5. Submit a pull request with a clear description

### Areas We'd Love Help With

- Additional chart types (violin plots, heat maps, etc.)
- Performance optimizations
- Better error messages and validation
- Cross-platform testing
- Documentation and examples

## License

MIT License - see LICENSE file for details.

## Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/vizlychart/vizlychart/issues)
- **Discussions**: Community discussion and questions
- **Documentation**: More examples and API documentation coming soon

---

Built with focus on practical performance and professional output quality.