<?php
$page_title = "Documentation";
require_once 'includes/config.php';
require_once 'includes/header.php';
?>

<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1>Documentation</h1>
            <p>Complete guides, API reference, and tutorials to get you started with Vizly</p>
            <div class="doc-search">
                <div class="search-container">
                    <input type="text" id="doc-search" placeholder="Search documentation..." />
                    <button class="search-btn">
                        <i class="fas fa-search"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="docs-layout">
            <nav class="docs-sidebar">
                <div class="sidebar-section">
                    <h3>Getting Started</h3>
                    <ul>
                        <li><a href="#installation" class="doc-link active">Installation</a></li>
                        <li><a href="#quick-start" class="doc-link">Quick Start</a></li>
                        <li><a href="#basic-concepts" class="doc-link">Basic Concepts</a></li>
                        <li><a href="#first-chart" class="doc-link">Your First Chart</a></li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <h3>Chart Types</h3>
                    <ul>
                        <li><a href="#line-charts" class="doc-link">Line Charts</a></li>
                        <li><a href="#scatter-plots" class="doc-link">Scatter Plots</a></li>
                        <li><a href="#bar-charts" class="doc-link">Bar Charts</a></li>
                        <li><a href="#surface-plots" class="doc-link">3D Surface Plots</a></li>
                        <li><a href="#financial-charts" class="doc-link">Financial Charts</a></li>
                        <li><a href="#engineering-charts" class="doc-link">Engineering Charts</a></li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <h3>Advanced Features</h3>
                    <ul>
                        <li><a href="#gpu-acceleration" class="doc-link">GPU Acceleration</a></li>
                        <li><a href="#vr-ar" class="doc-link">VR/AR Visualization</a></li>
                        <li><a href="#real-time" class="doc-link">Real-time Streaming</a></li>
                        <li><a href="#themes" class="doc-link">Themes & Styling</a></li>
                        <li><a href="#export" class="doc-link">Export Options</a></li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <h3>SDKs</h3>
                    <ul>
                        <li><a href="#python-sdk" class="doc-link">Python SDK</a></li>
                        <li><a href="#csharp-sdk" class="doc-link">C# SDK</a></li>
                        <li><a href="#cpp-sdk" class="doc-link">C++ SDK</a></li>
                        <li><a href="#java-sdk" class="doc-link">Java SDK</a></li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <h3>API Reference</h3>
                    <ul>
                        <li><a href="#api-figure" class="doc-link">Figure API</a></li>
                        <li><a href="#api-charts" class="doc-link">Chart Classes</a></li>
                        <li><a href="#api-themes" class="doc-link">Theme API</a></li>
                        <li><a href="#api-export" class="doc-link">Export API</a></li>
                    </ul>
                </div>
            </nav>

            <main class="docs-content">
                <section id="installation" class="doc-section">
                    <h2>Installation</h2>
                    <p>Get started with Vizly using your preferred package manager.</p>

                    <div class="installation-tabs">
                        <div class="tab-buttons">
                            <button class="tab-btn active" onclick="showTab('python-install')">Python</button>
                            <button class="tab-btn" onclick="showTab('csharp-install')">C#</button>
                            <button class="tab-btn" onclick="showTab('cpp-install')">C++</button>
                            <button class="tab-btn" onclick="showTab('java-install')">Java</button>
                        </div>

                        <div id="python-install" class="tab-content active">
                            <h3>Python Installation</h3>
                            <div class="code-block">
                                <pre><code># Install from PyPI
pip install vizlychart

# Verify installation
python -c "import vizly; print(vizly.__version__)"

# Install with GPU support (optional)
pip install vizlychart[gpu]

# Install development dependencies
pip install vizlychart[dev]</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                            <div class="requirements">
                                <h4>Requirements</h4>
                                <ul>
                                    <li>Python 3.7+</li>
                                    <li>NumPy 1.19.0+</li>
                                    <li>Matplotlib 3.5.0+</li>
                                    <li>CUDA toolkit (for GPU acceleration)</li>
                                </ul>
                            </div>
                        </div>

                        <div id="csharp-install" class="tab-content">
                            <h3>C# (.NET) Installation</h3>
                            <div class="code-block">
                                <pre><code># Install via NuGet Package Manager
