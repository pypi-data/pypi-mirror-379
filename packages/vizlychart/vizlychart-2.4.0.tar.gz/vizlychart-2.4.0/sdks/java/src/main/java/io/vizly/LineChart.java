package io.vizly;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;

/**
 * High-performance line chart with GPU acceleration support
 */
public class LineChart implements Chart, AutoCloseable {

    private final String chartId;
    private final List<Point2D> dataPoints;
    private String title = "";
    private String xLabel = "";
    private String yLabel = "";
    private boolean gpuAccelerated = true;

    public LineChart() {
        this.chartId = java.util.UUID.randomUUID().toString();
        this.dataPoints = new ArrayList<>();
    }

    /**
     * Add data points to the line chart
     */
    public LineChart plot(float[] x, float[] y) {
        if (x.length != y.length) {
            throw new IllegalArgumentException("X and Y arrays must have the same length");
        }

        for (int i = 0; i < x.length; i++) {
            dataPoints.add(new Point2D(x[i], y[i]));
        }

        return this;
    }

    /**
     * Add data points with GPU acceleration
     */
    public CompletableFuture<LineChart> plotAsync(float[] x, float[] y) {
        return CompletableFuture.supplyAsync(() -> {
            if (gpuAccelerated && GpuBackend.isAvailable()) {
                try {
                    GpuBackend.processDataAsync(x, y).join();
                } catch (Exception e) {
                    // Fallback to CPU if GPU fails
                    System.err.println("GPU processing failed, using CPU: " + e.getMessage());
                }
            }
            return plot(x, y);
        });
    }

    /**
     * Set chart title
     */
    public LineChart setTitle(String title) {
        this.title = title;
        return this;
    }

    /**
     * Set axis labels
     */
    public LineChart setLabels(String xLabel, String yLabel) {
        this.xLabel = xLabel;
        this.yLabel = yLabel;
        return this;
    }

    /**
     * Enable or disable GPU acceleration
     */
    public LineChart enableGpu(boolean enable) {
        this.gpuAccelerated = enable;
        return this;
    }

    /**
     * Enable real-time streaming updates
     */
    public CompletableFuture<StreamingChart> enableStreaming(String streamUrl) {
        StreamingChart streamingChart = new StreamingChart(this);
        return streamingChart.connectAsync(streamUrl);
    }

    /**
     * Export chart to VR/AR scene
     */
    public VRChart toVR() {
        return toVR(VRTransform.getDefault());
    }

    public VRChart toVR(VRTransform transform) {
        return new VRChart(this, transform);
    }

    /**
     * Render chart to image asynchronously
     */
    public CompletableFuture<byte[]> renderAsync(int width, int height) {
        return CompletableFuture.supplyAsync(() -> {
            ChartRenderer renderer = gpuAccelerated && GpuBackend.isAvailable()
                    ? new GpuRenderer()
                    : new CpuRenderer();

            try {
                return renderer.renderChart(this, width, height);
            } catch (Exception e) {
                throw new RuntimeException("Failed to render chart", e);
            }
        });
    }

    public CompletableFuture<byte[]> renderAsync() {
        return renderAsync(800, 600);
    }

    /**
     * Save chart to file
     */
    public CompletableFuture<Void> saveAsync(String filePath) {
        return saveAsync(filePath, ImageFormat.PNG);
    }

    public CompletableFuture<Void> saveAsync(String filePath, ImageFormat format) {
        return renderAsync().thenAccept(imageData -> {
            try {
                java.nio.file.Files.write(java.nio.file.Paths.get(filePath), imageData);
            } catch (Exception e) {
                throw new RuntimeException("Failed to save chart", e);
            }
        });
    }

    // Chart interface implementation
    @Override
    public String getChartId() {
        return chartId;
    }

    @Override
    public ChartType getType() {
        return ChartType.LINE;
    }

    @Override
    public ChartData getData() {
        return new ChartData(chartId, ChartType.LINE, dataPoints, title, xLabel, yLabel);
    }

    // Getters
    public List<Point2D> getDataPoints() {
        return new ArrayList<>(dataPoints);
    }

    public String getTitle() {
        return title;
    }

    public String getXLabel() {
        return xLabel;
    }

    public String getYLabel() {
        return yLabel;
    }

    public boolean isGpuAccelerated() {
        return gpuAccelerated;
    }

    @Override
    public void close() {
        dataPoints.clear();
    }

    @Override
    public String toString() {
        return String.format("LineChart{id='%s', title='%s', points=%d, gpu=%b}",
                chartId, title, dataPoints.size(), gpuAccelerated);
    }
}