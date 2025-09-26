<?php
$page_title = "Gallery";
require_once 'includes/config.php';
require_once 'includes/header.php';
?>

<section class="hero">
    <div class="container">
        <div class="hero-content">
            <h1>Interactive Gallery</h1>
            <p>Explore 50+ professional chart types with live demos, GPU acceleration, VR/AR export, and real-time streaming</p>
            <div class="hero-actions">
                <a href="interactive-gallery.php" class="btn btn-primary btn-large">
                    <i class="fas fa-play"></i> Interactive Demo
                </a>
                <a href="https://pypi.org/project/vizlychart/" class="btn btn-outline btn-large" target="_blank">
                    <i class="fab fa-python"></i> Install Now
                </a>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="gallery-filters">
            <h3>Filter by Category</h3>
            <div class="filter-buttons">
                <button class="filter-btn active" onclick="filterCharts('all')">All Charts</button>
                <button class="filter-btn" onclick="filterCharts('basic')">Basic</button>
                <button class="filter-btn" onclick="filterCharts('advanced')">Advanced</button>
                <button class="filter-btn" onclick="filterCharts('financial')">Financial</button>
                <button class="filter-btn" onclick="filterCharts('engineering')">Engineering</button>
                <button class="filter-btn" onclick="filterCharts('datascience')">Data Science</button>
            </div>
        </div>

        <div class="charts-grid" id="charts-gallery">
            <!-- Basic Charts -->
            <div class="chart-item" data-category="basic">
                <div class="chart-preview">
                    <canvas id="line-chart-demo"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Line Chart</h4>
                    <p>High-performance line charts with optimized rendering and smooth animations.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Optimized</span>
                        <span class="feature-tag">Interactive</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('line')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="basic">
                <div class="chart-preview">
                    <canvas id="scatter-chart-demo"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Scatter Plot</h4>
                    <p>Efficient scatter plots for large datasets with optimized rendering performance.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Large Data</span>
                        <span class="feature-tag">Fast</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('scatter')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="basic">
                <div class="chart-preview">
                    <canvas id="bar-chart-demo"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Bar Chart</h4>
                    <p>Professional bar charts with customizable styling and animations.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Animated</span>
                        <span class="feature-tag">Responsive</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('bar')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="basic">
                <div class="chart-preview">
                    <canvas id="surface-chart-demo"></canvas>
                </div>
                <div class="chart-info">
                    <h4>3D Surface</h4>
                    <p>Interactive 3D surface plots with WebGL rendering and modern browser support.</p>
                    <div class="chart-features">
                        <span class="feature-tag">WebGL</span>
                        <span class="feature-tag">3D</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('surface')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <!-- Advanced Charts -->
            <div class="chart-item" data-category="advanced">
                <div class="chart-preview">
                    <canvas id="heatmap-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Heatmap</h4>
                    <p>Advanced correlation heatmaps with customizable color schemes and clustering.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Clustering</span>
                        <span class="feature-tag">Custom Colors</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('heatmap')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="advanced">
                <div class="chart-preview">
                    <canvas id="violin-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Violin Plot</h4>
                    <p>Statistical distribution visualization with kernel density estimation.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Statistical</span>
                        <span class="feature-tag">KDE</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('violin')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="advanced">
                <div class="chart-preview">
                    <canvas id="radar-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Radar Chart</h4>
                    <p>Multi-dimensional data visualization with customizable axes and styling.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Multi-dimensional</span>
                        <span class="feature-tag">Comparative</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('radar')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="advanced">
                <div class="chart-preview">
                    <canvas id="treemap-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Treemap</h4>
                    <p>Hierarchical data visualization with interactive drill-down capabilities.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Hierarchical</span>
                        <span class="feature-tag">Interactive</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('treemap')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <!-- Financial Charts -->
            <div class="chart-item" data-category="financial">
                <div class="chart-preview">
                    <canvas id="candlestick-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Candlestick</h4>
                    <p>Professional financial charts with OHLC data and technical indicators.</p>
                    <div class="chart-features">
                        <span class="feature-tag">OHLC</span>
                        <span class="feature-tag">Technical Analysis</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('candlestick')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="financial">
                <div class="chart-preview">
                    <canvas id="rsi-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>RSI Indicator</h4>
                    <p>Relative Strength Index with configurable periods and overbought/oversold levels.</p>
                    <div class="chart-features">
                        <span class="feature-tag">RSI</span>
                        <span class="feature-tag">Configurable</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('rsi')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="financial">
                <div class="chart-preview">
                    <canvas id="macd-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>MACD</h4>
                    <p>Moving Average Convergence Divergence with signal line and histogram.</p>
                    <div class="chart-features">
                        <span class="feature-tag">MACD</span>
                        <span class="feature-tag">Signal Line</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('macd')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="financial">
                <div class="chart-preview">
                    <canvas id="volume-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Volume Profile</h4>
                    <p>Advanced volume analysis with price-volume distribution and POC levels.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Volume Analysis</span>
                        <span class="feature-tag">POC</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('volume')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <!-- Engineering Charts -->
            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="bode-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Bode Plot</h4>
                    <p>Frequency response analysis with magnitude and phase plots for control systems.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Control Systems</span>
                        <span class="feature-tag">Frequency Response</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('bode')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="stress-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Stress-Strain</h4>
                    <p>Material testing visualization with yield point detection and modulus calculation.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Material Testing</span>
                        <span class="feature-tag">Yield Detection</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('stress')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="phase-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Phase Diagram</h4>
                    <p>Thermodynamic phase diagrams with critical points and phase boundaries.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Thermodynamics</span>
                        <span class="feature-tag">Critical Points</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('phase')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="fem-mesh-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>FEM Mesh</h4>
                    <p>Finite Element Analysis mesh visualization with stress contours and deformation.</p>
                    <div class="chart-features">
                        <span class="feature-tag">FEA</span>
                        <span class="feature-tag">Stress Analysis</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('fem')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="cfd-flow-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>CFD Flow Field</h4>
                    <p>Computational Fluid Dynamics with velocity vectors and pressure contours.</p>
                    <div class="chart-features">
                        <span class="feature-tag">CFD</span>
                        <span class="feature-tag">Fluid Flow</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('cfd')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="cad-model-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>CAD Model Viewer</h4>
                    <p>3D CAD model rendering from IGES, STEP, and STL files with interactive rotation.</p>
                    <div class="chart-features">
                        <span class="feature-tag">IGES/STEP</span>
                        <span class="feature-tag">3D Rendering</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('cad')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="vibration-mode-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Vibration Modes</h4>
                    <p>Modal analysis visualization with animated mode shapes and frequency response.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Modal Analysis</span>
                        <span class="feature-tag">Animation</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('vibration')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="thermal-analysis-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Thermal Analysis</h4>
                    <p>Heat transfer simulation with temperature gradients and thermal boundary conditions.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Heat Transfer</span>
                        <span class="feature-tag">Thermal Gradient</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('thermal')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="engineering">
                <div class="chart-preview">
                    <canvas id="contour-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Contour Plot</h4>
                    <p>2D contour plots for field visualization with customizable levels and colors.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Field Visualization</span>
                        <span class="feature-tag">Custom Levels</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('contour')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <!-- Data Science Charts -->
            <div class="chart-item" data-category="datascience">
                <div class="chart-preview">
                    <canvas id="distribution-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Distribution</h4>
                    <p>Statistical distribution analysis with multiple distribution fitting and testing.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Distribution Fitting</span>
                        <span class="feature-tag">Statistical Tests</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('distribution')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="datascience">
                <div class="chart-preview">
                    <canvas id="correlation-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Correlation Matrix</h4>
                    <p>Advanced correlation analysis with hierarchical clustering and significance testing.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Hierarchical Clustering</span>
                        <span class="feature-tag">Significance Testing</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('correlation')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="datascience">
                <div class="chart-preview">
                    <canvas id="regression-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Regression Analysis</h4>
                    <p>Multiple regression models with confidence intervals and residual analysis.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Multiple Models</span>
                        <span class="feature-tag">Confidence Intervals</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('regression')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>

            <div class="chart-item" data-category="datascience">
                <div class="chart-preview">
                    <canvas id="anomaly-chart-demo" width="300" height="200"></canvas>
                </div>
                <div class="chart-info">
                    <h4>Anomaly Detection</h4>
                    <p>Real-time anomaly detection with multiple algorithms and confidence scoring.</p>
                    <div class="chart-features">
                        <span class="feature-tag">Real-time</span>
                        <span class="feature-tag">Multiple Algorithms</span>
                    </div>
                    <button class="chart-demo-btn" onclick="showChartDemo('anomaly')">
                        <i class="fas fa-code"></i> View Code
                    </button>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section" id="live-demo" style="background: var(--bg-light-secondary);">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Live Interactive Demo</h2>
            <p class="section-subtitle">Try Vizly features directly in your browser</p>
        </div>

        <div class="demo-container">
            <div class="demo-controls">
                <h3>Choose Demo Type</h3>
                <div class="demo-buttons">
                    <button class="demo-btn active" onclick="runDemo('basic')">Basic Charts</button>
                    <button class="demo-btn" onclick="runDemo('gpu')">GPU Acceleration</button>
                    <button class="demo-btn" onclick="runDemo('vr')">VR/AR</button>
                    <button class="demo-btn" onclick="runDemo('streaming')">Real-time</button>
                </div>
            </div>

            <div class="demo-workspace">
                <div class="demo-code">
                    <div class="code-header">
                        <h4><i class="fas fa-code"></i> Python Code</h4>
                        <button class="copy-btn" onclick="copyToClipboard(document.getElementById('demo-code').textContent)">
                            <i class="fas fa-copy"></i> Copy
                        </button>
                    </div>
                    <pre id="demo-code">import vizlychart as vz