Install-Package Vizly.SDK

# Or via .NET CLI
dotnet add package Vizly.SDK

# Verify installation
using Vizly;
Console.WriteLine(VizlyInfo.Version);</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                            <div class="requirements">
                                <h4>Requirements</h4>
                                <ul>
                                    <li>.NET 6.0+</li>
                                    <li>Visual Studio 2022 or VS Code</li>
                                    <li>CUDA toolkit (for GPU acceleration)</li>
                                </ul>
                            </div>
                        </div>

                        <div id="cpp-install" class="tab-content">
                            <h3>C++ Installation</h3>
                            <div class="code-block">
                                <pre><code># CMake integration
find_package(Vizly REQUIRED)
target_link_libraries(your_target Vizly::Vizly)

# Or manual installation
git clone https://github.com/vizly/vizly-cpp
cd vizly-cpp
mkdir build && cd build
cmake ..
make install</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                            <div class="requirements">
                                <h4>Requirements</h4>
                                <ul>
                                    <li>C++17 compiler</li>
                                    <li>CMake 3.16+</li>
                                    <li>OpenGL 4.0+</li>
                                    <li>CUDA toolkit (optional)</li>
                                </ul>
                            </div>
                        </div>

                        <div id="java-install" class="tab-content">
                            <h3>Java Installation</h3>
                            <div class="code-block">
                                <pre><code><!-- Maven dependency -->
&lt;dependency&gt;
    &lt;groupId&gt;com.vizly&lt;/groupId&gt;
    &lt;artifactId&gt;vizly-sdk&lt;/artifactId&gt;
    &lt;version&gt;1.1.0&lt;/version&gt;
&lt;/dependency&gt;

// Gradle dependency
implementation 'com.vizly:vizly-sdk:1.1.0'</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                            <div class="requirements">
                                <h4>Requirements</h4>
                                <ul>
                                    <li>Java 11+</li>
                                    <li>Maven 3.6+ or Gradle 6.0+</li>
                                    <li>OpenJFX (for GUI components)</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="quick-start" class="doc-section">
                    <h2>Quick Start</h2>
                    <p>Create your first visualization in just a few lines of code.</p>

                    <div class="example-container">
                        <div class="example-code">
                            <h3>Basic Line Chart</h3>
                            <div class="code-block">
                                <pre><code>import vizly as vz

# Create a figure
fig = vz.Figure()

# Create a line chart
chart = vz.LineChart(fig)

# Plot data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
chart.plot(x, y, label='Sample Data')

# Customize
chart.set_title('My First Chart')
chart.set_xlabel('X Values')
chart.set_ylabel('Y Values')

