"""
Pure Python Rendering Engine
============================

A high-performance rendering engine built with only NumPy as dependency.
Supports SVG, PNG, and HTML Canvas output without matplotlib.
"""

from __future__ import annotations

import base64
import io
import math
import struct
import zlib
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union
import warnings

import numpy as np


@dataclass
class Color:
    """Pure Python color representation."""
    r: float
    g: float
    b: float
    a: float = 1.0

    @classmethod
    def from_hex(cls, hex_color: str) -> 'Color':
        """Create color from hex string (#RRGGBB or #RRGGBBAA)."""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 6:
            r, g, b = [int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
            return cls(r, g, b, 1.0)
        elif len(hex_color) == 8:
            r, g, b, a = [int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4, 6)]
            return cls(r, g, b, a)
        else:
            raise ValueError(f"Invalid hex color: {hex_color}")

    @classmethod
    def from_name(cls, name: str) -> 'Color':
        """Create color from named color."""
        colors = {
            'red': (1.0, 0.0, 0.0),
            'green': (0.0, 1.0, 0.0),
            'blue': (0.0, 0.0, 1.0),
            'black': (0.0, 0.0, 0.0),
            'white': (1.0, 1.0, 1.0),
            'gray': (0.5, 0.5, 0.5),
            'grey': (0.5, 0.5, 0.5),
            'orange': (1.0, 0.5, 0.0),
            'purple': (0.5, 0.0, 0.5),
            'yellow': (1.0, 1.0, 0.0),
            'cyan': (0.0, 1.0, 1.0),
            'magenta': (1.0, 0.0, 1.0),
            'skyblue': (0.53, 0.81, 0.98),
            'lightblue': (0.68, 0.85, 0.90),
            'darkblue': (0.0, 0.0, 0.55),
            'lightgreen': (0.56, 0.93, 0.56),
            'darkgreen': (0.0, 0.39, 0.0),
            'pink': (1.0, 0.75, 0.80),
            'brown': (0.65, 0.16, 0.16),
            'gold': (1.0, 0.84, 0.0),
            'silver': (0.75, 0.75, 0.75),
        }
        if name.lower() in colors:
            r, g, b = colors[name.lower()]
            return cls(r, g, b, 1.0)
        else:
            raise ValueError(f"Unknown color name: {name}")

    def to_hex(self) -> str:
        """Convert to hex string."""
        r = int(self.r * 255)
        g = int(self.g * 255)
        b = int(self.b * 255)
        if self.a < 1.0:
            a = int(self.a * 255)
            return f"#{r:02x}{g:02x}{b:02x}{a:02x}"
        else:
            return f"#{r:02x}{g:02x}{b:02x}"

    def to_rgb_tuple(self) -> Tuple[int, int, int]:
        """Convert to RGB tuple (0-255)."""
        return (int(self.r * 255), int(self.g * 255), int(self.b * 255))


