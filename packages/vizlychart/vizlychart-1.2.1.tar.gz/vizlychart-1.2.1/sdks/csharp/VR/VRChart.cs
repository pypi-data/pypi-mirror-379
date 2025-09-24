using System;
using System.Numerics;
using System.Threading.Tasks;

namespace Vizly.SDK
{
    /// <summary>
    /// VR/AR chart integration with WebXR support
    /// </summary>
    public class VRChart
    {
        private readonly IChart _baseChart;
        private readonly VRTransform _transform;

        public string VRChartId { get; } = Guid.NewGuid().ToString();
        public IChart BaseChart => _baseChart;
        public VRTransform Transform => _transform;

        public VRChart(IChart baseChart, VRTransform transform)
        {
            _baseChart = baseChart ?? throw new ArgumentNullException(nameof(baseChart));
            _transform = transform ?? throw new ArgumentNullException(nameof(transform));
        }

        /// <summary>
        /// Export chart to WebXR-compatible format
        /// </summary>
        public async Task<WebXRScene> ExportToWebXRAsync()
        {
            var scene = new WebXRScene();

            var chartNode = new WebXRNode
            {
                Id = VRChartId,
                Type = "vizly-chart",
                Transform = new WebXRTransform
                {
                    Position = _transform.Position,
                    Rotation = _transform.Rotation,
                    Scale = _transform.Scale
                },
                ChartData = _baseChart.GetData(),
                Interactive = true
            };

            scene.Nodes.Add(chartNode);

            return scene;
        }

        /// <summary>
        /// Generate WebXR HTML page for this chart
        /// </summary>
        public string GenerateWebXRHtml(WebXRMode mode = WebXRMode.VR)
        {
            var modeString = mode == WebXRMode.VR ? "immersive-vr" : "immersive-ar";

            return $@"
<!DOCTYPE html>
<html>
<head>
    <meta charset=""utf-8"">
    <title>Vizly {mode} Visualization</title>
    <script src=""https://cdn.jsdelivr.net/npm/three@0.150.0/build/three.min.js""></script>
    <script src=""https://cdn.jsdelivr.net/npm/three@0.150.0/examples/js/webxr/VRButton.js""></script>
    <script src=""https://cdn.jsdelivr.net/npm/three@0.150.0/examples/js/webxr/ARButton.js""></script>
    <style>
        body {{ margin: 0; background: #000; }}
        #container {{ width: 100%; height: 100vh; }}
    </style>
</head>
<body>
    <div id=""container""></div>
    <script>
        // Vizly WebXR Chart: {VRChartId}
        let scene, camera, renderer;

        function init() {{
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

            renderer = new THREE.WebGLRenderer({{ antialias: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.xr.enabled = true;

            document.getElementById('container').appendChild(renderer.domElement);

            // Add {mode} button
            {(mode == WebXRMode.VR ? "document.body.appendChild(VRButton.createButton(renderer));" : "document.body.appendChild(ARButton.createButton(renderer));")}

            // Create chart representation
            const chartGeometry = new THREE.BoxGeometry(2, 1.5, 0.1);
            const chartMaterial = new THREE.MeshBasicMaterial({{ color: 0x0066cc }});
            const chartMesh = new THREE.Mesh(chartGeometry, chartMaterial);

            chartMesh.position.set({_transform.Position.X}, {_transform.Position.Y}, {_transform.Position.Z});
            scene.add(chartMesh);

            renderer.setAnimationLoop(animate);
        }}

        function animate() {{
            renderer.render(scene, camera);
        }}

        init();
        console.log('Vizly {mode} chart {VRChartId} initialized');
    </script>
</body>
</html>";
        }

        /// <summary>
        /// Enable hand tracking for VR interaction
        /// </summary>
        public VRChart EnableHandTracking()
        {
            // Hand tracking implementation would go here
            return this;
        }

        /// <summary>
        /// Set spatial position in VR space
        /// </summary>
        public VRChart SetPosition(Vector3 position)
        {
            _transform.Position = position;
            return this;
        }

        /// <summary>
        /// Set rotation in VR space
        /// </summary>
        public VRChart SetRotation(Quaternion rotation)
        {
            _transform.Rotation = rotation;
            return this;
        }

        /// <summary>
        /// Set scale in VR space
        /// </summary>
        public VRChart SetScale(Vector3 scale)
        {
            _transform.Scale = scale;
            return this;
        }
    }

    public enum WebXRMode
    {
        VR,
        AR
    }

    public class VRTransform
    {
        public Vector3 Position { get; set; } = new Vector3(0, 1.5f, -2);
        public Quaternion Rotation { get; set; } = Quaternion.Identity;
        public Vector3 Scale { get; set; } = Vector3.One;

        public static VRTransform Default => new VRTransform();
    }

    public class WebXRScene
    {
        public List<WebXRNode> Nodes { get; set; } = new();
        public string ReferenceSpace { get; set; } = "local-floor";
    }

    public class WebXRNode
    {
        public string Id { get; set; } = "";
        public string Type { get; set; } = "";
        public WebXRTransform Transform { get; set; } = new();
        public ChartData? ChartData { get; set; }
        public bool Interactive { get; set; } = false;
    }

    public class WebXRTransform
    {
        public Vector3 Position { get; set; }
        public Quaternion Rotation { get; set; }
        public Vector3 Scale { get; set; }
    }
}