# Display
fig.show()</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                        </div>
                        <div class="example-output">
                            <h3>Output</h3>
                            <div class="chart-preview">
                                <canvas id="quick-start-chart" width="400" height="300"></canvas>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="basic-concepts" class="doc-section">
                    <h2>Basic Concepts</h2>
                    <p>Understanding the core concepts of Vizly's architecture.</p>

                    <div class="concept-grid">
                        <div class="concept-card">
                            <div class="concept-icon">
                                <i class="fas fa-layer-group"></i>
                            </div>
                            <h3>Figure</h3>
                            <p>The main container for your visualizations. Think of it as a canvas that holds one or more charts.</p>
                            <div class="code-snippet">
                                <code>fig = vz.Figure(width=800, height=600)</code>
                            </div>
                        </div>

                        <div class="concept-card">
                            <div class="concept-icon">
                                <i class="fas fa-chart-line"></i>
                            </div>
                            <h3>Charts</h3>
                            <p>Individual visualization components like LineChart, ScatterChart, BarChart, etc.</p>
                            <div class="code-snippet">
                                <code>chart = vz.LineChart(fig)</code>
                            </div>
                        </div>

                        <div class="concept-card">
                            <div class="concept-icon">
                                <i class="fas fa-palette"></i>
                            </div>
                            <h3>Themes</h3>
                            <p>Pre-defined styling configurations that control the appearance of your visualizations.</p>
                            <div class="code-snippet">
                                <code>fig.set_theme('professional')</code>
                            </div>
                        </div>

                        <div class="concept-card">
                            <div class="concept-icon">
                                <i class="fas fa-download"></i>
                            </div>
                            <h3>Export</h3>
                            <p>Save your visualizations in various formats including PNG, SVG, PDF, and interactive HTML.</p>
                            <div class="code-snippet">
                                <code>fig.export('chart.png', dpi=300)</code>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="gpu-acceleration" class="doc-section">
                    <h2>GPU Acceleration</h2>
                    <p>Harness the power of GPU computing for lightning-fast visualizations.</p>

                    <div class="feature-highlight">
                        <div class="highlight-content">
                            <h3>Performance Benefits</h3>
                            <ul>
                                <li><strong>10x-50x speedup</strong> for large datasets</li>
                                <li><strong>Real-time rendering</strong> of millions of points</li>
                                <li><strong>Automatic optimization</strong> based on data size</li>
                                <li><strong>Memory efficient</strong> processing</li>
                            </ul>
                        </div>
                        <div class="highlight-code">
                            <div class="code-block">
                                <pre><code># Enable GPU acceleration
fig = vz.Figure(gpu=True)

# Automatic GPU selection
chart = vz.ScatterChart(fig)

# Handle large datasets efficiently
import numpy as np
x = np.random.randn(1_000_000)
y = np.random.randn(1_000_000)

# Renders in <100ms with GPU
chart.scatter(x, y, alpha=0.6)

# Check GPU status
print(f"GPU enabled: {fig.gpu_enabled}")
print(f"GPU device: {fig.gpu_device}")</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="performance-comparison">
                        <h3>Performance Comparison</h3>
                        <table class="comparison-table">
                            <thead>
                                <tr>
                                    <th>Data Size</th>
                                    <th>CPU Time</th>
                                    <th>GPU Time</th>
                                    <th>Speedup</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>10K points</td>
                                    <td>200ms</td>
                                    <td>25ms</td>
                                    <td class="speedup">8x</td>
                                </tr>
                                <tr>
                                    <td>100K points</td>
                                    <td>2s</td>
                                    <td>100ms</td>
                                    <td class="speedup">20x</td>
                                </tr>
                                <tr>
                                    <td>1M points</td>
                                    <td>20s</td>
                                    <td>500ms</td>
                                    <td class="speedup">40x</td>
                                </tr>
                                <tr>
                                    <td>10M points</td>
                                    <td>200s</td>
                                    <td>4s</td>
                                    <td class="speedup">50x</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <section id="vr-ar" class="doc-section">
                    <h2>VR/AR Visualization</h2>
                    <p>Create immersive data experiences with WebXR integration.</p>

                    <div class="vr-features">
                        <div class="vr-feature">
                            <h3><i class="fas fa-vr-cardboard"></i> WebXR Integration</h3>
                            <p>Browser-based VR/AR experiences that work across devices.</p>
                            <div class="code-block">
                                <pre><code># Create VR-enabled figure
fig = vz.Figure(mode='vr')

# Add 3D scene
scene = vz.Scene3D(fig)

# Create immersive surface plot
scene.surface(x, y, z, interactive=True)

# Enable hand tracking
scene.enable_hand_tracking()

# Export as WebXR app
fig.export_webxr('my_vr_viz.html')</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                        </div>

                        <div class="vr-feature">
                            <h3><i class="fas fa-hand-paper"></i> Hand Tracking</h3>
                            <p>Natural interaction with your data using gesture recognition.</p>
                            <div class="code-block">
                                <pre><code># Configure hand tracking
scene.hand_tracking.configure({
    'pinch_sensitivity': 0.8,
    'gesture_recognition': True,
    'haptic_feedback': True
})

# Define gesture callbacks
@scene.on_gesture('pinch')
def on_pinch(data):
    scene.zoom(data.scale)

