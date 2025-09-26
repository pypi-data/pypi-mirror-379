# Quick test script to verify VizlyChart works in Google Colab environment
import sys
print("🧪 VizlyChart Colab Compatibility Test")
print("=" * 40)

# Test basic imports
try:
    import numpy as np
    print("✅ NumPy: Available")
except ImportError:
    print("❌ NumPy: Missing")

try:
    import pandas as pd
    print("✅ Pandas: Available")
except ImportError:
    print("❌ Pandas: Missing")

try:
    import matplotlib.pyplot as plt
    print("✅ Matplotlib: Available")
except ImportError:
    print("❌ Matplotlib: Missing")

try:
    import ipywidgets as widgets
    print("✅ IPyWidgets: Available")
except ImportError:
    print("❌ IPyWidgets: Missing - install with !pip install ipywidgets")

# Test if running in Colab
try:
    import google.colab
    print("✅ Google Colab: Detected")
    colab_env = True
except ImportError:
    print("ℹ️  Google Colab: Not detected (running locally)")
    colab_env = False

# Test GPU availability
gpu_available = False
try:
    import tensorflow as tf
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        print(f"✅ GPU: {len(gpus)} device(s) available")
        for gpu in gpus:
            print(f"   • {gpu.name}")
        gpu_available = True
    else:
        print("⚠️  GPU: No TensorFlow GPU devices found")
except ImportError:
    print("ℹ️  GPU: TensorFlow not available for GPU detection")

# Test CUDA availability for potential cupy usage
try:
    import cupy
    print("✅ CuPy: Available for GPU acceleration")
    cuda_available = True
except ImportError:
    print("⚠️  CuPy: Not available - GPU acceleration limited")
    cuda_available = False

# Environment summary
print("\n🎯 Environment Summary:")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Colab Environment: {colab_env}")
print(f"GPU Available: {gpu_available}")
print(f"CUDA Available: {cuda_available}")

# Recommendations
print("\n💡 Recommendations for VizlyChart:")
if colab_env:
    print("• ✅ Perfect Colab environment")
    if gpu_available:
        print("• ✅ GPU acceleration ready")
        print("• 💡 Try !pip install cupy-cuda11x for full GPU support")
    else:
        print("• ⚠️  Enable GPU runtime: Runtime > Change runtime type > GPU")
else:
    print("• ℹ️  Running locally - all features should work")

print("\n🚀 Ready to run VizlyChart notebook!")