using System;
using System.Numerics;
using System.Threading.Tasks;

namespace Vizly.SDK
{
    /// <summary>
    /// Base interface for all Vizly charts
    /// </summary>
    public interface IChart
    {
        string ChartId { get; }
        ChartType Type { get; }
        ChartData GetData();
    }

    /// <summary>
    /// Interface for renderable charts
    /// </summary>
    public interface IRenderable
    {
        Task<byte[]> RenderAsync(int width = 800, int height = 600);
        Task SaveAsync(string filePath, ImageFormat format = ImageFormat.PNG);
    }

    /// <summary>
    /// Interface for streaming charts
    /// </summary>
    public interface IStreamable
    {
        Task<StreamingChart> EnableStreaming(string streamUrl);
        Task UpdateDataAsync(float[] x, float[] y);
    }

    /// <summary>
    /// Interface for VR/AR compatible charts
    /// </summary>
    public interface IVRCompatible
    {
        VRChart ToVR(VRTransform? transform = null);
        Task<WebXRScene> ExportToWebXRAsync();
    }

    /// <summary>
    /// Chart data structure for serialization
    /// </summary>
    public class ChartData
    {
        public string ChartId { get; set; } = "";
        public ChartType Type { get; set; }
        public Vector2[] DataPoints { get; set; } = Array.Empty<Vector2>();
        public ChartOptions Options { get; set; } = new();
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    }

    /// <summary>
    /// Real-time streaming chart wrapper
    /// </summary>
    public class StreamingChart : IDisposable
    {
        private readonly IChart _baseChart;
        private readonly StreamingConnection _connection;
        private bool _disposed = false;

        public IChart BaseChart => _baseChart;
        public bool IsConnected => _connection.IsConnected;

        public StreamingChart(IChart baseChart)
        {
            _baseChart = baseChart ?? throw new ArgumentNullException(nameof(baseChart));
            _connection = new StreamingConnection();
        }

        public async Task ConnectAsync(string streamUrl)
        {
            await _connection.ConnectAsync(streamUrl);
        }

        public async Task DisconnectAsync()
        {
            await _connection.DisconnectAsync();
        }

        public async Task UpdateDataAsync(float[] x, float[] y)
        {
            if (!IsConnected)
                throw new InvalidOperationException("Not connected to streaming source");

            await _connection.SendDataAsync(x, y);
        }

        public void Dispose()
        {
            if (!_disposed)
            {
                _connection?.Dispose();
                _disposed = true;
            }
        }
    }

    /// <summary>
    /// Streaming connection handler
    /// </summary>
    internal class StreamingConnection : IDisposable
    {
        public bool IsConnected { get; private set; }

        public async Task ConnectAsync(string streamUrl)
        {
            // WebSocket connection implementation
            await Task.Delay(100); // Simulate connection
            IsConnected = true;
        }

        public async Task DisconnectAsync()
        {
            await Task.Delay(10);
            IsConnected = false;
        }

        public async Task SendDataAsync(float[] x, float[] y)
        {
            // Send data over WebSocket
            await Task.Delay(1);
        }

        public void Dispose()
        {
            if (IsConnected)
            {
                DisconnectAsync().Wait();
            }
        }
    }

    /// <summary>
    /// Chart renderer interface
    /// </summary>
    public interface IChartRenderer
    {
        Task<byte[]> RenderChartAsync(IChart chart, int width, int height);
    }

    /// <summary>
    /// GPU-accelerated renderer
    /// </summary>
    public class GpuRenderer : IChartRenderer
    {
        public async Task<byte[]> RenderChartAsync(IChart chart, int width, int height)
        {
            // GPU rendering implementation
            await Task.Delay(10); // Simulate GPU rendering
            return new byte[width * height * 4]; // RGBA buffer
        }
    }

    /// <summary>
    /// CPU fallback renderer
    /// </summary>
    public class CpuRenderer : IChartRenderer
    {
        public async Task<byte[]> RenderChartAsync(IChart chart, int width, int height)
        {
            // CPU rendering implementation
            await Task.Delay(50); // Simulate CPU rendering (slower)
            return new byte[width * height * 4]; // RGBA buffer
        }
    }
}