@scene.on_gesture('rotate')
def on_rotate(data):
    scene.rotate(data.angle)</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="real-time" class="doc-section">
                    <h2>Real-time Streaming</h2>
                    <p>Stream live data with sub-millisecond latency for dynamic visualizations.</p>

                    <div class="streaming-example">
                        <div class="streaming-code">
                            <h3>WebSocket Streaming</h3>
                            <div class="code-block">
                                <pre><code># Create streaming figure
fig = vz.Figure()
chart = vz.LineChart(fig)

# Setup data stream
stream = vz.DataStream('ws://localhost:8080/data')

# Configure real-time updates
stream.configure({
    'buffer_size': 1000,
    'update_interval': 16,  # 60 FPS
    'compression': True
})

# Connect stream to chart
stream.connect(chart.update_data)

# Start live visualization
fig.show_live()

# Stream will automatically update chart
# as new data arrives</code></pre>
                                <button class="copy-code" onclick="copyCode(this)">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </div>
                        </div>

                        <div class="streaming-protocols">
                            <h3>Supported Protocols</h3>
                            <div class="protocol-list">
                                <div class="protocol">
                                    <i class="fas fa-bolt"></i>
                                    <h4>WebSocket</h4>
                                    <p>Real-time bidirectional communication</p>
                                </div>
                                <div class="protocol">
                                    <i class="fas fa-sync-alt"></i>
                                    <h4>HTTP Polling</h4>
                                    <p>Compatible with existing REST APIs</p>
                                </div>
                                <div class="protocol">
                                    <i class="fas fa-database"></i>
                                    <h4>Redis Pub/Sub</h4>
                                    <p>High-throughput message streaming</p>
                                </div>
                                <div class="protocol">
                                    <i class="fas fa-file-alt"></i>
                                    <h4>File Watching</h4>
                                    <p>Monitor files for changes</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="api-reference" class="doc-section">
                    <h2>API Reference</h2>
                    <p>Complete reference documentation for all Vizly classes and methods.</p>

                    <div class="api-grid">
                        <div class="api-section">
                            <h3>Core Classes</h3>
                            <div class="api-item">
                                <h4><code>vz.Figure</code></h4>
                                <p>Main visualization container</p>
                                <details>
                                    <summary>Methods</summary>
                                    <ul>
                                        <li><code>show()</code> - Display the figure</li>
                                        <li><code>export(format, **kwargs)</code> - Export to file</li>
                                        <li><code>set_theme(theme)</code> - Apply theme</li>
                                        <li><code>add_chart(chart)</code> - Add chart to figure</li>
                                    </ul>
                                </details>
                            </div>

                            <div class="api-item">
                                <h4><code>vz.LineChart</code></h4>
                                <p>Line and curve plotting</p>
                                <details>
                                    <summary>Methods</summary>
                                    <ul>
                                        <li><code>plot(x, y, **kwargs)</code> - Plot line</li>
                                        <li><code>set_title(title)</code> - Set chart title</li>
                                        <li><code>set_xlabel(label)</code> - Set X axis label</li>
                                        <li><code>set_ylabel(label)</code> - Set Y axis label</li>
                                    </ul>
                                </details>
                            </div>

                            <div class="api-item">
                                <h4><code>vz.ScatterChart</code></h4>
                                <p>Scatter plot visualization</p>
                                <details>
                                    <summary>Methods</summary>
                                    <ul>
                                        <li><code>scatter(x, y, **kwargs)</code> - Create scatter plot</li>
                                        <li><code>set_point_size(size)</code> - Set point size</li>
                                        <li><code>set_alpha(alpha)</code> - Set transparency</li>
                                        <li><code>add_regression_line()</code> - Add trend line</li>
                                    </ul>
                                </details>
                            </div>
                        </div>

                        <div class="api-section">
                            <h3>Advanced Features</h3>
                            <div class="api-item">
                                <h4><code>vz.DataStream</code></h4>
                                <p>Real-time data streaming</p>
                                <details>
                                    <summary>Methods</summary>
                                    <ul>
                                        <li><code>connect(callback)</code> - Connect to data source</li>
                                        <li><code>configure(options)</code> - Set streaming options</li>
                                        <li><code>start()</code> - Begin streaming</li>
                                        <li><code>stop()</code> - Stop streaming</li>
                                    </ul>
                                </details>
                            </div>

                            <div class="api-item">
                                <h4><code>vz.Scene3D</code></h4>
                                <p>3D and VR visualization</p>
                                <details>
                                    <summary>Methods</summary>
                                    <ul>
                                        <li><code>surface(x, y, z)</code> - 3D surface plot</li>
                                        <li><code>enable_hand_tracking()</code> - Enable VR controls</li>
                                        <li><code>set_camera(position)</code> - Set view angle</li>
                                        <li><code>add_lighting(type)</code> - Configure lighting</li>
                                    </ul>
                                </details>
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    </div>
</section>