# Create high-performance line chart
fig = vz.Figure()
chart = vz.LineChart(fig)
chart.plot([1, 2, 3, 4], [1, 4, 2, 3])
fig.show()</pre>
                </div>

                <div class="demo-output">
                    <div class="output-header">
                        <h4><i class="fas fa-chart-line"></i> Live Output</h4>
                        <button class="refresh-btn" onclick="refreshDemo()">
                            <i class="fas fa-sync-alt"></i> Refresh
                        </button>
                    </div>
                    <div class="demo-chart">
                        <canvas id="live-demo-chart" width="600" height="400"></canvas>
                    </div>
                    <div class="demo-description">
                        <p id="demo-description">Basic line chart with GPU acceleration</p>
                    </div>
                </div>
            </div>

            <div class="performance-metrics">
                <div class="metric">
                    <span class="metric-label">Render Time</span>
                    <span class="metric-value" id="render-time">12ms</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Data Points</span>
                    <span class="metric-value" id="data-points">1,000</span>
                </div>
                <div class="metric">
                    <span class="metric-label">GPU Speedup</span>
                    <span class="metric-value" id="gpu-speedup">8x</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Memory Usage</span>
                    <span class="metric-value" id="memory-usage">2.4MB</span>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Performance Showcase</h2>
            <p class="section-subtitle">See Vizly's speed advantage in action</p>
        </div>

        <div class="performance-showcase">
            <div class="performance-comparison">
                <h3>Real-time GPU Performance Test</h3>
                <div class="performance-controls">
                    <label for="point-count">Data Points:</label>
                    <select id="point-count" onchange="updatePerformanceDemo()">
                        <option value="1000">1,000 points</option>
                        <option value="10000">10,000 points</option>
                        <option value="100000">100,000 points</option>
                        <option value="1000000">1,000,000 points</option>
                    </select>
                    <button class="run-test-btn" onclick="runPerformanceTest()">
                        <i class="fas fa-play"></i> Run Test
                    </button>
                </div>

                <div class="performance-results">
                    <div class="result-item cpu">
                        <h4><i class="fas fa-microchip"></i> CPU Rendering</h4>
                        <div class="time-display" id="cpu-time">--ms</div>
                        <div class="progress-bar">
                            <div class="progress-fill cpu-progress" id="cpu-progress"></div>
                        </div>
                    </div>

                    <div class="result-item optimized">
                        <h4><i class="fas fa-rocket"></i> GPU Rendering</h4>
                        <div class="time-display" id="gpu-time">--ms</div>
                        <div class="progress-bar">
                            <div class="progress-fill gpu-progress" id="gpu-progress"></div>
                        </div>
                    </div>

                    <div class="speedup-indicator">
                        <span class="speedup-label">GPU Speedup:</span>
                        <span class="speedup-value" id="speedup-value">--x</span>
                    </div>
                </div>
            </div>

            <div class="performance-chart">
                <canvas id="performance-benchmark-chart" width="500" height="300"></canvas>
            </div>
        </div>
    </div>
</section>

<section class="section" style="background: var(--gradient-primary); color: white;">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title" style="color: white;">Ready to Get Started?</h2>
            <p class="section-subtitle" style="color: rgba(255,255,255,0.9);">
                Install Vizly now and start creating professional visualizations
            </p>
        </div>

        <div class="get-started-grid">
            <div class="install-option">
                <div class="install-icon">
                    <i class="fab fa-python"></i>
                </div>
                <h3>Python (PyPI)</h3>
                <div class="install-command">
                    <code>pip install vizlychart</code>
                    <button onclick="copyToClipboard('pip install vizlychart')" class="copy-install-btn">
                        <i class="fas fa-copy"></i>
                    </button>
                </div>
                <p>Complete feature set with GPU acceleration and VR/AR support</p>
                <a href="https://pypi.org/project/vizly/" class="btn btn-secondary" target="_blank">
                    <i class="fab fa-python"></i> Install Now
                </a>
            </div>

            <div class="install-option">
                <div class="install-icon">
                    <i class="fab fa-microsoft"></i>
                </div>
                <h3>C# (.NET)</h3>
                <div class="install-command">
                    <code>dotnet add package Vizly.SDK</code>
                    <button onclick="copyToClipboard('dotnet add package Vizly.SDK')" class="copy-install-btn">
                        <i class="fas fa-copy"></i>
                    </button>
                </div>
                <p>Native .NET integration with async support and enterprise features</p>
                <a href="contact.php" class="btn btn-outline">
                    <i class="fas fa-envelope"></i> Request Access
                </a>
            </div>

            <div class="install-option">
                <div class="install-icon">
                    <i class="fas fa-terminal"></i>
                </div>
                <h3>C++</h3>
                <div class="install-command">
                    <code>cmake -DVIZLY_SDK=ON</code>
                    <button onclick="copyToClipboard('cmake -DVIZLY_SDK=ON')" class="copy-install-btn">
                        <i class="fas fa-copy"></i>
                    </button>
                </div>
                <p>High-performance native library with zero-overhead abstractions</p>
                <a href="contact.php" class="btn btn-outline">
                    <i class="fas fa-envelope"></i> Request Access
                </a>
            </div>

            <div class="install-option">
                <div class="install-icon">
                    <i class="fab fa-java"></i>
                </div>
                <h3>Java</h3>
                <div class="install-command">
                    <code>&lt;artifactId&gt;vizly-sdk&lt;/artifactId&gt;</code>
                    <button onclick="copyToClipboard('<artifactId>vizly-sdk</artifactId>')" class="copy-install-btn">
                        <i class="fas fa-copy"></i>
                    </button>
                </div>
                <p>Enterprise Java integration with Spring Boot and Maven support</p>
                <a href="contact.php" class="btn btn-outline">
                    <i class="fas fa-envelope"></i> Request Access
                </a>
            </div>
        </div>

        <div class="quick-start-links">
            <a href="documentation.php" class="quick-link">
                <i class="fas fa-book"></i> Documentation
            </a>
            <a href="features.php" class="quick-link">
                <i class="fas fa-list"></i> Full Feature List
            </a>
            <a href="pricing.php" class="quick-link">
                <i class="fas fa-calculator"></i> Pricing
            </a>
            <a href="contact.php" class="quick-link">
                <i class="fas fa-envelope"></i> Enterprise Sales
            </a>
        </div>
    </div>
