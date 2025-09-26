using System;
using System.Collections.Generic;
using System.Numerics;
using System.Threading.Tasks;

namespace Vizly.SDK.Charts
{
    /// <summary>
    /// High-performance line chart with GPU acceleration support
    /// </summary>
    public class LineChart : IChart, IDisposable
    {
        private readonly List<Vector2> _dataPoints = new();
        private readonly ChartOptions _options;
        private bool _disposed = false;

        public string ChartId { get; } = Guid.NewGuid().ToString();
        public ChartType Type => ChartType.Line;
        public bool GpuAccelerated { get; set; } = true;

        public LineChart(ChartOptions? options = null)
        {
            _options = options ?? new ChartOptions();
        }

        /// <summary>
        /// Add data points to the line chart
        /// </summary>
        public LineChart Plot(float[] x, float[] y, LineStyle? style = null)
        {
            if (x.Length != y.Length)
                throw new ArgumentException("X and Y arrays must have the same length");

            for (int i = 0; i < x.Length; i++)
            {
                _dataPoints.Add(new Vector2(x[i], y[i]));
            }

            return this;
        }

        /// <summary>
        /// Add data points with GPU acceleration
        /// </summary>
        public async Task<LineChart> PlotAsync(float[] x, float[] y, LineStyle? style = null)
        {
            if (GpuAccelerated && GpuBackend.IsAvailable())
            {
                await GpuBackend.ProcessDataAsync(x, y);
            }

            return Plot(x, y, style);
        }

        /// <summary>
        /// Set chart title
        /// </summary>
        public LineChart SetTitle(string title)
        {
            _options.Title = title;
            return this;
        }

        /// <summary>
        /// Set axis labels
        /// </summary>
        public LineChart SetLabels(string xLabel, string yLabel)
        {
            _options.XLabel = xLabel;
            _options.YLabel = yLabel;
            return this;
        }

        /// <summary>
        /// Enable real-time streaming updates
        /// </summary>
        public async Task<StreamingChart> EnableStreaming(string streamUrl)
        {
            var streamingChart = new StreamingChart(this);
            await streamingChart.ConnectAsync(streamUrl);
            return streamingChart;
        }

        /// <summary>
        /// Export chart to VR/AR scene
        /// </summary>
        public VRChart ToVR(VRTransform? transform = null)
        {
            return new VRChart(this, transform ?? VRTransform.Default);
        }

        /// <summary>
        /// Render chart to image
        /// </summary>
        public async Task<byte[]> RenderAsync(int width = 800, int height = 600)
        {
            var renderer = GpuAccelerated && GpuBackend.IsAvailable()
                ? new GpuRenderer()
                : new CpuRenderer();

            return await renderer.RenderChartAsync(this, width, height);
        }

        /// <summary>
        /// Save chart to file
        /// </summary>
        public async Task SaveAsync(string filePath, ImageFormat format = ImageFormat.PNG)
        {
            var imageData = await RenderAsync();
            await File.WriteAllBytesAsync(filePath, imageData);
        }

        /// <summary>
        /// Get chart data for serialization
        /// </summary>
        public ChartData GetData()
        {
            return new ChartData
            {
                ChartId = ChartId,
                Type = Type,
                DataPoints = _dataPoints.ToArray(),
                Options = _options
            };
        }

        public void Dispose()
        {
            if (!_disposed)
            {
                _dataPoints.Clear();
                _disposed = true;
            }
        }
    }

    public enum ChartType
    {
        Line,
        Scatter,
        Bar,
        Surface,
        Heatmap
    }

    public enum ImageFormat
    {
        PNG,
        JPEG,
        SVG
    }

    public class LineStyle
    {
        public string Color { get; set; } = "#0066cc";
        public float Width { get; set; } = 2.0f;
        public bool Smooth { get; set; } = true;
        public float Alpha { get; set; } = 1.0f;
    }
}