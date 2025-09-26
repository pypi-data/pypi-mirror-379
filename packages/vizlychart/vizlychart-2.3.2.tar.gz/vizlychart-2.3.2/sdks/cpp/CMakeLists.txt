cmake_minimum_required(VERSION 3.20)
project(VizlySDK VERSION 1.1.0 LANGUAGES CXX CUDA)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find packages
find_package(OpenGL REQUIRED)
find_package(OpenCL QUIET)
find_package(CUDA QUIET)

# Options
option(VIZLY_BUILD_EXAMPLES "Build example applications" ON)
option(VIZLY_GPU_SUPPORT "Enable GPU acceleration" ON)
option(VIZLY_VR_SUPPORT "Enable VR/AR support" ON)
option(VIZLY_STREAMING_SUPPORT "Enable real-time streaming" ON)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Source files
set(VIZLY_SOURCES
    src/core/chart.cpp
    src/core/figure.cpp
    src/charts/line_chart.cpp
    src/charts/scatter_chart.cpp
    src/charts/surface_chart.cpp
    src/rendering/renderer.cpp
    src/rendering/gpu_renderer.cpp
)

# GPU support
if(VIZLY_GPU_SUPPORT AND CUDA_FOUND)
    list(APPEND VIZLY_SOURCES
        src/gpu/cuda_backend.cu
        src/gpu/gpu_manager.cpp
    )
    add_definitions(-DVIZLY_CUDA_SUPPORT)
endif()

if(VIZLY_GPU_SUPPORT AND OpenCL_FOUND)
    list(APPEND VIZLY_SOURCES
        src/gpu/opencl_backend.cpp
    )
    add_definitions(-DVIZLY_OPENCL_SUPPORT)
endif()

# VR support
if(VIZLY_VR_SUPPORT)
    list(APPEND VIZLY_SOURCES
        src/vr/vr_session.cpp
        src/vr/webxr_exporter.cpp
    )
    add_definitions(-DVIZLY_VR_SUPPORT)
endif()

# Streaming support
if(VIZLY_STREAMING_SUPPORT)
    list(APPEND VIZLY_SOURCES
        src/streaming/data_streamer.cpp
        src/streaming/websocket_client.cpp
    )
    add_definitions(-DVIZLY_STREAMING_SUPPORT)
endif()

# Create static library
add_library(vizly_static STATIC ${VIZLY_SOURCES})
target_include_directories(vizly_static PUBLIC include)

# Create shared library
add_library(vizly SHARED ${VIZLY_SOURCES})
target_include_directories(vizly PUBLIC include)

# Link libraries
target_link_libraries(vizly ${OPENGL_LIBRARIES})
target_link_libraries(vizly_static ${OPENGL_LIBRARIES})

if(CUDA_FOUND AND VIZLY_GPU_SUPPORT)
    target_link_libraries(vizly ${CUDA_LIBRARIES})
    target_link_libraries(vizly_static ${CUDA_LIBRARIES})
endif()

if(OpenCL_FOUND AND VIZLY_GPU_SUPPORT)
    target_link_libraries(vizly ${OpenCL_LIBRARIES})
    target_link_libraries(vizly_static ${OpenCL_LIBRARIES})
endif()

# Examples
if(VIZLY_BUILD_EXAMPLES)
    add_subdirectory(examples)
endif()

# Install
install(TARGETS vizly vizly_static
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)

install(DIRECTORY include/vizly DESTINATION include)

# Package configuration
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    VizlyConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

configure_file(VizlyConfig.cmake.in VizlyConfig.cmake @ONLY)

install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/VizlyConfig.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/VizlyConfigVersion.cmake
    DESTINATION lib/cmake/Vizly
)