</section>

<!-- Chart Demo Modal -->
<div id="chart-modal" class="modal">
    <div class="modal-content">
        <div class="modal-header">
            <h3 id="modal-title">Chart Demo</h3>
            <button class="modal-close" onclick="closeModal()">&times;</button>
        </div>
        <div class="modal-body">
            <div class="modal-code">
                <h4>Python Code</h4>
                <pre id="modal-code"></pre>
                <button class="copy-modal-btn" onclick="copyModalCode()">
                    <i class="fas fa-copy"></i> Copy Code
                </button>
            </div>
            <div class="modal-features">
                <h4>Key Features</h4>
                <ul id="modal-features-list"></ul>
            </div>
        </div>
    </div>
</div>

<style>
.gallery-filters {
    text-align: center;
    margin-bottom: 3rem;
}

.gallery-filters h3 {
    margin-bottom: 1.5rem;
    color: var(--text-light);
}

.filter-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.filter-btn {
    padding: 0.75rem 1.5rem;
    border: 2px solid var(--primary-color);
    background: transparent;
    color: var(--primary-color);
    border-radius: 2rem;
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition-fast);
}

.filter-btn:hover,
.filter-btn.active {
    background: var(--primary-color);
    color: white;
}

.charts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.chart-item {
    background: white;
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
    transition: var(--transition-normal);
    border: 1px solid rgba(0,0,0,0.05);
}

.chart-item:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-xl);
}

.chart-preview {
    background: var(--bg-light-secondary);
    padding: 1rem;
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-bottom: 1px solid rgba(0,0,0,0.05);
}

.chart-info {
    padding: 1.5rem;
}

.chart-info h4 {
    margin-bottom: 0.75rem;
    color: var(--text-light);
}

.chart-info p {
    color: var(--text-light-secondary);
    margin-bottom: 1rem;
    font-size: var(--font-size-sm);
    line-height: 1.5;
}

.chart-features {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}

.feature-tag {
    background: var(--gradient-success);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: var(--font-size-xs);
    font-weight: 500;
}

.chart-demo-btn {
    background: var(--gradient-primary);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition-fast);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.chart-demo-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.demo-container {
    background: white;
    border-radius: 1rem;
    padding: 2rem;
    box-shadow: var(--shadow-lg);
}

.demo-controls {
    text-align: center;
    margin-bottom: 2rem;
}

.demo-controls h3 {
    margin-bottom: 1rem;
    color: var(--text-light);
}

.demo-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.demo-btn {
    padding: 0.75rem 1.5rem;
    border: 2px solid var(--primary-color);
    background: transparent;
    color: var(--primary-color);
    border-radius: 0.5rem;
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition-fast);
}

.demo-btn:hover,
.demo-btn.active {
    background: var(--primary-color);
    color: white;
}

.demo-workspace {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin-bottom: 2rem;
}

.demo-code,
.demo-output {
    border-radius: 0.5rem;
    overflow: hidden;
    border: 1px solid var(--bg-light-secondary);
}

