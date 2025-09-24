#pragma once

#include <memory>
#include <vector>
#include <string>
#include <future>
#include <functional>

namespace vizly {

    // Forward declarations
    class Chart;
    class Figure;
    class GPU;
    class VRSession;
    class DataStreamer;

    // Type aliases
    using ChartPtr = std::shared_ptr<Chart>;
    using FigurePtr = std::shared_ptr<Figure>;
    using Point2D = std::pair<float, float>;
    using DataArray = std::vector<float>;

    /**
     * @brief Main Vizly namespace containing all visualization functionality
     */
    namespace core {

        /**
         * @brief Base chart class with GPU acceleration support
         */
        class Chart {
        public:
            virtual ~Chart() = default;

            /**
             * @brief Set chart title
             */
            virtual Chart& set_title(const std::string& title) = 0;

            /**
             * @brief Set axis labels
             */
            virtual Chart& set_labels(const std::string& x_label, const std::string& y_label) = 0;

            /**
             * @brief Enable GPU acceleration
             */
            virtual Chart& enable_gpu(bool enable = true) = 0;

            /**
             * @brief Render chart asynchronously
             */
            virtual std::future<std::vector<uint8_t>> render_async(int width = 800, int height = 600) = 0;

            /**
             * @brief Save chart to file
             */
            virtual void save(const std::string& filename) = 0;

            /**
             * @brief Export to VR scene
             */
            virtual std::shared_ptr<VRSession> to_vr() = 0;
        };

        /**
         * @brief High-performance line chart with GPU support
         */
        class LineChart : public Chart {
        private:
            std::vector<Point2D> data_points_;
            std::string title_;
            std::string x_label_, y_label_;
            bool gpu_enabled_ = true;

        public:
            /**
             * @brief Constructor
             */
            LineChart();

            /**
             * @brief Add data points to chart
             */
            LineChart& plot(const DataArray& x, const DataArray& y);

            /**
             * @brief Add data points with GPU acceleration
             */
            std::future<LineChart&> plot_async(const DataArray& x, const DataArray& y);

            // Inherited from Chart
            Chart& set_title(const std::string& title) override;
            Chart& set_labels(const std::string& x_label, const std::string& y_label) override;
            Chart& enable_gpu(bool enable = true) override;
            std::future<std::vector<uint8_t>> render_async(int width = 800, int height = 600) override;
            void save(const std::string& filename) override;
            std::shared_ptr<VRSession> to_vr() override;
        };

        /**
         * @brief High-performance scatter chart
         */
        class ScatterChart : public Chart {
        private:
            std::vector<Point2D> data_points_;
            std::string title_;
            std::string x_label_, y_label_;
            bool gpu_enabled_ = true;

        public:
            ScatterChart();

            /**
             * @brief Add scatter points
             */
            ScatterChart& scatter(const DataArray& x, const DataArray& y);

            /**
             * @brief Add scatter points with GPU acceleration
             */
            std::future<ScatterChart&> scatter_async(const DataArray& x, const DataArray& y);

            // Inherited from Chart
            Chart& set_title(const std::string& title) override;
            Chart& set_labels(const std::string& x_label, const std::string& y_label) override;
            Chart& enable_gpu(bool enable = true) override;
            std::future<std::vector<uint8_t>> render_async(int width = 800, int height = 600) override;
            void save(const std::string& filename) override;
            std::shared_ptr<VRSession> to_vr() override;
        };

    } // namespace core

    namespace gpu {

        /**
         * @brief GPU backend manager
         */
        class BackendManager {
        public:
            /**
             * @brief Check if GPU acceleration is available
             */
            static bool is_available();

            /**
             * @brief Get GPU device information
             */
            static std::string get_device_info();

            /**
             * @brief Benchmark GPU performance
             */
            static double benchmark(int data_size = 10000);

            /**
             * @brief Process data on GPU
             */
            static std::future<void> process_data_async(const DataArray& x, const DataArray& y);
        };

    } // namespace gpu

    namespace vr {

        /**
         * @brief VR/AR session manager with WebXR support
         */
        class VRSession {
        private:
            std::string session_id_;
            bool is_active_ = false;
            std::vector<ChartPtr> charts_;

        public:
            VRSession();
            ~VRSession();

            /**
             * @brief Start VR session
             */
            std::future<bool> start_session(const std::string& mode = "immersive-vr");

            /**
             * @brief Add chart to VR scene
             */
            void add_chart(ChartPtr chart);

            /**
             * @brief Export scene to WebXR HTML
             */
            std::string export_webxr_html();

            /**
             * @brief Enable hand tracking
             */
            void enable_hand_tracking();

            /**
             * @brief End VR session
             */
            void end_session();
        };

    } // namespace vr

    namespace streaming {

        /**
         * @brief Real-time data streaming client
         */
        class DataStreamer {
        private:
            std::string stream_url_;
            bool connected_ = false;
            std::function<void(const DataArray&, const DataArray&)> data_callback_;

        public:
            DataStreamer(const std::string& stream_url);
            ~DataStreamer();

            /**
             * @brief Connect to streaming source
             */
            std::future<bool> connect_async();

            /**
             * @brief Set data callback for incoming data
             */
            void set_data_callback(std::function<void(const DataArray&, const DataArray&)> callback);

            /**
             * @brief Send data to stream
             */
            std::future<void> send_data_async(const DataArray& x, const DataArray& y);

            /**
             * @brief Disconnect from stream
             */
            void disconnect();

            /**
             * @brief Check if connected
             */
            bool is_connected() const { return connected_; }
        };

        /**
         * @brief Real-time chart with streaming support
         */
        class StreamingChart {
        private:
            ChartPtr base_chart_;
            std::unique_ptr<DataStreamer> streamer_;

        public:
            StreamingChart(ChartPtr base_chart, const std::string& stream_url);

            /**
             * @brief Start streaming data updates
             */
            std::future<void> start_streaming();

            /**
             * @brief Stop streaming
             */
            void stop_streaming();

            /**
             * @brief Update chart with new data
             */
            void update_data(const DataArray& x, const DataArray& y);
        };

    } // namespace streaming

    // Convenience factory functions
    namespace factory {

        /**
         * @brief Create line chart
         */
        inline std::shared_ptr<core::LineChart> line_chart() {
            return std::make_shared<core::LineChart>();
        }

        /**
         * @brief Create scatter chart
         */
        inline std::shared_ptr<core::ScatterChart> scatter_chart() {
            return std::make_shared<core::ScatterChart>();
        }

        /**
         * @brief Create VR session
         */
        inline std::shared_ptr<vr::VRSession> vr_session() {
            return std::make_shared<vr::VRSession>();
        }

        /**
         * @brief Create streaming chart
         */
        inline std::shared_ptr<streaming::StreamingChart> streaming_chart(
            ChartPtr chart, const std::string& stream_url) {
            return std::make_shared<streaming::StreamingChart>(chart, stream_url);
        }

    } // namespace factory

} // namespace vizly

// Global convenience aliases
using VizlyLineChart = vizly::core::LineChart;
using VizlyScatterChart = vizly::core::ScatterChart;
using VizlyVRSession = vizly::vr::VRSession;
using VizlyDataStreamer = vizly::streaming::DataStreamer;