class PureCanvas:
    """Pure Python canvas for drawing operations."""

    def __init__(self, width: int, height: int, background: Color = None):
        self.width = width
        self.height = height
        self.background = background or Color(1.0, 1.0, 1.0, 1.0)  # White

        # Create RGBA pixel buffer
        self.pixels = np.ones((height, width, 4), dtype=np.float32)
        self.pixels[:, :] = [self.background.r, self.background.g, self.background.b, self.background.a]

        # Drawing state
        self.stroke_color = Color(0.0, 0.0, 0.0, 1.0)  # Black
        self.fill_color = Color(0.5, 0.5, 0.5, 1.0)    # Gray
        self.line_width = 1.0

        # Transform matrix [scale_x, scale_y, translate_x, translate_y]
        self.transform = np.array([1.0, 1.0, 0.0, 0.0])

        # SVG elements tracking for export
        self.svg_elements = []

    def set_stroke_color(self, color: Union[Color, str]):
        """Set stroke color."""
        if isinstance(color, str):
            if color.startswith('#'):
                self.stroke_color = Color.from_hex(color)
            else:
                self.stroke_color = Color.from_name(color)
        else:
            self.stroke_color = color

    def set_fill_color(self, color: Union[Color, str]):
        """Set fill color."""
        if isinstance(color, str):
            if color.startswith('#'):
                self.fill_color = Color.from_hex(color)
            else:
                self.fill_color = Color.from_name(color)
        else:
            self.fill_color = color

    def set_line_width(self, width: float):
        """Set line width."""
        self.line_width = width

    def _transform_point(self, x: float, y: float) -> Tuple[int, int]:
        """Apply transformation to a point."""
        tx = int(x * self.transform[0] + self.transform[2])
        ty = int(y * self.transform[1] + self.transform[3])
        return tx, ty

    def _set_pixel(self, x: int, y: int, color: Color):
        """Set a pixel with bounds checking."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y, x] = [color.r, color.g, color.b, color.a]

    def _draw_line_bresenham(self, x0: int, y0: int, x1: int, y1: int, color: Color):
        """Draw line using Bresenham's algorithm."""
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        x, y = x0, y0
        while True:
            self._set_pixel(x, y, color)

            if x == x1 and y == y1:
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

    def draw_line(self, x0: float, y0: float, x1: float, y1: float):
        """Draw a line."""
        tx0, ty0 = self._transform_point(x0, y0)
        tx1, ty1 = self._transform_point(x1, y1)
        self._draw_line_bresenham(tx0, ty0, tx1, ty1, self.stroke_color)

        # Track SVG element
        svg_line = f'<line x1="{tx0}" y1="{ty0}" x2="{tx1}" y2="{ty1}" stroke="{self.stroke_color.to_hex()}" stroke-width="{self.line_width}"/>'
        self.svg_elements.append(svg_line)

    def draw_rectangle(self, x: float, y: float, width: float, height: float, fill: bool = True):
        """Draw a rectangle."""
        tx, ty = self._transform_point(x, y)
        tw = int(width * self.transform[0])
        th = int(height * self.transform[1])

        if fill:
            # Fill rectangle
            for py in range(ty, ty + th):
                for px in range(tx, tx + tw):
                    self._set_pixel(px, py, self.fill_color)

        # Draw border
        self._draw_line_bresenham(tx, ty, tx + tw, ty, self.stroke_color)
        self._draw_line_bresenham(tx + tw, ty, tx + tw, ty + th, self.stroke_color)
        self._draw_line_bresenham(tx + tw, ty + th, tx, ty + th, self.stroke_color)
        self._draw_line_bresenham(tx, ty + th, tx, ty, self.stroke_color)

        # Track SVG element
        if fill:
            svg_rect = f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" fill="{self.fill_color.to_hex()}" stroke="{self.stroke_color.to_hex()}" stroke-width="{self.line_width}"/>'
        else:
            svg_rect = f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" fill="none" stroke="{self.stroke_color.to_hex()}" stroke-width="{self.line_width}"/>'
        self.svg_elements.append(svg_rect)

    def draw_circle(self, cx: float, cy: float, radius: float, fill: bool = True):
        """Draw a circle using midpoint circle algorithm."""
        tcx, tcy = self._transform_point(cx, cy)
        tr = int(radius * min(self.transform[0], self.transform[1]))

        def plot_circle_points(x: int, y: int):
            points = [
                (tcx + x, tcy + y), (tcx - x, tcy + y),
                (tcx + x, tcy - y), (tcx - x, tcy - y),
                (tcx + y, tcy + x), (tcx - y, tcy + x),
                (tcx + y, tcy - x), (tcx - y, tcy - x)
            ]
            for px, py in points:
                self._set_pixel(px, py, self.stroke_color)

            if fill:
                # Fill horizontal lines
                for fx in range(tcx - x, tcx + x + 1):
                    self._set_pixel(fx, tcy + y, self.fill_color)
                    self._set_pixel(fx, tcy - y, self.fill_color)
                for fx in range(tcx - y, tcx + y + 1):
                    self._set_pixel(fx, tcy + x, self.fill_color)
                    self._set_pixel(fx, tcy - x, self.fill_color)

        x, y = 0, tr
        d = 1 - tr

        plot_circle_points(x, y)

        while x < y:
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x - y) + 5
                y -= 1
            x += 1
            plot_circle_points(x, y)

        # Track SVG element
        if fill:
            svg_circle = f'<circle cx="{tcx}" cy="{tcy}" r="{tr}" fill="{self.fill_color.to_hex()}" stroke="{self.stroke_color.to_hex()}" stroke-width="{self.line_width}"/>'
        else:
            svg_circle = f'<circle cx="{tcx}" cy="{tcy}" r="{tr}" fill="none" stroke="{self.stroke_color.to_hex()}" stroke-width="{self.line_width}"/>'
        self.svg_elements.append(svg_circle)

    def draw_polyline(self, points: List[Tuple[float, float]]):
        """Draw connected line segments."""
        if len(points) < 2:
            return

        for i in range(len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            self.draw_line(x0, y0, x1, y1)

    def draw_text(self, text: str, x: float, y: float, font_size: int = 12, color: str = 'black'):
        """Draw text at specified position."""
        # Convert coordinates
        tx, ty = self._transform_point(x, y)

        # Track SVG text element
        svg_color = color
        if isinstance(color, Color):
            svg_color = color.to_hex()
        elif not color.startswith('#'):
            # Convert named color to hex
            color_obj = Color.from_name(color)
            svg_color = color_obj.to_hex()

        svg_text = f'<text x="{tx}" y="{ty}" font-size="{font_size}" fill="{svg_color}" font-family="Arial, sans-serif">{text}</text>'
        self.svg_elements.append(svg_text)

    def draw_axes(self, x_min: float, x_max: float, y_min: float, y_max: float):
        """Draw coordinate axes with proper scaling and tick marks."""
        # Set axis color
        axis_color = Color(0.0, 0.0, 0.0, 1.0)  # Black
        original_color = self.stroke_color
        self.set_stroke_color(axis_color)

        # Calculate chart margins (leave space for labels)
        margin_left = 60
        margin_bottom = 50
        margin_top = 40
        margin_right = 40

        # Chart bounds in pixel coordinates
        chart_left = margin_left
        chart_right = self.width - margin_right
        chart_bottom = self.height - margin_bottom
        chart_top = margin_top

        # Draw main axis lines (chart boundaries)
        # Bottom X-axis
        svg_line = f'<line x1="{chart_left}" y1="{chart_bottom}" x2="{chart_right}" y2="{chart_bottom}" stroke="{axis_color.to_hex()}" stroke-width="2"/>'
        self.svg_elements.append(svg_line)

        # Left Y-axis
        svg_line = f'<line x1="{chart_left}" y1="{chart_top}" x2="{chart_left}" y2="{chart_bottom}" stroke="{axis_color.to_hex()}" stroke-width="2"/>'
        self.svg_elements.append(svg_line)

        # Draw tick marks and labels
        num_x_ticks = 6
        num_y_ticks = 6

        # X-axis ticks and labels
        x_step = (x_max - x_min) / (num_x_ticks - 1)
        for i in range(num_x_ticks):
            x_val = x_min + i * x_step
            x_pixel = chart_left + (i / (num_x_ticks - 1)) * (chart_right - chart_left)

            # Tick mark
            tick_line = f'<line x1="{x_pixel}" y1="{chart_bottom}" x2="{x_pixel}" y2="{chart_bottom + 5}" stroke="{axis_color.to_hex()}" stroke-width="1"/>'
            self.svg_elements.append(tick_line)

            # Tick label
            label_text = f"{x_val:.1f}"
            tick_label = f'<text x="{x_pixel}" y="{chart_bottom + 20}" font-size="12" fill="{axis_color.to_hex()}" font-family="Arial, sans-serif" text-anchor="middle">{label_text}</text>'
            self.svg_elements.append(tick_label)

        # Y-axis ticks and labels
        y_step = (y_max - y_min) / (num_y_ticks - 1)
        for i in range(num_y_ticks):
            y_val = y_min + i * y_step
            y_pixel = chart_bottom - (i / (num_y_ticks - 1)) * (chart_bottom - chart_top)

            # Tick mark
            tick_line = f'<line x1="{chart_left - 5}" y1="{y_pixel}" x2="{chart_left}" y2="{y_pixel}" stroke="{axis_color.to_hex()}" stroke-width="1"/>'
            self.svg_elements.append(tick_line)

            # Tick label
            label_text = f"{y_val:.1f}"
            tick_label = f'<text x="{chart_left - 10}" y="{y_pixel + 4}" font-size="12" fill="{axis_color.to_hex()}" font-family="Arial, sans-serif" text-anchor="end">{label_text}</text>'
            self.svg_elements.append(tick_label)

        # Store chart bounds for future use
        self.chart_bounds = {
            'left': chart_left,
            'right': chart_right,
            'top': chart_top,
            'bottom': chart_bottom,
            'x_min': x_min,
            'x_max': x_max,
            'y_min': y_min,
            'y_max': y_max
        }

        # Restore original color
        self.set_stroke_color(original_color)

    def draw_grid(self, x_min: float, x_max: float, y_min: float, y_max: float,
                  num_x_lines: int = 5, num_y_lines: int = 5, alpha: float = 0.3):
        """Draw grid lines."""
        # Store current color
        original_color = self.stroke_color

        # Set grid color (light gray with alpha)
        grid_color = Color(0.8, 0.8, 0.8, alpha)
        self.set_stroke_color(grid_color)

        # Vertical grid lines
        x_step = (x_max - x_min) / num_x_lines
        for i in range(num_x_lines + 1):
            x = x_min + i * x_step
            self.draw_line(x, y_min, x, y_max)

        # Horizontal grid lines
        y_step = (y_max - y_min) / num_y_lines
        for i in range(num_y_lines + 1):
            y = y_min + i * y_step
            self.draw_line(x_min, y, x_max, y)

        # Restore original color
        self.set_stroke_color(original_color)

    def set_viewport(self, x_min: float, x_max: float, y_min: float, y_max: float):
        """Set viewport transformation."""
        scale_x = self.width / (x_max - x_min)
        scale_y = self.height / (y_max - y_min)
        translate_x = -x_min * scale_x
        translate_y = -y_min * scale_y

        self.transform = np.array([scale_x, scale_y, translate_x, translate_y])

    def to_png_bytes(self) -> bytes:
        """Export canvas as PNG bytes (pure Python implementation)."""
        # Convert float pixels to uint8
        pixel_data = (self.pixels[:, :, :3] * 255).astype(np.uint8)

        # PNG file structure
        def crc32(data):
            return zlib.crc32(data) & 0xffffffff

        def write_chunk(chunk_type, data):
            length = len(data)
            chunk = struct.pack('>I', length)
            chunk += chunk_type
            chunk += data
            chunk += struct.pack('>I', crc32(chunk_type + data))
            return chunk

        # PNG signature
        png_data = b'\x89PNG\r\n\x1a\n'

        # IHDR chunk
        ihdr_data = struct.pack('>IIBBBBB', self.width, self.height, 8, 2, 0, 0, 0)
        png_data += write_chunk(b'IHDR', ihdr_data)

        # IDAT chunk (compressed image data)
        raw_data = b''
        for row in pixel_data:
            raw_data += b'\x00'  # No filter
            raw_data += row.tobytes()

        compressed_data = zlib.compress(raw_data)
        png_data += write_chunk(b'IDAT', compressed_data)

        # IEND chunk
        png_data += write_chunk(b'IEND', b'')

        return png_data

    def to_svg(self) -> str:
        """Export canvas as SVG string."""
        svg_elements = []

        # SVG header
        svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{self.width}" height="{self.height}"
     viewBox="0 0 {self.width} {self.height}"
     xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="{self.background.to_hex()}"/>
'''

        # Add all tracked SVG elements
        for element in self.svg_elements:
            svg += element + '\n'

        svg += '</svg>'
        return svg


class PureRenderer:
    """Pure Python rendering engine."""

    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.canvas = PureCanvas(width, height)

    def create_figure(self, figsize: Tuple[float, float] = (8, 6), dpi: int = 100):
        """Create a new figure."""
        width = int(figsize[0] * dpi)
        height = int(figsize[1] * dpi)
        self.canvas = PureCanvas(width, height)
        return self

    def plot(self, x: np.ndarray, y: np.ndarray, color: str = 'blue', linewidth: float = 1.0):
        """Plot line chart."""
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")

        # Set up viewport
        x_min, x_max = float(np.min(x)), float(np.max(x))
        y_min, y_max = float(np.min(y)), float(np.max(y))

        # Add padding
        x_range = x_max - x_min
        y_range = y_max - y_min
        x_min -= x_range * 0.1
        x_max += x_range * 0.1
        y_min -= y_range * 0.1
        y_max += y_range * 0.1

        self.canvas.set_viewport(x_min, x_max, y_min, y_max)
        self.canvas.set_stroke_color(color)
        self.canvas.set_line_width(linewidth)

        # Draw line segments
        points = [(float(x[i]), float(y[i])) for i in range(len(x))]
        self.canvas.draw_polyline(points)

        return self

    def scatter(self, x: np.ndarray, y: np.ndarray, color: str = 'blue', size: float = 20):
        """Plot scatter chart."""
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")

        # Set up viewport
        x_min, x_max = float(np.min(x)), float(np.max(x))
        y_min, y_max = float(np.min(y)), float(np.max(y))

        # Add padding
        x_range = x_max - x_min
        y_range = y_max - y_min
        x_min -= x_range * 0.1
        x_max += x_range * 0.1
        y_min -= y_range * 0.1
        y_max += y_range * 0.1

        self.canvas.set_viewport(x_min, x_max, y_min, y_max)
        self.canvas.set_fill_color(color)

        # Draw points as small circles
        radius = size / 100.0  # Convert size to radius
        for i in range(len(x)):
            self.canvas.draw_circle(float(x[i]), float(y[i]), radius, fill=True)

        return self

    def bar(self, x: np.ndarray, height: np.ndarray, color: str = 'blue', width: float = 0.8):
        """Plot bar chart."""
        if len(x) != len(height):
            raise ValueError("x and height must have the same length")

        # Set up viewport
        x_min, x_max = float(np.min(x) - width/2), float(np.max(x) + width/2)
        y_min, y_max = 0.0, float(np.max(height) * 1.1)

        self.canvas.set_viewport(x_min, x_max, y_min, y_max)
        self.canvas.set_fill_color(color)

        # Draw bars
        for i in range(len(x)):
            bar_x = float(x[i]) - width/2
            bar_height = float(height[i])
            self.canvas.draw_rectangle(bar_x, 0, width, bar_height, fill=True)

        return self

    def save(self, filename: str, dpi: int = 100):
        """Save the figure to file."""
        if filename.lower().endswith('.png'):
            png_data = self.canvas.to_png_bytes()
            with open(filename, 'wb') as f:
                f.write(png_data)
        elif filename.lower().endswith('.svg'):
            svg_data = self.canvas.to_svg()
            with open(filename, 'w') as f:
                f.write(svg_data)
        else:
            raise ValueError(f"Unsupported file format: {filename}")

    def show(self):
        """Display the figure inline in Jupyter/Colab or print info."""
        try:
            # Try to display inline in Jupyter/Colab
            from IPython.display import display, HTML, SVG

            # Generate SVG for inline display
            svg_data = self.canvas.to_svg()
            display(SVG(svg_data))
            print(f"📊 VizlyChart rendered: {self.canvas.width}x{self.canvas.height} pixels")

        except ImportError:
            # Not in Jupyter environment
            print(f"Figure rendered: {self.canvas.width}x{self.canvas.height} pixels")
            print("Use .save() to export to PNG or SVG format")

        except Exception as e:
            # Fallback if SVG display fails
            print(f"📊 VizlyChart rendered: {self.canvas.width}x{self.canvas.height} pixels")
            print(f"⚠️  Inline display failed: {e}")
            print("Use .save() to export to PNG or SVG format")


# Alternative matplotlib-like interface
class pyplot:
    """Matplotlib-like interface for pure Python rendering."""

    _current_renderer = None

    @staticmethod
    def figure(figsize: Tuple[float, float] = (8, 6), dpi: int = 100):
        """Create a new figure."""
        pyplot._current_renderer = PureRenderer()
        pyplot._current_renderer.create_figure(figsize, dpi)
        return pyplot._current_renderer

    @staticmethod
    def plot(x: np.ndarray, y: np.ndarray, color: str = 'blue', linewidth: float = 1.0):
        """Plot line chart."""
        if pyplot._current_renderer is None:
            pyplot.figure()
        return pyplot._current_renderer.plot(x, y, color, linewidth)

    @staticmethod
    def scatter(x: np.ndarray, y: np.ndarray, color: str = 'blue', s: float = 20):
        """Plot scatter chart."""
        if pyplot._current_renderer is None:
            pyplot.figure()
        return pyplot._current_renderer.scatter(x, y, color, s)

    @staticmethod
    def bar(x: np.ndarray, height: np.ndarray, color: str = 'blue', width: float = 0.8):
        """Plot bar chart."""
        if pyplot._current_renderer is None:
            pyplot.figure()
        return pyplot._current_renderer.bar(x, height, color, width)

    @staticmethod
    def savefig(filename: str, dpi: int = 100):
        """Save the current figure."""
        if pyplot._current_renderer is not None:
            pyplot._current_renderer.save(filename, dpi)

    @staticmethod
    def show():
        """Show the current figure."""
        if pyplot._current_renderer is not None:
            pyplot._current_renderer.show()