<section class="section" style="background: var(--gradient-primary); color: white;">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title" style="color: white;">Need Help?</h2>
            <p class="section-subtitle" style="color: rgba(255,255,255,0.9);">
                Get support from our community and expert team
            </p>
        </div>

        <div class="help-grid">
            <div class="help-option">
                <div class="help-icon">
                    <i class="fab fa-github"></i>
                </div>
                <h3>GitHub Issues</h3>
                <p>Report bugs, request features, and get community support</p>
                <a href="https://github.com/vizly/vizly/issues" class="btn btn-outline" target="_blank">
                    <i class="fab fa-github"></i> Open Issue
                </a>
            </div>

            <div class="help-option">
                <div class="help-icon">
                    <i class="fas fa-comments"></i>
                </div>
                <h3>Community Forum</h3>
                <p>Join discussions, share examples, and learn from other users</p>
                <a href="#" class="btn btn-outline">
                    <i class="fas fa-comments"></i> Join Forum
                </a>
            </div>

            <div class="help-option">
                <div class="help-icon">
                    <i class="fas fa-envelope"></i>
                </div>
                <h3>Enterprise Support</h3>
                <p>Get dedicated support with guaranteed response times</p>
                <a href="contact.php" class="btn btn-secondary">
                    <i class="fas fa-envelope"></i> Contact Support
                </a>
            </div>

            <div class="help-option">
                <div class="help-icon">
                    <i class="fas fa-graduation-cap"></i>
                </div>
                <h3>Training</h3>
                <p>Professional training programs and certification courses</p>
                <a href="contact.php" class="btn btn-outline">
                    <i class="fas fa-graduation-cap"></i> Learn More
                </a>
            </div>
        </div>
    </div>
</section>

<style>
.doc-search {
    margin-top: 2rem;
}

.search-container {
    display: flex;
    max-width: 500px;
    margin: 0 auto;
    background: white;
    border-radius: 2rem;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
}

.search-container input {
    flex: 1;
    padding: 1rem 1.5rem;
    border: none;
    font-size: var(--font-size-base);
    outline: none;
}

.search-btn {
    background: var(--gradient-secondary);
    color: white;
    border: none;
    padding: 1rem 1.5rem;
    cursor: pointer;
    transition: var(--transition-fast);
}

.search-btn:hover {
    background: var(--gradient-primary);
}

.docs-layout {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 3rem;
    align-items: start;
}

.docs-sidebar {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: var(--shadow-lg);
    position: sticky;
    top: 100px;
    max-height: calc(100vh - 120px);
    overflow-y: auto;
}

.sidebar-section {
    margin-bottom: 2rem;
}

.sidebar-section:last-child {
    margin-bottom: 0;
}

.sidebar-section h3 {
    color: var(--text-light);
    margin-bottom: 1rem;
    font-size: var(--font-size-lg);
    border-bottom: 2px solid var(--bg-light-secondary);
    padding-bottom: 0.5rem;
}

.sidebar-section ul {
    list-style: none;
    padding: 0;
}

.sidebar-section li {
    margin-bottom: 0.5rem;
}

.doc-link {
    display: block;
    padding: 0.5rem 1rem;
    color: var(--text-light-secondary);
    text-decoration: none;
    border-radius: 0.5rem;
    transition: var(--transition-fast);
}

