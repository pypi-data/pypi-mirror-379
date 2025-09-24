using System.Text.Json.Serialization;

namespace Vizly.SDK
{
    /// <summary>
    /// Configuration options for Vizly charts
    /// </summary>
    public class ChartOptions
    {
        /// <summary>
        /// Chart title
        /// </summary>
        public string Title { get; set; } = "";

        /// <summary>
        /// X-axis label
        /// </summary>
        public string XLabel { get; set; } = "";

        /// <summary>
        /// Y-axis label
        /// </summary>
        public string YLabel { get; set; } = "";

        /// <summary>
        /// Chart theme
        /// </summary>
        public string Theme { get; set; } = "modern";

        /// <summary>
        /// Enable GPU acceleration
        /// </summary>
        public bool GpuAcceleration { get; set; } = true;

        /// <summary>
        /// Enable interactive features
        /// </summary>
        public bool Interactive { get; set; } = true;

        /// <summary>
        /// Chart width in pixels
        /// </summary>
        public int Width { get; set; } = 800;

        /// <summary>
        /// Chart height in pixels
        /// </summary>
        public int Height { get; set; } = 600;

        /// <summary>
        /// Background color
        /// </summary>
        public string BackgroundColor { get; set; } = "#ffffff";

        /// <summary>
        /// Grid configuration
        /// </summary>
        public GridOptions Grid { get; set; } = new();

        /// <summary>
        /// Legend configuration
        /// </summary>
        public LegendOptions Legend { get; set; } = new();

        /// <summary>
        /// Animation settings
        /// </summary>
        public AnimationOptions Animation { get; set; } = new();
    }

    public class GridOptions
    {
        public bool Show { get; set; } = true;
        public string Color { get; set; } = "#e0e0e0";
        public float Alpha { get; set; } = 0.5f;
    }

    public class LegendOptions
    {
        public bool Show { get; set; } = true;
        public string Position { get; set; } = "top-right";
    }

    public class AnimationOptions
    {
        public bool Enabled { get; set; } = true;
        public int Duration { get; set; } = 750;
        public string Easing { get; set; } = "ease-in-out";
    }
}