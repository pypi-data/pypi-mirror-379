package io.vizly;

/**
 * Base interface for all Vizly charts
 */
public interface Chart {
    String getChartId();
    ChartType getType();
    ChartData getData();
}

/**
 * Chart types enumeration
 */
enum ChartType {
    LINE, SCATTER, BAR, SURFACE, HEATMAP
}

/**
 * Image format enumeration
 */
enum ImageFormat {
    PNG, JPEG, SVG
}

/**
 * 2D point data structure
 */
record Point2D(float x, float y) {}

/**
 * Chart data container for serialization
 */
record ChartData(
    String chartId,
    ChartType type,
    java.util.List<Point2D> dataPoints,
    String title,
    String xLabel,
    String yLabel
) {}

/**
 * Chart renderer interface
 */
interface ChartRenderer {
    byte[] renderChart(Chart chart, int width, int height) throws Exception;
}

/**
 * GPU-accelerated renderer
 */
class GpuRenderer implements ChartRenderer {
    @Override
    public byte[] renderChart(Chart chart, int width, int height) {
        // GPU rendering implementation
        try {
            Thread.sleep(10); // Simulate GPU rendering
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return new byte[width * height * 4]; // RGBA buffer
    }
}

/**
 * CPU fallback renderer
 */
class CpuRenderer implements ChartRenderer {
    @Override
    public byte[] renderChart(Chart chart, int width, int height) {
        // CPU rendering implementation
        try {
            Thread.sleep(50); // Simulate CPU rendering (slower)
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return new byte[width * height * 4]; // RGBA buffer
    }
}