.code-header,
.output-header {
    background: var(--gradient-primary);
    color: white;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.code-header h4,
.output-header h4 {
    margin: 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.copy-btn,
.refresh-btn {
    background: rgba(255,255,255,0.2);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    cursor: pointer;
    transition: var(--transition-fast);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.copy-btn:hover,
.refresh-btn:hover {
    background: rgba(255,255,255,0.3);
}

#demo-code {
    background: var(--bg-dark);
    color: var(--text-dark);
    padding: 1.5rem;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: var(--font-size-sm);
    margin: 0;
    min-height: 200px;
    overflow-x: auto;
}

.demo-chart {
    padding: 1rem;
    background: var(--bg-light-secondary);
    height: 400px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.demo-description {
    padding: 1rem;
    background: white;
    border-top: 1px solid var(--bg-light-secondary);
}

.performance-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    padding: 1.5rem;
    background: var(--bg-light-secondary);
    border-radius: 0.5rem;
}

.metric {
    text-align: center;
    padding: 1rem;
    background: white;
    border-radius: 0.5rem;
    box-shadow: var(--shadow-sm);
}

.metric-label {
    display: block;
    font-size: var(--font-size-sm);
    color: var(--text-light-secondary);
    margin-bottom: 0.5rem;
}

.metric-value {
    display: block;
    font-size: var(--font-size-xl);
    font-weight: 700;
    color: var(--primary-color);
}

.performance-showcase {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: start;
}

.performance-comparison {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
}

.performance-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
    align-items: center;
    flex-wrap: wrap;
}

.performance-controls label {
    font-weight: 500;
    color: var(--text-light);
}

.performance-controls select {
    padding: 0.5rem;
    border: 1px solid var(--bg-light-secondary);
    border-radius: 0.25rem;
    background: white;
}

.run-test-btn {
    background: var(--gradient-success);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    font-weight: 500;
    cursor: pointer;
    transition: var(--transition-fast);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.run-test-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.performance-results {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.result-item {
    padding: 1.5rem;
    border-radius: 0.5rem;
    border: 2px solid transparent;
}

.result-item.cpu {
    background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
    border-color: var(--danger-color);
}

.result-item.gpu {
    background: var(--gradient-success);
    border-color: var(--secondary-color);
    color: white;
}

.result-item h4 {
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.time-display {
    font-size: var(--font-size-2xl);
    font-weight: 700;
    margin-bottom: 1rem;
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: rgba(0,0,0,0.2);
    border-radius: 4px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 1s ease;
}

.cpu-progress {
    background: var(--danger-color);
}

.gpu-progress {
    background: white;
}

.speedup-indicator {
    text-align: center;
    padding: 1rem;
    background: var(--gradient-primary);
    color: white;
    border-radius: 0.5rem;
    font-size: var(--font-size-lg);
    font-weight: 600;
}

.speedup-value {
    color: var(--accent-color);
    font-size: var(--font-size-2xl);
    margin-left: 0.5rem;
}

.performance-chart {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: var(--shadow-lg);
}

.get-started-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.install-option {
    background: rgba(255,255,255,0.1);
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    transition: var(--transition-normal);
}

.install-option:hover {
    background: rgba(255,255,255,0.15);
    transform: translateY(-5px);
}

.install-icon {
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

.install-option h3 {
    color: white;
    margin-bottom: 1rem;
}

.install-command {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(0,0,0,0.3);
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
}

.install-command code {
    flex: 1;
    background: none;
    color: var(--accent-color);
    font-size: var(--font-size-sm);
}

.copy-install-btn {
    background: rgba(255,255,255,0.2);
    color: white;
    border: none;
    padding: 0.5rem;
    border-radius: 0.25rem;
    cursor: pointer;
    transition: var(--transition-fast);
}

.copy-install-btn:hover {
    background: rgba(255,255,255,0.3);
}

.install-option p {
    color: rgba(255,255,255,0.9);
    margin-bottom: 1.5rem;
    font-size: var(--font-size-sm);
}

.quick-start-links {
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.2);
}

.quick-link {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: rgba(255,255,255,0.9);
    text-decoration: none;
    transition: var(--transition-fast);
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
}

.quick-link:hover {
    color: white;
    background: rgba(255,255,255,0.1);
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    z-index: 10000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    backdrop-filter: blur(5px);
}

.modal-content {
    background: white;
    margin: 5% auto;
    border-radius: 1rem;
    width: 90%;
    max-width: 800px;
    max-height: 80vh;
    overflow-y: auto;
    box-shadow: var(--shadow-xl);
}

.modal-header {
    background: var(--gradient-primary);
    color: white;
    padding: 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 1rem 1rem 0 0;
}

.modal-header h3 {
    margin: 0;
}

.modal-close {
    background: none;
    border: none;
    color: white;
    font-size: 2rem;
    cursor: pointer;
    padding: 0;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: var(--transition-fast);
}

.modal-close:hover {
    background: rgba(255,255,255,0.2);
}

.modal-body {
    padding: 2rem;
}

.modal-code {
    margin-bottom: 2rem;
}

.modal-code h4 {
    margin-bottom: 1rem;
    color: var(--text-light);
}

.modal-code pre {
    background: var(--bg-dark);
    color: var(--text-dark);
    padding: 1.5rem;
    border-radius: 0.5rem;
    overflow-x: auto;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: var(--font-size-sm);
    margin-bottom: 1rem;
}

.copy-modal-btn {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: var(--transition-fast);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.copy-modal-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.modal-features h4 {
    margin-bottom: 1rem;
    color: var(--text-light);
}

.modal-features ul {
    list-style: none;
    padding: 0;
}

.modal-features li {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
    color: var(--text-light-secondary);
}

.modal-features li::before {
    content: '✓';
    color: var(--secondary-color);
    font-weight: bold;
    width: 16px;
}

@media (prefers-color-scheme: dark) {
    .chart-item,
    .demo-container,
    .performance-comparison,
    .performance-chart,
    .modal-content {
        background: var(--bg-dark-secondary);
        border: 1px solid rgba(255,255,255,0.05);
    }

    .chart-preview,
    .demo-chart {
        background: var(--bg-dark);
    }

    .chart-info h4,
    .gallery-filters h3,
    .demo-controls h3 {
        color: var(--text-dark);
    }

    .performance-controls label {
        color: var(--text-dark);
    }

    .performance-controls select {
        background: var(--bg-dark);
        border-color: rgba(255,255,255,0.1);
        color: var(--text-dark);
    }

    .modal-code h4,
    .modal-features h4 {
        color: var(--text-dark);
    }

    .performance-metrics {
        background: var(--bg-dark);
    }

    .metric {
        background: var(--bg-dark-secondary);
    }
}

@media (max-width: 768px) {
    .charts-grid {
        grid-template-columns: 1fr;
    }

    .demo-workspace {
        grid-template-columns: 1fr;
    }

    .performance-showcase {
        grid-template-columns: 1fr;
    }

    .performance-controls {
        flex-direction: column;
        align-items: stretch;
    }

    .get-started-grid {
        grid-template-columns: 1fr;
    }

    .quick-start-links {
        flex-direction: column;
        align-items: center;
    }

    .modal-content {
        margin: 2% auto;
        width: 95%;
        max-height: 95vh;
    }

    .modal-body {
        padding: 1rem;
    }
}
</style>

<script>
// Gallery Charts - Simplified approach
document.addEventListener('DOMContentLoaded', function() {
    console.log('Gallery: DOM loaded');
    console.log('Gallery: Chart.js available:', typeof Chart !== 'undefined');

    // Multiple attempts to initialize charts
    attemptChartInitialization();
});

function attemptChartInitialization() {
    if (typeof Chart !== 'undefined') {
        console.log('Gallery: Initializing charts immediately');
        initializeGalleryCharts();
    } else {
        console.log('Gallery: Chart.js not ready, retrying in 500ms');
        setTimeout(() => {
            if (typeof Chart !== 'undefined') {
                console.log('Gallery: Chart.js now available, initializing');
                initializeGalleryCharts();
            } else {
                console.log('Gallery: Chart.js still not available, retrying in 1000ms');
                setTimeout(() => {
                    if (typeof Chart !== 'undefined') {
                        initializeGalleryCharts();
                    } else {
                        console.error('Gallery: Chart.js failed to load after multiple attempts');
                        // Show fallback message
                        showChartFallback();
                    }
                }, 1000);
            }
        }, 500);
    }
}

function initializeGalleryCharts() {
    console.log('Gallery: Starting chart initialization');

    // Line Chart
    createChart('line-chart-demo', {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                data: [12, 19, 3, 5, 2, 3],
                borderColor: 'rgb(37, 99, 235)',
                backgroundColor: 'rgba(37, 99, 235, 0.1)',
                tension: 0.4,
                fill: true,
                pointRadius: 0
            }]
        }
    });

    // Scatter Chart
    const scatterData = Array.from({length: 30}, () => ({
        x: Math.random() * 100,
        y: Math.random() * 100
    }));

    createChart('scatter-chart-demo', {
        type: 'scatter',
        data: {
            datasets: [{
                data: scatterData,
                backgroundColor: 'rgba(16, 185, 129, 0.6)',
                pointRadius: 4
            }]
        }
    });

    // Bar Chart
    createChart('bar-chart-demo', {
        type: 'bar',
        data: {
            labels: ['A', 'B', 'C', 'D', 'E'],
            datasets: [{
                data: [12, 19, 3, 5, 2],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(255, 205, 86, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)'
                ],
                borderRadius: 4
            }]
        }
    });

    // Surface Chart (using line chart as fallback)
    createChart('surface-chart-demo', {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5', '6'],
            datasets: [{
                data: [5, 10, 5, 2, 20, 30],
                borderColor: 'rgb(255, 99, 132)',
                backgroundColor: 'rgba(255, 99, 132, 0.1)',
                tension: 0.4,
                fill: true,
                pointRadius: 0
            }, {
                data: [15, 25, 12, 8, 30, 40],
                borderColor: 'rgb(54, 162, 235)',
                backgroundColor: 'rgba(54, 162, 235, 0.1)',
                tension: 0.4,
                fill: true,
                pointRadius: 0
            }]
        }
    });

    // Heatmap Chart (using multiple datasets for gradient colors)
    const gridSize = 5;
    const heatmapMatrix = [];
    const heatmapDatasets = [];

    // Generate correlation matrix
    for (let row = 0; row < gridSize; row++) {
        heatmapMatrix[row] = [];
        for (let col = 0; col < gridSize; col++) {
            heatmapMatrix[row][col] = row === col ? 1.0 : Math.random() * 0.8 + 0.1;
        }
    }

    // Function to get color based on value
    function getHeatmapColor(value) {
        // Blue to Red gradient
        const red = Math.floor(255 * value);
        const blue = Math.floor(255 * (1 - value));
        const green = Math.floor(100 * (1 - Math.abs(value - 0.5) * 2));
        return `rgba(${red}, ${green}, ${blue}, 0.8)`;
    }

    // Create data points with pre-calculated colors
    const heatmapPoints = [];
    const backgroundColors = [];
    const borderColors = [];

    for (let row = 0; row < gridSize; row++) {
        for (let col = 0; col < gridSize; col++) {
            const value = heatmapMatrix[row][col];
            heatmapPoints.push({
                x: col,
                y: gridSize - 1 - row,
                v: value // Store value for tooltip
            });

            const color = getHeatmapColor(value);
            backgroundColors.push(color);
            borderColors.push(color.replace('0.8', '1.0'));
        }
    }

    createChart('heatmap-chart-demo', {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Correlation',
                data: heatmapPoints,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
                pointRadius: 22, // Large squares for heatmap effect
                pointHoverRadius: 26,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Correlation Heatmap',
                    color: '#ffffff'
                },
                tooltip: {
                    callbacks: {
                        title: function(context) {
                            const x = context[0].parsed.x;
                            const y = context[0].parsed.y;
                            const xLabels = ['Revenue', 'Users', 'Growth', 'Costs', 'ROI'];
                            const yLabels = ['ROI', 'Costs', 'Growth', 'Users', 'Revenue'];
                            return `${yLabels[y]} vs ${xLabels[x]}`;
                        },
                        label: function(context) {
                            const value = context.raw.v;
                            return `Correlation: ${value.toFixed(3)}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    min: -0.5,
                    max: gridSize - 0.5,
                    ticks: {
                        stepSize: 1,
                        callback: function(value) {
                            const labels = ['Revenue', 'Users', 'Growth', 'Costs', 'ROI'];
                            return labels[value] || '';
                        },
                        color: '#ffffff'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                },
                y: {
                    type: 'linear',
                    min: -0.5,
                    max: gridSize - 0.5,
                    ticks: {
                        stepSize: 1,
                        callback: function(value) {
                            const labels = ['ROI', 'Costs', 'Growth', 'Users', 'Revenue'];
                            return labels[value] || '';
                        },
                        color: '#ffffff'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                }
            },
            interaction: {
                intersect: false
            }
        }
    });

    // Violin Chart (using line chart)
    createChart('violin-chart-demo', {
        type: 'line',
        data: {
            labels: ['A', 'B', 'C', 'D'],
            datasets: [{
                data: [2, 5, 3, 1],
                borderColor: 'rgb(153, 102, 255)',
                backgroundColor: 'rgba(153, 102, 255, 0.1)',
                tension: 0.6,
                fill: true,
                pointRadius: 0
            }]
        }
    });

    // Radar Chart
    createChart('radar-chart-demo', {
        type: 'radar',
        data: {
            labels: ['Speed', 'Memory', 'GPU', 'CPU', 'Network'],
            datasets: [{
                data: [80, 90, 85, 75, 95],
                borderColor: 'rgb(255, 205, 86)',
                backgroundColor: 'rgba(255, 205, 86, 0.2)',
                pointRadius: 0
            }]
        }
    });

    // Treemap Chart (using bar chart)
    createChart('treemap-chart-demo', {
        type: 'bar',
        data: {
            labels: ['A', 'B', 'C', 'D'],
            datasets: [{
                data: [40, 30, 20, 10],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(255, 205, 86, 0.8)',
                    'rgba(75, 192, 192, 0.8)'
                ]
            }]
        }
    });

    // Candlestick Chart (using line chart)
    createChart('candlestick-chart-demo', {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5'],
            datasets: [{
                data: [10, 15, 8, 20, 12],
                borderColor: 'rgb(34, 197, 94)',
                backgroundColor: 'rgba(34, 197, 94, 0.1)',
                tension: 0,
                pointRadius: 0
            }]
        }
    });

    // RSI Chart
    createChart('rsi-chart-demo', {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5', '6'],
            datasets: [{
                data: [30, 45, 70, 25, 80, 50],
                borderColor: 'rgb(239, 68, 68)',
                backgroundColor: 'rgba(239, 68, 68, 0.1)',
                tension: 0.4,
                pointRadius: 0
            }]
        }
    });

    // MACD Chart
    createChart('macd-chart-demo', {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5'],
            datasets: [{
                data: [1, -2, 3, -1, 2],
                borderColor: 'rgb(59, 130, 246)',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                tension: 0.4,
                pointRadius: 0
            }]
        }
    });

    // Volume Chart
    createChart('volume-chart-demo', {
        type: 'bar',
        data: {
            labels: ['1', '2', '3', '4'],
            datasets: [{
                data: [1000, 2000, 1500, 3000],
                backgroundColor: 'rgba(168, 85, 247, 0.8)'
            }]
        }
    });

    // Correlation Chart
    createChart('correlation-chart-demo', {
        type: 'scatter',
        data: {
            datasets: [{
                data: Array.from({length: 15}, () => ({
                    x: Math.random() * 10,
                    y: Math.random() * 10
                })),
                backgroundColor: 'rgba(251, 146, 60, 0.6)',
                pointRadius: 4
            }]
        }
    });

    // Distribution Chart
    createChart('distribution-chart-demo', {
        type: 'bar',
        data: {
            labels: ['0-10', '10-20', '20-30', '30-40', '40-50'],
            datasets: [{
                data: [5, 15, 25, 15, 5],
                backgroundColor: 'rgba(14, 165, 233, 0.8)'
            }]
        }
    });

    // Regression Chart
    createChart('regression-chart-demo', {
        type: 'scatter',
        data: {
            datasets: [{
                data: Array.from({length: 10}, (_, i) => ({
                    x: i,
                    y: i * 2 + Math.random() * 3
                })),
                backgroundColor: 'rgba(236, 72, 153, 0.6)',
                pointRadius: 4
            }]
        }
    });

    // Anomaly Chart
    createChart('anomaly-chart-demo', {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5', '6'],
            datasets: [{
                data: [5, 5, 5, 15, 5, 5],
                borderColor: 'rgb(220, 38, 127)',
                backgroundColor: 'rgba(220, 38, 127, 0.1)',
                tension: 0.4,
                pointRadius: function(context) {
                    return context.parsed.y > 10 ? 8 : 0;
                }
            }]
        }
    });

    // Contour Chart (using line chart)
    createChart('contour-chart-demo', {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5'],
            datasets: Array.from({length: 3}, (_, i) => ({
                data: Array.from({length: 5}, () => Math.random() * 10),
                borderColor: `hsl(${i * 120}, 70%, 50%)`,
                backgroundColor: `hsla(${i * 120}, 70%, 50%, 0.1)`,
                tension: 0.6,
                fill: false,
                pointRadius: 0
            }))
        }
    });

    // Bode Chart
    createChart('bode-chart-demo', {
        type: 'line',
        data: {
            labels: ['0.1', '1', '10', '100', '1000'],
            datasets: [{
                data: [0, -20, -40, -60, -80],
                borderColor: 'rgb(34, 197, 94)',
                backgroundColor: 'rgba(34, 197, 94, 0.1)',
                tension: 0.4,
                pointRadius: 0
            }]
        }
    });

    // Phase Chart
    createChart('phase-chart-demo', {
        type: 'line',
        data: {
            labels: ['0.1', '1', '10', '100', '1000'],
            datasets: [{
                data: [0, -45, -90, -135, -180],
                borderColor: 'rgb(168, 85, 247)',
                backgroundColor: 'rgba(168, 85, 247, 0.1)',
                tension: 0.4,
                pointRadius: 0
            }]
        }
    });

    // Stress Chart
    createChart('stress-chart-demo', {
        type: 'line',
        data: {
            labels: ['0', '0.1', '0.2', '0.3', '0.4'],
            datasets: [{
                data: [0, 50, 100, 150, 120],
                borderColor: 'rgb(239, 68, 68)',
                backgroundColor: 'rgba(239, 68, 68, 0.1)',
                tension: 0.4,
                pointRadius: 0
            }]
        }
    });

    // FEM Mesh Chart
    createChart('fem-mesh-demo', {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Nodes',
                data: Array.from({length: 50}, () => ({
                    x: Math.random() * 10,
                    y: Math.random() * 10
                })),
                backgroundColor: function(context) {
                    const stress = Math.random();
                    const red = Math.floor(255 * stress);
                    const blue = Math.floor(255 * (1 - stress));
                    return `rgba(${red}, 100, ${blue}, 0.8)`;
                },
                pointRadius: 4,
                showLine: false
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'FEM Stress Distribution',
                    color: '#ffffff'
                },
                legend: { display: false }
            },
            scales: {
                x: {
                    title: { display: true, text: 'X Position (mm)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                },
                y: {
                    title: { display: true, text: 'Y Position (mm)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                }
            }
        }
    });

    // CFD Flow Field Chart
    createChart('cfd-flow-demo', {
        type: 'line',
        data: {
            labels: ['Inlet', 'Expansion', 'Throat', 'Diffuser', 'Outlet'],
            datasets: [{
                label: 'Velocity (m/s)',
                data: [10, 8, 25, 15, 12],
                borderColor: 'rgb(34, 197, 94)',
                backgroundColor: 'rgba(34, 197, 94, 0.2)',
                tension: 0.4,
                fill: true
            }, {
                label: 'Pressure (Pa)',
                data: [101325, 98000, 85000, 95000, 101000],
                borderColor: 'rgb(239, 68, 68)',
                backgroundColor: 'rgba(239, 68, 68, 0.2)',
                tension: 0.4,
                yAxisID: 'pressure'
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'CFD Analysis - Nozzle Flow',
                    color: '#ffffff'
                }
            },
            scales: {
                y: {
                    title: { display: true, text: 'Velocity (m/s)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                },
                pressure: {
                    type: 'linear',
                    position: 'right',
                    title: { display: true, text: 'Pressure (Pa)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { display: false }
                },
                x: {
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                }
            }
        }
    });

    // CAD Model Viewer (3D representation)
    createChart('cad-model-demo', {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'CAD Model Points',
                data: [
                    {x: 0, y: 0}, {x: 2, y: 0}, {x: 2, y: 2}, {x: 0, y: 2},
                    {x: 0.5, y: 0.5}, {x: 1.5, y: 0.5}, {x: 1.5, y: 1.5}, {x: 0.5, y: 1.5}
                ],
                backgroundColor: 'rgba(34, 197, 94, 0.8)',
                borderColor: 'rgb(34, 197, 94)',
                pointRadius: 6,
                showLine: true,
                borderWidth: 2
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'CAD Model - IGES Import',
                    color: '#ffffff'
                },
                legend: { display: false }
            },
            scales: {
                x: {
                    title: { display: true, text: 'X (mm)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                },
                y: {
                    title: { display: true, text: 'Y (mm)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                }
            }
        }
    });

    // Vibration Modes Chart
    createChart('vibration-mode-demo', {
        type: 'line',
        data: {
            labels: ['0', '0.2', '0.4', '0.6', '0.8', '1.0'],
            datasets: [{
                label: 'Mode 1 (50 Hz)',
                data: [0, 0.8, 1.0, 0.8, 0, -0.5],
                borderColor: 'rgb(59, 130, 246)',
                backgroundColor: 'rgba(59, 130, 246, 0.2)',
                tension: 0.4,
                fill: false
            }, {
                label: 'Mode 2 (120 Hz)',
                data: [0, -0.5, 0, 0.5, 0, -0.3],
                borderColor: 'rgb(239, 68, 68)',
                backgroundColor: 'rgba(239, 68, 68, 0.2)',
                tension: 0.4,
                fill: false
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Modal Analysis - Beam Vibration',
                    color: '#ffffff'
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Position (L)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                },
                y: {
                    title: { display: true, text: 'Amplitude', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                }
            }
        }
    });

    // Thermal Analysis Chart
    createChart('thermal-analysis-demo', {
        type: 'line',
        data: {
            labels: ['Surface', '1mm', '2mm', '3mm', '4mm', 'Center'],
            datasets: [{
                label: 'Temperature (°C)',
                data: [100, 85, 70, 55, 40, 25],
                borderColor: 'rgb(239, 68, 68)',
                backgroundColor: function(context) {
                    const temp = context.parsed.y;
                    const intensity = (temp - 25) / 75; // Normalize 25-100°C to 0-1
                    return `rgba(255, ${Math.floor(165 * (1 - intensity))}, 0, 0.6)`;
                },
                tension: 0.4,
                fill: true,
                pointBackgroundColor: function(context) {
                    const temp = context.parsed.y;
                    const intensity = (temp - 25) / 75;
                    return `rgba(255, ${Math.floor(165 * (1 - intensity))}, 0, 1.0)`;
                }
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Thermal Analysis - Heat Conduction',
                    color: '#ffffff'
                },
                legend: { display: false }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Distance from Surface', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                },
                y: {
                    title: { display: true, text: 'Temperature (°C)', color: '#ffffff' },
                    ticks: { color: '#ffffff' },
                    grid: { color: 'rgba(255, 255, 255, 0.1)' }
                }
            }
        }
    });

    console.log('Gallery: Chart initialization completed');
}

function createChart(canvasId, config) {
    try {
        const canvas = document.getElementById(canvasId);
        if (!canvas) {
            console.warn('Gallery: Canvas element not found for', canvasId);
            return;
        }

        // Verify canvas context is available
        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.error('Gallery: Cannot get 2D context for', canvasId);
            return;
        }

        console.log('Gallery: Creating chart for', canvasId, 'canvas size:', canvas.width, 'x', canvas.height);

            // Set default options with GPU acceleration disabled for compatibility
            const defaultOptions = {
                responsive: true,
                maintainAspectRatio: false,
                devicePixelRatio: 1, // Disable high DPI for better compatibility
                plugins: {
                    legend: { display: false },
                    tooltip: { enabled: false }
                },
                scales: {
                    x: { display: false },
                    y: { display: false }
                },
                interaction: {
                    intersect: false
                },
                elements: {
                    point: {
                        hoverRadius: 0
                    }
                },
                animation: {
                    duration: 0 // Disable animations to prevent GPU issues
                }
            };

            // Merge with existing options instead of replacing
            config.options = Object.assign({}, defaultOptions, config.options || {});

            new Chart(canvas, config);
            console.log('Gallery: Successfully created chart for', canvasId);
    } catch (error) {
        console.error('Gallery: Error creating chart for', canvasId, error);
    }
}

function showChartFallback() {
    console.log('Gallery: Showing fallback for charts');
    const chartPreviews = document.querySelectorAll('.chart-preview canvas');
    chartPreviews.forEach(canvas => {
        const parent = canvas.parentElement;
        parent.innerHTML = '<div style="display: flex; align-items: center; justify-content: center; height: 100%; color: #666; font-size: 14px;">Chart Preview</div>';
    });
}

function initializeLiveDemo() {
    createChart('live-demo-chart', {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4'],
            datasets: [{
                label: 'Sample Data',
                data: [1, 4, 2, 3],
                borderColor: 'rgb(37, 99, 235)',
                backgroundColor: 'rgba(37, 99, 235, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top' }
            }
        }
    });
}

function initializePerformanceBenchmark() {
    createChart('performance-benchmark-chart', {
        type: 'bar',
        data: {
            labels: ['Small', 'Medium', 'Large', 'Very Large'],
            datasets: [{
                label: 'Standard',
                data: [20, 100, 500, 2000],
                backgroundColor: 'rgba(239, 68, 68, 0.8)'
            }, {
                label: 'Optimized',
                data: [15, 60, 200, 800],
                backgroundColor: 'rgba(37, 99, 235, 0.8)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top' }
            },
            scales: {
                y: {
                    title: { display: true, text: 'Time (ms)' }
                }
            }
        }
    });
}

function filterCharts(category) {
    const charts = document.querySelectorAll('.chart-item');
    const buttons = document.querySelectorAll('.filter-btn');

    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    charts.forEach(chart => {
        if (category === 'all' || chart.dataset.category === category) {
            chart.style.display = 'block';
        } else {
            chart.style.display = 'none';
        }
    });
}

function showChartDemo(chartType) {
    const modal = document.getElementById('chart-modal');
    const title = document.getElementById('modal-title');
    const code = document.getElementById('modal-code');
    const features = document.getElementById('modal-features-list');

    const demos = {
        line: {
            title: 'Line Chart Demo',
            code: `import vizlychart as vz

# Create GPU-accelerated line chart
import vizlychart as vz

fig = vz.Figure(gpu=True)
chart = vz.LineChart(fig)

# Plot with GPU acceleration
x = [1, 2, 3, 4, 5]
y = [1, 4, 2, 3, 5]
chart.plot(x, y, style='smooth', alpha=0.8)

# Customize appearance
chart.set_title('GPU-Accelerated Line Chart')
chart.set_theme('professional')

# Export or display
fig.show()`,
            features: [
                'GPU acceleration for large datasets',
                'Smooth curve interpolation',
                'Professional styling themes',
                'Interactive zoom and pan',
                'Export to multiple formats'
            ]
        },
        scatter: {
            title: 'Scatter Plot Demo',
            code: `import vizlychart as vz
import numpy as np

# Create scatter plot with 1M points
fig = vz.Figure(gpu=True)
chart = vz.ScatterChart(fig)

# Generate large dataset
n_points = 1_000_000
x = np.random.randn(n_points)
y = np.random.randn(n_points)

# Plot with GPU acceleration (renders in <100ms)
chart.scatter(x, y, alpha=0.6, size=2)
chart.set_title(f'Scatter Plot - {n_points:,} Points')

fig.show()`,
            features: [
                'Handle millions of points',
                '50x GPU speedup',
                'Alpha blending for density visualization',
                'Automatic point size optimization',
                'Memory-efficient rendering'
            ]
        },
        heatmap: {
            title: 'Heatmap Demo',
            code: `import vizlychart as vz
import numpy as np

# Create correlation heatmap
fig = vz.Figure(gpu=True)
chart = vz.HeatmapChart(fig)

# Generate correlation matrix
features = ['Revenue', 'Customers', 'Marketing', 'Support', 'Growth']
n_features = len(features)
correlation_matrix = np.random.rand(n_features, n_features)

# Make symmetric (correlation property)
correlation_matrix = (correlation_matrix + correlation_matrix.T) / 2
np.fill_diagonal(correlation_matrix, 1.0)

# Create heatmap with custom colormap
chart.heatmap(
    correlation_matrix,
    labels=features,
    colormap='RdBu_r',  # Red-Blue reversed
    show_values=True,
    cluster=True
)

chart.set_title('Feature Correlation Heatmap')
fig.show()`,
            features: [
                'Automatic clustering for pattern discovery',
                'Custom color schemes (RdBu, viridis, etc.)',
                'Value annotations with smart formatting',
                'Interactive hover for detailed values',
                'Export to high-resolution formats'
            ]
        },
        violin: {
            title: 'Violin Plot Demo',
            code: `import vizlychart as vz
import numpy as np

# Create violin plot for distribution analysis
fig = vz.Figure(gpu=True)
chart = vz.ViolinChart(fig)

# Generate sample data
categories = ['Group A', 'Group B', 'Group C', 'Group D']
data = []
for i, cat in enumerate(categories):
    # Different distributions for each group
    if i == 0:
        values = np.random.normal(50, 10, 1000)
    elif i == 1:
        values = np.random.exponential(15, 1000)
    elif i == 2:
        values = np.concatenate([
            np.random.normal(30, 5, 500),
            np.random.normal(70, 8, 500)
        ])
    else:
        values = np.random.uniform(20, 80, 1000)

    data.append(values)

# Create violin plot
chart.violin(data, labels=categories, show_means=True)
chart.set_title('Distribution Analysis - Violin Plot')
chart.set_ylabel('Values')

fig.show()`,
            features: [
                'Kernel density estimation (KDE)',
                'Statistical overlays (mean, median, quartiles)',
                'Multiple distribution visualization',
                'Bandwidth optimization',
                'Comparative analysis tools'
            ]
        },
        radar: {
            title: 'Radar Chart Demo',
            code: `import vizlychart as vz
import numpy as np

# Create radar chart for multi-dimensional comparison
fig = vz.Figure(gpu=True)
chart = vz.RadarChart(fig)

# Define performance metrics
metrics = ['Speed', 'Memory', 'GPU Usage', 'Accuracy', 'Scalability']
n_metrics = len(metrics)

# Performance data for different systems
systems = {
    'System A': [85, 90, 75, 95, 80],
    'System B': [90, 85, 85, 90, 85],
    'System C': [80, 95, 90, 85, 90]
}

# Plot multiple systems
for system_name, values in systems.items():
    chart.plot(
        values,
        labels=metrics,
        label=system_name,
        fill_alpha=0.3
    )

chart.set_title('System Performance Comparison')
chart.set_scale(0, 100)  # 0-100 scale
chart.show_grid(True)

fig.show()`,
            features: [
                'Multi-dimensional data comparison',
                'Customizable scale and grid',
                'Multiple series overlay',
                'Interactive legend',
                'Professional styling themes'
            ]
        },
        fem: {
            title: 'FEM Analysis Demo',
            code: `import vizlychart as vz
import numpy as np
from vizlychart.engineering import FEMSolver

# Create FEM analysis visualization
fig = vz.Figure(gpu=True)
fem_chart = vz.FEMChart(fig)

# Define mesh geometry
nodes = np.array([
    [0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1]
])
elements = np.array([
    [0, 1, 4, 3], [1, 2, 5, 4]  # Quad elements
])

# Apply loads and boundary conditions
loads = {1: [0, -1000]}  # 1000N downward on node 1
boundary_conditions = {0: [0, 0], 3: [0, 0]}  # Fixed supports

# Solve FEM problem
solver = FEMSolver(nodes, elements)
solver.apply_loads(loads)
solver.apply_boundary_conditions(boundary_conditions)
stress, displacement = solver.solve()

# Visualize results with GPU acceleration
fem_chart.plot_mesh(nodes, elements,
                   stress_values=stress,
                   displacement=displacement,
                   colormap='jet',
                   show_deformed=True,
                   scale_factor=100)

fem_chart.set_title('FEM Stress Analysis - Bridge Beam')
fem_chart.add_colorbar(label='Von Mises Stress (MPa)')

fig.show()`,
            features: [
                'GPU-accelerated finite element solving',
                'Stress contour visualization',
                'Deformed shape animation',
                'Multiple element types (quad, triangle, hex)',
                'Interactive mesh manipulation'
            ]
        },
        cfd: {
            title: 'CFD Simulation Demo',
            code: `import vizlychart as vz
import numpy as np
from vizlychart.engineering import CFDSolver

# Create CFD flow visualization
fig = vz.Figure(gpu=True)
cfd_chart = vz.CFDChart(fig)

# Define flow domain
x = np.linspace(0, 10, 50)
y = np.linspace(0, 5, 25)
X, Y = np.meshgrid(x, y)

# Setup flow simulation
solver = CFDSolver(domain_shape=(50, 25))
solver.set_inlet_velocity(inlet_velocity=10.0)
solver.set_wall_boundaries(walls=['top', 'bottom'])
solver.set_outlet_pressure(pressure=101325)

# Add obstacle (cylinder)
solver.add_cylinder(center=(3, 2.5), radius=0.5)

# Solve Navier-Stokes equations with GPU acceleration
velocity_field, pressure_field = solver.solve(
    reynolds_number=1000,
    time_steps=1000,
    convergence_tolerance=1e-6
)

# Visualize results
cfd_chart.plot_velocity_field(X, Y, velocity_field,
                             streamlines=True,
                             colormap='coolwarm')

cfd_chart.plot_pressure_contours(X, Y, pressure_field,
                                levels=20,
                                alpha=0.7)

cfd_chart.set_title('CFD Analysis - Flow Around Cylinder')
cfd_chart.set_labels('X Position (m)', 'Y Position (m)')

fig.show()`,
            features: [
                'GPU-accelerated Navier-Stokes solver',
                'Velocity vector field visualization',
                'Pressure contour mapping',
                'Streamline generation',
                'Turbulence modeling support'
            ]
        },
        cad: {
            title: 'CAD Model Rendering Demo',
            code: `import vizlychart as vz
from vizlychart.cad import IGESImporter, STEPImporter

# Create CAD model viewer
fig = vz.Figure(gpu=True, renderer='webgl')
cad_viewer = vz.CADViewer(fig)

# Import CAD model from IGES file
importer = IGESImporter()
model = importer.load_file('mechanical_part.iges')

# Alternative: Import from STEP file
# step_importer = STEPImporter()
# model = step_importer.load_file('assembly.step')

# Render 3D model with GPU acceleration
cad_viewer.add_model(model,
                    color='steel_blue',
                    transparency=0.8,
                    edge_visibility=True,
                    surface_quality='high')

# Add measurements and annotations
cad_viewer.add_dimension(
    start_point=[0, 0, 0],
    end_point=[10, 0, 0],
    label='Length: 10mm'
)

# Apply materials and lighting
cad_viewer.set_material('aluminum_brushed')
cad_viewer.add_lighting(
    ambient=0.3,
    directional=0.7,
    specular=0.5
)

# Interactive controls
cad_viewer.enable_rotation(True)
cad_viewer.enable_zoom(True)
cad_viewer.enable_pan(True)

# Export capabilities
cad_viewer.export_webxr('model_viewer.html')  # VR/AR viewing
cad_viewer.export_gltf('model.gltf')  # 3D web format

fig.show()`,
            features: [
                'IGES, STEP, STL file import',
                'GPU-accelerated 3D rendering',
                'Interactive model manipulation',
                'Measurement and annotation tools',
                'WebXR export for VR/AR viewing'
            ]
        },
        vibration: {
            title: 'Modal Analysis Demo',
            code: `import vizlychart as vz
import numpy as np
from vizlychart.engineering import ModalSolver

# Create vibration analysis visualization
fig = vz.Figure(gpu=True)
modal_chart = vz.ModalChart(fig)

# Define structure geometry (cantilever beam)
length = 1.0  # 1 meter beam
nodes = np.linspace(0, length, 21)  # 21 nodes
beam_properties = {
    'young_modulus': 200e9,  # Steel (Pa)
    'density': 7850,         # kg/m³
    'cross_section': 0.01,   # m²
    'moment_inertia': 8.33e-6  # m⁴
}

# Solve for natural frequencies and mode shapes
solver = ModalSolver(nodes, beam_properties)
solver.set_boundary_conditions(fixed_end=0)  # Cantilever

frequencies, mode_shapes = solver.solve_eigenvalue_problem(
    num_modes=5
)

# Animate mode shapes
for i, (freq, mode) in enumerate(zip(frequencies, mode_shapes)):
    modal_chart.add_mode_shape(
        nodes, mode,
        frequency=freq,
        mode_number=i+1,
        animate=True,
        amplitude_scale=0.1
    )

# Create frequency response function
excitation_freq = np.linspace(0, 200, 1000)  # 0-200 Hz
response = solver.calculate_frf(
    excitation_point=length,  # Tip excitation
    response_point=length,
    frequencies=excitation_freq,
    damping_ratio=0.02
)

modal_chart.plot_frf(excitation_freq, response,
                    log_scale=True,
                    show_resonances=True)

modal_chart.set_title('Modal Analysis - Cantilever Beam')
modal_chart.set_labels('Position (m)', 'Amplitude')

# Display mode information
for i, freq in enumerate(frequencies):
    print(f"Mode {i+1}: {freq:.2f} Hz")

fig.show()`,
            features: [
                'Eigenvalue problem solving',
                'Animated mode shape visualization',
                'Frequency response function (FRF)',
                'Resonance peak identification',
                'Multi-DOF system support'
            ]
        },
        thermal: {
            title: 'Thermal Analysis Demo',
            code: `import vizlychart as vz
import numpy as np
from vizlychart.engineering import ThermalSolver

# Create thermal analysis visualization
fig = vz.Figure(gpu=True)
thermal_chart = vz.ThermalChart(fig)

# Define 2D heat conduction problem
nx, ny = 50, 50
x = np.linspace(0, 0.1, nx)  # 10cm x 10cm domain
y = np.linspace(0, 0.1, ny)
X, Y = np.meshgrid(x, y)

# Setup thermal solver
solver = ThermalSolver(domain_shape=(nx, ny))
solver.set_material_properties(
    thermal_conductivity=200,  # W/m·K (Aluminum)
    density=2700,              # kg/m³
    specific_heat=900          # J/kg·K
)

# Define boundary conditions
solver.set_temperature_bc(boundary='left', temperature=100)    # Hot side
solver.set_temperature_bc(boundary='right', temperature=20)    # Cold side
solver.set_heat_flux_bc(boundary='top', heat_flux=0)          # Insulated
solver.set_heat_flux_bc(boundary='bottom', heat_flux=0)       # Insulated

# Add internal heat generation (electronics)
heat_source = np.zeros((nx, ny))
heat_source[20:30, 20:30] = 1e6  # 1 MW/m³ heat generation

solver.add_heat_source(heat_source)

# Solve steady-state heat equation
temperature = solver.solve_steady_state()

# Visualize temperature distribution
thermal_chart.plot_temperature_contours(
    X, Y, temperature,
    levels=20,
    colormap='hot',
    show_isotherms=True
)

# Add heat flux vectors
heat_flux_x, heat_flux_y = solver.calculate_heat_flux(temperature)
thermal_chart.plot_heat_flux_vectors(
    X[::5, ::5], Y[::5, ::5],
    heat_flux_x[::5, ::5], heat_flux_y[::5, ::5],
    scale=0.001,
    color='blue'
)

thermal_chart.set_title('Thermal Analysis - Electronic Component')
thermal_chart.add_colorbar(label='Temperature (°C)')
thermal_chart.set_labels('X Position (m)', 'Y Position (m)')

# Calculate maximum temperature
max_temp = np.max(temperature)
print(f"Maximum temperature: {max_temp:.1f}°C")

fig.show()`,
            features: [
                'GPU-accelerated heat equation solver',
                'Temperature contour visualization',
                'Heat flux vector plotting',
                'Multiple boundary condition types',
                'Transient thermal analysis support'
            ]
        }
        // Add more chart demos...
    };

    const demo = demos[chartType];
    if (demo) {
        title.textContent = demo.title;
        code.textContent = demo.code;
        features.innerHTML = demo.features.map(f => `<li>${f}</li>`).join('');
        modal.style.display = 'block';
    }
}

function closeModal() {
    document.getElementById('chart-modal').style.display = 'none';
}

function copyModalCode() {
    const code = document.getElementById('modal-code').textContent;
    navigator.clipboard.writeText(code).then(() => {
        showToast('Code copied to clipboard!');
    });
}

function runPerformanceTest() {
    const pointCount = parseInt(document.getElementById('point-count').value);
    const cpuTime = simulateRenderTime(pointCount, 'cpu');
    const gpuTime = simulateRenderTime(pointCount, 'gpu');
    const speedup = Math.round(cpuTime / gpuTime);

    // Animate progress bars
    const cpuProgress = document.getElementById('cpu-progress');
    const gpuProgress = document.getElementById('gpu-progress');

    cpuProgress.style.width = '100%';
    gpuProgress.style.width = `${(gpuTime / cpuTime) * 100}%`;

    // Update displays
    document.getElementById('cpu-time').textContent = `${cpuTime}ms`;
    document.getElementById('gpu-time').textContent = `${gpuTime}ms`;
    document.getElementById('speedup-value').textContent = `${speedup}x`;

    // Update metrics
    document.getElementById('render-time').textContent = `${gpuTime}ms`;
    document.getElementById('data-points').textContent = pointCount.toLocaleString();
    document.getElementById('gpu-speedup').textContent = `${speedup}x`;
}

function simulateRenderTime(points, type) {
    const baseTime = type === 'cpu' ? 0.2 : 0.025; // ms per point
    return Math.round(points * baseTime);
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('chart-modal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}
</script>

<?php require_once 'includes/footer.php'; ?>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<script>
// Initialize charts when page loads
document.addEventListener("DOMContentLoaded", function() {
    initializeGalleryCharts();
});

function initializeGalleryCharts() {
    // Initialize all visible chart canvases
    initLineChart();
    initScatterChart();
    initBarChart();
    initSurfaceChart();
    initHeatmapChart();
}

function initLineChart() {
    const canvas = document.getElementById("line-chart-demo");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    const data = generateTimeSeriesData(100);

    new Chart(ctx, {
        type: "line",
        data: {
            labels: data.labels,
            datasets: [{
                label: "Performance Data",
                data: data.values,
                borderColor: "#3b82f6",
                backgroundColor: "rgba(59, 130, 246, 0.1)",
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: { x: { display: false }, y: { display: false } },
            elements: { point: { radius: 0 } }
        }
    });
}

function generateTimeSeriesData(points) {
    const labels = [];
    const values = [];
    for (let i = 0; i < points; i++) {
        labels.push(i);
        values.push(Math.sin(i * 0.1) * 50 + Math.random() * 20);
    }
    return { labels, values };
}
</script>