.doc-link:hover,
.doc-link.active {
    background: var(--gradient-primary);
    color: white;
}

.docs-content {
    background: white;
    border-radius: 1rem;
    padding: 3rem;
    box-shadow: var(--shadow-lg);
}

.doc-section {
    margin-bottom: 4rem;
    padding-bottom: 3rem;
    border-bottom: 1px solid var(--bg-light-secondary);
}

.doc-section:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.doc-section h2 {
    color: var(--text-light);
    margin-bottom: 1rem;
    font-size: var(--font-size-3xl);
}

.doc-section p {
    color: var(--text-light-secondary);
    font-size: var(--font-size-lg);
    margin-bottom: 2rem;
    line-height: 1.6;
}

.installation-tabs {
    background: var(--bg-light-secondary);
    border-radius: 1rem;
    overflow: hidden;
}

.tab-buttons {
    display: flex;
    background: var(--gradient-primary);
}

.tab-btn {
    flex: 1;
    padding: 1rem;
    background: transparent;
    border: none;
    color: rgba(255,255,255,0.7);
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition-fast);
}

.tab-btn.active,
.tab-btn:hover {
    background: rgba(255,255,255,0.2);
    color: white;
}

.tab-content {
    display: none;
    padding: 2rem;
}

.tab-content.active {
    display: block;
}

.tab-content h3 {
    color: var(--text-light);
    margin-bottom: 1.5rem;
}

.code-block {
    position: relative;
    background: var(--bg-dark);
    color: var(--text-dark);
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin: 1.5rem 0;
    overflow-x: auto;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: var(--font-size-sm);
    line-height: 1.5;
}

.copy-code {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: rgba(255,255,255,0.1);
    color: var(--text-dark-secondary);
    border: none;
    padding: 0.5rem;
    border-radius: 0.25rem;
    cursor: pointer;
    transition: var(--transition-fast);
}

.copy-code:hover {
    background: rgba(255,255,255,0.2);
    color: var(--text-dark);
}

.requirements {
    background: white;
    border: 1px solid var(--bg-light-secondary);
    border-radius: 0.5rem;
    padding: 1.5rem;
    margin-top: 1rem;
}

.requirements h4 {
    color: var(--text-light);
    margin-bottom: 1rem;
}

.requirements ul {
    color: var(--text-light-secondary);
    padding-left: 1.5rem;
}

.requirements li {
    margin-bottom: 0.5rem;
}

.example-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    background: var(--bg-light-secondary);
    border-radius: 1rem;
    padding: 2rem;
}

.example-code h3,
.example-output h3 {
    color: var(--text-light);
    margin-bottom: 1rem;
}

.chart-preview {
    background: white;
    border-radius: 0.5rem;
    padding: 1rem;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--bg-light-secondary);
}

.concept-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.concept-card {
    background: var(--bg-light-secondary);
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    transition: var(--transition-normal);
}

.concept-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
}

