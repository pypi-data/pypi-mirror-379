package io.vizly;

import java.util.concurrent.CompletableFuture;

/**
 * VR/AR chart integration with WebXR support
 */
public class VRChart {

    private final String vrChartId;
    private final Chart baseChart;
    private final VRTransform transform;

    public VRChart(Chart baseChart, VRTransform transform) {
        this.vrChartId = java.util.UUID.randomUUID().toString();
        this.baseChart = baseChart;
        this.transform = transform;
    }

    /**
     * Export chart to WebXR-compatible format
     */
    public CompletableFuture<WebXRScene> exportToWebXRAsync() {
        return CompletableFuture.supplyAsync(() -> {
            WebXRScene scene = new WebXRScene();

            WebXRNode chartNode = new WebXRNode(
                vrChartId,
                "vizly-chart",
                transform,
                baseChart.getData(),
                true
            );

            scene.addNode(chartNode);
            return scene;
        });
    }

    /**
     * Generate WebXR HTML page for this chart
     */
    public String generateWebXRHtml(WebXRMode mode) {
        String modeString = mode == WebXRMode.VR ? "immersive-vr" : "immersive-ar";
        String buttonCode = mode == WebXRMode.VR ?
            "document.body.appendChild(VRButton.createButton(renderer));" :
            "document.body.appendChild(ARButton.createButton(renderer));";

        return String.format("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Vizly %s Visualization</title>
    <script src="https://cdn.jsdelivr.net/npm/three@0.150.0/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.150.0/examples/js/webxr/VRButton.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.150.0/examples/js/webxr/ARButton.js"></script>
    <style>
        body { margin: 0; background: #000; }
        #container { width: 100%%; height: 100vh; }
    </style>
</head>
<body>
    <div id="container"></div>
    <script>
        // Vizly WebXR Chart: %s
        let scene, camera, renderer;

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.xr.enabled = true;

            document.getElementById('container').appendChild(renderer.domElement);

            // Add %s button
            %s

            // Create chart representation
            const chartGeometry = new THREE.BoxGeometry(2, 1.5, 0.1);
            const chartMaterial = new THREE.MeshBasicMaterial({ color: 0x0066cc });
            const chartMesh = new THREE.Mesh(chartGeometry, chartMaterial);

            chartMesh.position.set(%.1f, %.1f, %.1f);
            scene.add(chartMesh);

            renderer.setAnimationLoop(animate);
        }

        function animate() {
            renderer.render(scene, camera);
        }

        init();
        console.log('Vizly %s chart %s initialized');
    </script>
</body>
</html>""",
            mode, vrChartId, mode, buttonCode,
            transform.position().x, transform.position().y, transform.position().z,
            mode, vrChartId);
    }

    // Getters
    public String getVrChartId() { return vrChartId; }
    public Chart getBaseChart() { return baseChart; }
    public VRTransform getTransform() { return transform; }
}

/**
 * WebXR mode enumeration
 */
enum WebXRMode {
    VR, AR
}

/**
 * VR transform data structure
 */
record VRTransform(Point3D position, Quaternion rotation, Point3D scale) {
    public static VRTransform getDefault() {
        return new VRTransform(
            new Point3D(0, 1.5f, -2),
            new Quaternion(0, 0, 0, 1),
            new Point3D(1, 1, 1)
        );
    }
}

/**
 * 3D point data structure
 */
record Point3D(float x, float y, float z) {}

/**
 * Quaternion for rotations
 */
record Quaternion(float x, float y, float z, float w) {}

/**
 * WebXR scene container
 */
class WebXRScene {
    private final java.util.List<WebXRNode> nodes = new java.util.ArrayList<>();
    private String referenceSpace = "local-floor";

    public void addNode(WebXRNode node) {
        nodes.add(node);
    }

    public java.util.List<WebXRNode> getNodes() {
        return new java.util.ArrayList<>(nodes);
    }

    public String getReferenceSpace() { return referenceSpace; }
    public void setReferenceSpace(String referenceSpace) { this.referenceSpace = referenceSpace; }
}

/**
 * WebXR node representation
 */
record WebXRNode(
    String id,
    String type,
    VRTransform transform,
    ChartData chartData,
    boolean interactive
) {}

/**
 * Streaming chart wrapper
 */
class StreamingChart implements AutoCloseable {
    private final Chart baseChart;
    private StreamingConnection connection;

    public StreamingChart(Chart baseChart) {
        this.baseChart = baseChart;
    }

    public CompletableFuture<StreamingChart> connectAsync(String streamUrl) {
        return CompletableFuture.supplyAsync(() -> {
            this.connection = new StreamingConnection(streamUrl);
            connection.connect();
            return this;
        });
    }

    public Chart getBaseChart() { return baseChart; }
    public boolean isConnected() { return connection != null && connection.isConnected(); }

    @Override
    public void close() {
        if (connection != null) {
            connection.disconnect();
        }
    }
}

/**
 * Streaming connection handler
 */
class StreamingConnection {
    private final String streamUrl;
    private boolean connected = false;

    public StreamingConnection(String streamUrl) {
        this.streamUrl = streamUrl;
    }

    public void connect() {
        // WebSocket connection implementation
        try {
            Thread.sleep(100); // Simulate connection
            connected = true;
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    public void disconnect() {
        connected = false;
    }

    public boolean isConnected() { return connected; }
}