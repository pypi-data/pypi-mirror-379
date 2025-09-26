<?php
/**
 * VizlyChart Website Configuration
 * Configuration settings for the comprehensive website
 */

// Site configuration
define('SITE_NAME', 'VizlyChart');
define('SITE_TITLE', 'VizlyChart - High-Performance Visualization Library');
define('SITE_DESCRIPTION', 'Revolutionary visualization library with GPU acceleration, VR/AR support, real-time streaming, and multi-language SDKs');
define('SITE_URL', 'https://vizlychart.io');
define('CONTACT_EMAIL', 'durai@infinidatum.net');
define('COMPANY_NAME', 'Infinidatum Corporation');

// Version information
define('VIZLYCHART_VERSION', '1.1.0');
define('RELEASE_DATE', 'December 2024');

// Pricing configuration
$pricing = [
    'community' => [
        'name' => 'Community Edition',
        'price' => 'Free',
        'features' => [
            'Core Python package via PyPI',
            'Basic chart types (Line, Scatter, Bar, Surface)',
            'PNG/SVG export',
            'Community support'
        ]
    ],
    'professional' => [
        'name' => 'Professional Edition',
        'price' => '$5,000/year',
        'features' => [
            'All SDK access (C#, C++, Java)',
            'GPU acceleration with CUDA/OpenCL',
            'VR/AR features with WebXR',
            '50+ chart types',
            'Real-time streaming capabilities'
        ]
    ],
    'enterprise' => [
        'name' => 'Enterprise Edition',
        'price' => 'Custom pricing',
        'features' => [
            'High-frequency streaming capabilities',
            'Custom GPU kernel development',
            '24/7 support with SLA guarantees',
            'Volume licensing discounts',
            'Advanced VR/AR integration'
        ]
    ]
];

// Chart types configuration
$chart_categories = [
    'Basic' => ['Line', 'Scatter', 'Bar', 'Surface', 'Histogram', 'Box Plot'],
    'Advanced' => ['Heatmap', 'Violin', 'Radar', 'Treemap', 'Sankey', 'Spectrogram'],
    'Financial' => ['Candlestick', 'OHLC', 'RSI', 'MACD', 'Volume Profile', 'Point & Figure'],
    'Engineering' => ['Bode Plot', 'Stress-Strain', 'Phase Diagram', 'Contour'],
    'Data Science' => ['Distribution', 'Correlation', 'Regression', 'Anomaly Detection']
];

// Performance benchmarks (actual GPU acceleration)
$benchmarks = [
    '10K Points' => ['speedup' => '8x', 'cpu_time' => '200ms', 'gpu_time' => '25ms'],
    '100K Points' => ['speedup' => '20x', 'cpu_time' => '2s', 'gpu_time' => '100ms'],
    '1M Points' => ['speedup' => '40x', 'cpu_time' => '20s', 'gpu_time' => '500ms'],
    '10M Points' => ['speedup' => '50x', 'cpu_time' => '200s', 'gpu_time' => '4s']
];

// Multi-language SDKs configuration
$sdks = [
    'python' => [
        'name' => 'Python',
        'status' => 'Live on PyPI',
        'install' => 'pip install vizlychart',
        'features' => 'Complete feature set with GPU acceleration'
    ],
    'csharp' => [
        'name' => 'C# (.NET)',
        'status' => 'Available',
        'install' => 'dotnet add package VizlyChart.SDK',
        'features' => 'Native .NET integration with VR/AR support'
    ],
    'cpp' => [
        'name' => 'C++',
        'status' => 'Available',
        'install' => 'cmake -DVIZLY_SDK=ON',
        'features' => 'High-performance native library'
    ],
    'java' => [
        'name' => 'Java',
        'status' => 'Available',
        'install' => '<artifactId>vizlychart-sdk</artifactId>',
        'features' => 'Enterprise Java integration'
    ]
];

// Navigation menu
$navigation = [
    'Home' => 'index.php',
    'Features' => 'features.php',
    'Pricing' => 'pricing.php',
    'Documentation' => 'documentation.php',
    'Gallery' => 'gallery.php',
    'Contact' => 'contact.php'
];
?>