.concept-icon {
    width: 80px;
    height: 80px;
    background: var(--gradient-primary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    font-size: 2rem;
    color: white;
}

.concept-card h3 {
    color: var(--text-light);
    margin-bottom: 1rem;
}

.concept-card p {
    color: var(--text-light-secondary);
    margin-bottom: 1.5rem;
    font-size: var(--font-size-base);
}

.code-snippet {
    background: var(--bg-dark);
    color: var(--secondary-color);
    padding: 0.75rem;
    border-radius: 0.5rem;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: var(--font-size-sm);
}

.feature-highlight {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    background: var(--bg-light-secondary);
    border-radius: 1rem;
    padding: 2rem;
    margin: 2rem 0;
}

.highlight-content h3 {
    color: var(--text-light);
    margin-bottom: 1rem;
}

.highlight-content ul {
    color: var(--text-light-secondary);
    padding-left: 1.5rem;
}

.highlight-content li {
    margin-bottom: 0.75rem;
}

.highlight-content strong {
    color: var(--primary-color);
}

.performance-comparison {
    margin: 2rem 0;
}

.performance-comparison h3 {
    color: var(--text-light);
    margin-bottom: 1.5rem;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 0.5rem;
    overflow: hidden;
    box-shadow: var(--shadow-md);
}

.comparison-table th {
    background: var(--gradient-primary);
    color: white;
    padding: 1rem;
    text-align: left;
    font-weight: 600;
}

.comparison-table td {
    padding: 1rem;
    border-bottom: 1px solid var(--bg-light-secondary);
}

.comparison-table tr:last-child td {
    border-bottom: none;
}

.speedup {
    color: var(--secondary-color);
    font-weight: 600;
}

.vr-features {
    display: grid;
    gap: 3rem;
}

.vr-feature {
    background: var(--bg-light-secondary);
    border-radius: 1rem;
    padding: 2rem;
}

.vr-feature h3 {
    color: var(--text-light);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.vr-feature h3 i {
    color: var(--primary-color);
}

.vr-feature p {
    color: var(--text-light-secondary);
    margin-bottom: 1.5rem;
    font-size: var(--font-size-base);
}

.streaming-example {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.streaming-code h3,
.streaming-protocols h3 {
    color: var(--text-light);
    margin-bottom: 1.5rem;
}

.protocol-list {
    display: grid;
    gap: 1rem;
}

.protocol {
    background: white;
    padding: 1.5rem;
    border-radius: 0.5rem;
    border: 1px solid var(--bg-light-secondary);
    display: flex;
    align-items: center;
    gap: 1rem;
}

.protocol i {
    color: var(--primary-color);
    font-size: 1.5rem;
    width: 30px;
}

.protocol h4 {
    color: var(--text-light);
    margin-bottom: 0.25rem;
}

.protocol p {
    color: var(--text-light-secondary);
    margin: 0;
    font-size: var(--font-size-sm);
}

.api-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
}

.api-section h3 {
    color: var(--text-light);
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--primary-color);
}

.api-item {
    background: var(--bg-light-secondary);
    border-radius: 0.5rem;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

.api-item h4 {
    color: var(--text-light);
    margin-bottom: 0.75rem;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: var(--font-size-lg);
}

.api-item p {
    color: var(--text-light-secondary);
    margin-bottom: 1rem;
    font-size: var(--font-size-base);
}

.api-item details {
    cursor: pointer;
}

.api-item summary {
    color: var(--primary-color);
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.api-item ul {
    color: var(--text-light-secondary);
    padding-left: 1.5rem;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: var(--font-size-sm);
}

.api-item li {
    margin-bottom: 0.5rem;
}

.help-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}

.help-option {
    background: rgba(255,255,255,0.1);
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    transition: var(--transition-normal);
}

.help-option:hover {
    background: rgba(255,255,255,0.15);
    transform: translateY(-5px);
}

.help-icon {
    width: 80px;
    height: 80px;
    background: rgba(255,255,255,0.2);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    font-size: 2rem;
    color: white;
}

.help-option h3 {
    color: white;
    margin-bottom: 1rem;
}

.help-option p {
    color: rgba(255,255,255,0.9);
    margin-bottom: 2rem;
    font-size: var(--font-size-base);
}

@media (prefers-color-scheme: dark) {
    .docs-sidebar,
    .docs-content,
    .requirements,
    .chart-preview,
    .protocol,
    .api-item {
        background: var(--bg-dark-secondary);
        border: 1px solid rgba(255,255,255,0.05);
    }

    .sidebar-section h3,
    .doc-section h2,
    .doc-section p,
    .concept-card h3,
    .concept-card p,
    .requirements h4,
    .example-code h3,
    .example-output h3,
    .highlight-content h3,
    .performance-comparison h3,
    .vr-feature h3,
    .vr-feature p,
    .streaming-code h3,
    .streaming-protocols h3,
    .api-section h3,
    .api-item h4,
    .api-item p,
    .protocol h4 {
        color: var(--text-dark);
    }

    .doc-link {
        color: var(--text-dark-secondary);
    }

    .concept-card,
    .feature-highlight,
    .vr-feature {
        background: var(--bg-dark);
    }

    .installation-tabs {
        background: var(--bg-dark);
    }

    .example-container {
        background: var(--bg-dark);
    }

    .comparison-table {
        background: var(--bg-dark-secondary);
    }

    .comparison-table td {
        border-color: rgba(255,255,255,0.1);
    }

    .requirements ul,
    .highlight-content ul,
    .api-item ul {
        color: var(--text-dark-secondary);
    }

    .protocol p {
        color: var(--text-dark-secondary);
    }
}

@media (max-width: 768px) {
    .docs-layout {
        grid-template-columns: 1fr;
        gap: 2rem;
    }

    .docs-sidebar {
        position: static;
        max-height: none;
    }

    .docs-content {
        padding: 2rem;
    }

    .example-container,
    .feature-highlight,
    .streaming-example,
    .api-grid {
        grid-template-columns: 1fr;
    }

    .help-grid {
        grid-template-columns: 1fr;
    }

    .concept-grid {
        grid-template-columns: 1fr;
    }

    .tab-buttons {
        flex-wrap: wrap;
    }

    .tab-btn {
        flex: 1 1 50%;
    }
}
</style>

<script>
// Initialize documentation page
document.addEventListener('DOMContentLoaded', function() {
    initializeTabs();
    initializeNavigation();
    initializeQuickStartChart();
    initializeCodeCopying();
});

function initializeTabs() {
    window.showTab = function(tabId) {
        // Hide all tab contents
        document.querySelectorAll('.tab-content').forEach(tab => {
            tab.classList.remove('active');
        });

        // Remove active class from all tab buttons
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('active');
        });

        // Show selected tab
        document.getElementById(tabId).classList.add('active');

        // Add active class to clicked button
        event.target.classList.add('active');
    };
}

function initializeNavigation() {
    const docLinks = document.querySelectorAll('.doc-link');

    docLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            // Remove active class from all links
            docLinks.forEach(l => l.classList.remove('active'));

            // Add active class to clicked link
            this.classList.add('active');

            // Scroll to section
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Update active link on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                const link = document.querySelector(`a[href="#${id}"]`);

                if (link) {
                    docLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                }
            }
        });
    }, {
        threshold: 0.3,
        rootMargin: '-100px 0px -50% 0px'
    });

    document.querySelectorAll('.doc-section').forEach(section => {
        observer.observe(section);
    });
}

function initializeQuickStartChart() {
    const ctx = document.getElementById('quick-start-chart');
    if (ctx) {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['1', '2', '3', '4', '5'],
                datasets: [{
                    label: 'Sample Data',
                    data: [2, 4, 1, 5, 3],
                    borderColor: 'rgb(37, 99, 235)',
                    backgroundColor: 'rgba(37, 99, 235, 0.1)',
                    tension: 0.4,
                    fill: true,
                    pointBackgroundColor: 'rgb(37, 99, 235)',
                    pointBorderColor: 'white',
                    pointBorderWidth: 2,
                    pointRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top'
                    }
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'X Values'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Y Values'
                        }
                    }
                }
            }
        });
    }
}

function initializeCodeCopying() {
    window.copyCode = function(button) {
        const codeBlock = button.parentElement;
        const code = codeBlock.querySelector('pre code').textContent;

        navigator.clipboard.writeText(code).then(() => {
            const originalIcon = button.innerHTML;
            button.innerHTML = '<i class="fas fa-check"></i>';
            button.style.color = '#10b981';

            setTimeout(() => {
                button.innerHTML = originalIcon;
                button.style.color = '';
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy code:', err);
        });
    };
}

// Search functionality
document.getElementById('doc-search').addEventListener('input', function(e) {
    const query = e.target.value.toLowerCase();
    const sections = document.querySelectorAll('.doc-section');

    sections.forEach(section => {
        const content = section.textContent.toLowerCase();
        if (query === '' || content.includes(query)) {
            section.style.display = 'block';
        } else {
            section.style.display = 'none';
        }
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
</script>

<?php require_once 'includes/footer.php'; ?>