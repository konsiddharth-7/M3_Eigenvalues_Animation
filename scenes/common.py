"""Shared visual styling, MathJax-SVG equation rendering, and geometric helpers."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

import numpy as np
from manim import (
    ApplyMatrix,
    Arrow,
    DashedLine,
    DOWN,
    DR,
    FadeIn,
    FadeOut,
    LEFT,
    NumberPlane,
    RIGHT,
    RoundedRectangle,
    SVGMobject,
    SurroundingRectangle,
    Text,
    UP,
    VGroup,
    config,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEX_CACHE_DIR = PROJECT_ROOT / "assets" / "tex_cache"
MATHJAX_SCRIPT = PROJECT_ROOT / "assets" / "mathjax" / "tex2svg.mjs"

# ---------------------------------------------------------------------------
# Consistent Color Palette (Mathematics-Documentary Aesthetic)
# ---------------------------------------------------------------------------
BG_COLOR = "#0F172A"           # Dark navy background
CARD_BG = "#162033"            # Slightly lighter navy card surface
CARD_BORDER = "#334155"        # Crisp slate card border
GRID_MAJOR = "#334155"         # Main coordinate grid lines
GRID_MINOR = "#1E293B"         # Subtle sub-grid lines
AXIS_COLOR = "#CBD5E1"         # Clean X/Y axes

TEXT_WHITE = "#F8FAFC"         # White mathematical equations & headings
TEXT_MUTED = "#94A3B8"         # Secondary explanations & labels
ORIGINAL_CYAN = "#38BDF8"      # Original vectors & inputs
TRANSFORMED_ORANGE = "#FB923C" # Transformed vectors & outputs
EIGEN_GREEN = "#4ADE80"        # Eigenvectors & invariant directions
RESULT_YELLOW = "#FACC15"      # Eigenvalues & key results
ACCENT_RED = "#F87171"         # Highlighting contrast / singularity cue

FONT_FAMILY = "Helvetica Neue"

# Worked example matrix A = [[2, 1], [1, 2]]
MATRIX_A = np.array([[2.0, 1.0], [1.0, 2.0]])


def configure_scene_background() -> None:
    """Apply consistent dark navy background across all scenes."""
    config.background_color = BG_COLOR


def _render_mathjax_svg(latex: str, display: bool = True) -> Path:
    """Render a LaTeX expression to a standalone vector SVG via MathJax (cached)."""
    TEX_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(f"{int(display)}::{latex}".encode("utf-8")).hexdigest()[:24]
    svg_path = TEX_CACHE_DIR / f"{key}.svg"
    if svg_path.exists():
        return svg_path

    payload = json.dumps({"latex": latex, "display": display})
    proc = subprocess.run(
        ["node", str(MATHJAX_SCRIPT)],
        input=payload,
        text=True,
        capture_output=True,
        check=True,
    )
    svg_markup = json.loads(proc.stdout)
    svg_path.write_text(svg_markup, encoding="utf-8")
    return svg_path


def _extract_svg_ex_height(svg_path: Path) -> float:
    """Read MathJax's height attribute in ex units for proportional scaling."""
    text = svg_path.read_text(encoding="utf-8")
    match = re.search(r'height="([0-9.]+)ex"', text)
    if match:
        return float(match.group(1))
    return 2.0


def math_tex(
    latex: str,
    color: str | None = TEXT_WHITE,
    scale: float = 1.0,
    display: bool = True,
    max_width: float | None = None,
) -> SVGMobject:
    """Create a crisp Manim SVGMobject from a LaTeX math string."""
    svg_path = _render_mathjax_svg(latex, display=display)
    ex_height = _extract_svg_ex_height(svg_path)
    mob = SVGMobject(str(svg_path))
    if color is not None:
        mob.set_fill(color, opacity=1.0)
        mob.set_stroke(color, width=0)
    else:
        mob.set_stroke(width=0)
    # 1 ex ~ 0.19 Manim units at scale=1.0 gives clean ~38pt equivalent legibility at 1080p
    mob.set(height=ex_height * 0.19 * scale)
    if max_width is not None and mob.width > max_width:
        mob.scale_to_fit_width(max_width)
    return mob


def txt(
    content: str,
    size: float = 28,
    color: str = TEXT_WHITE,
    weight: str = "NORMAL",
    max_width: float | None = None,
) -> Text:
    """Create consistently styled sans-serif typography."""
    mob = Text(content, font=FONT_FAMILY, font_size=size, color=color, weight=weight)
    if max_width is not None and mob.width > max_width:
        mob.scale_to_fit_width(max_width)
    return mob


def fit_to_width(mob, max_width: float):
    """Scale down a mobject only if it exceeds max_width."""
    if mob.width > max_width:
        mob.scale_to_fit_width(max_width)
    return mob


def make_card(
    width: float,
    height: float,
    border_color: str = CARD_BORDER,
    fill_color: str = CARD_BG,
    fill_opacity: float = 0.92,
    corner_radius: float = 0.16,
    stroke_width: float = 1.8,
) -> RoundedRectangle:
    """Create a clean container panel for equations or summaries."""
    return RoundedRectangle(
        width=width,
        height=height,
        corner_radius=corner_radius,
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        stroke_color=border_color,
        stroke_width=stroke_width,
    )


def highlight_box(
    mob,
    color: str = RESULT_YELLOW,
    buff: float = 0.14,
    corner_radius: float = 0.08,
    stroke_width: float = 2.5,
) -> SurroundingRectangle:
    """Create a yellow highlight frame around an equation or result."""
    return SurroundingRectangle(
        mob,
        color=color,
        buff=buff,
        corner_radius=corner_radius,
        stroke_width=stroke_width,
    )


def build_plane(
    x_range: tuple[float, float, float] = (-5, 5, 1),
    y_range: tuple[float, float, float] = (-4, 4, 1),
    x_length: float = 8.4,
    y_length: float = 6.72,
    include_numbers: bool = True,
    font_size: float = 16,
) -> tuple[VGroup, Text, Text]:
    """Create a clean 2D Cartesian plane with labeled X and Y axes (no external LaTeX required)."""
    plane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        background_line_style={
            "stroke_color": GRID_MAJOR,
            "stroke_width": 1.3,
            "stroke_opacity": 0.55,
        },
        faded_line_style={
            "stroke_color": GRID_MINOR,
            "stroke_width": 0.7,
            "stroke_opacity": 0.35,
        },
        faded_line_ratio=2,
        axis_config={
            "color": AXIS_COLOR,
            "stroke_width": 2.4,
            "include_tip": True,
            "tip_width": 0.18,
            "tip_height": 0.18,
            "include_numbers": False,
        },
    )
    if include_numbers:
        num_labels = VGroup()
        x_min, x_max, x_step = x_range
        y_min, y_max, y_step = y_range
        for x in np.arange(x_min + x_step, x_max, x_step):
            val = int(round(x))
            if val == 0:
                continue
            lbl = Text(str(val), font=FONT_FAMILY, font_size=font_size, color=TEXT_MUTED)
            lbl.next_to(plane.c2p(x, 0), DOWN, buff=0.12)
            num_labels.add(lbl)
        for y in np.arange(y_min + y_step, y_max, y_step):
            val = int(round(y))
            if val == 0:
                continue
            lbl = Text(str(val), font=FONT_FAMILY, font_size=font_size, color=TEXT_MUTED)
            lbl.next_to(plane.c2p(0, y), LEFT, buff=0.12)
            num_labels.add(lbl)
        plane.add(num_labels)

    x_label = Text("X", font=FONT_FAMILY, font_size=22, color=AXIS_COLOR, weight="BOLD")
    y_label = Text("Y", font=FONT_FAMILY, font_size=22, color=AXIS_COLOR, weight="BOLD")
    x_label.next_to(plane.x_axis.get_end(), DOWN + LEFT * 0.15, buff=0.14)
    y_label.next_to(plane.y_axis.get_end(), LEFT + DOWN * 0.1, buff=0.16)
    return plane, x_label, y_label


def make_vector(
    plane: NumberPlane,
    coords: tuple[float, float] | list[float] | np.ndarray,
    color: str = ORIGINAL_CYAN,
    stroke_width: float = 4.5,
    max_tip_length_to_length_ratio: float = 0.22,
) -> Arrow:
    """Create a vector arrow anchored at the plane's origin to logical coordinates."""
    start = plane.c2p(0, 0)
    end = plane.c2p(float(coords[0]), float(coords[1]))
    return Arrow(
        start,
        end,
        buff=0,
        color=color,
        stroke_width=stroke_width,
        tip_length=0.22,
        max_tip_length_to_length_ratio=max_tip_length_to_length_ratio,
    )


def apply_matrix_coords(matrix: np.ndarray, coords: tuple[float, float] | list[float]) -> np.ndarray:
    """Compute matrix * [x, y]^T accurately."""
    vec = np.array([float(coords[0]), float(coords[1])], dtype=float)
    return matrix @ vec


def plane_linear_transform_matrix(plane: NumberPlane, matrix_2x2: np.ndarray) -> np.ndarray:
    """Convert a 2x2 logical coordinate matrix into Manim scene-space 2x2 matrix for ApplyMatrix."""
    sx = plane.x_axis.get_unit_size()
    sy = plane.y_axis.get_unit_size()
    scale_mat = np.diag([sx, sy])
    inv_scale_mat = np.diag([1.0 / sx, 1.0 / sy])
    return scale_mat @ matrix_2x2 @ inv_scale_mat


def build_warping_grid(
    ref_plane: NumberPlane,
    grid_radius: int = 4,
    line_color: str = ORIGINAL_CYAN,
    line_opacity: float = 0.35,
) -> NumberPlane:
    """Create an unnumbered overlay grid aligned with ref_plane that can be warped via ApplyMatrix."""
    ux = ref_plane.x_axis.get_unit_size()
    uy = ref_plane.y_axis.get_unit_size()
    grid = NumberPlane(
        x_range=(-grid_radius, grid_radius, 1),
        y_range=(-grid_radius, grid_radius, 1),
        x_length=2 * grid_radius * ux,
        y_length=2 * grid_radius * uy,
        background_line_style={
            "stroke_color": line_color,
            "stroke_width": 1.6,
            "stroke_opacity": line_opacity,
        },
        faded_line_style={
            "stroke_color": line_color,
            "stroke_width": 0.7,
            "stroke_opacity": line_opacity * 0.4,
        },
        faded_line_ratio=2,
        axis_config={
            "color": line_color,
            "stroke_width": 1.8,
            "stroke_opacity": line_opacity * 1.3,
            "include_tip": False,
            "include_numbers": False,
        },
    )
    grid.move_to(ref_plane.c2p(0, 0))
    return grid


def make_eigen_line(
    plane: NumberPlane,
    direction: tuple[float, float],
    extent: float = 4.2,
    color: str = EIGEN_GREEN,
    stroke_width: float = 2.4,
    stroke_opacity: float = 0.65,
) -> DashedLine:
    """Create a dashed invariant span line through the origin along an eigenvector direction."""
    dx, dy = direction
    norm = float(np.hypot(dx, dy))
    ux, uy = dx / norm * extent, dy / norm * extent
    return DashedLine(
        plane.c2p(-ux, -uy),
        plane.c2p(ux, uy),
        color=color,
        stroke_width=stroke_width,
        stroke_opacity=stroke_opacity,
        dash_length=0.18,
    )


def header_bar(title_text: str, subtitle_text: str = "", accent: str = ORIGINAL_CYAN) -> VGroup:
    """Create a clean top-left documentary section header."""
    bar = RoundedRectangle(
        width=0.08,
        height=0.52 if subtitle_text else 0.36,
        corner_radius=0.04,
        fill_color=accent,
        fill_opacity=1.0,
        stroke_width=0,
    )
    title = txt(title_text, size=26, color=TEXT_WHITE, weight="BOLD")
    if subtitle_text:
        sub = txt(subtitle_text, size=18, color=TEXT_MUTED)
        sub.next_to(title, DOWN, aligned_edge=LEFT, buff=0.06)
        text_group = VGroup(title, sub)
    else:
        text_group = VGroup(title)
    bar.next_to(text_group, LEFT, buff=0.16)
    group = VGroup(bar, text_group)
    group.to_corner(UP + LEFT, buff=0.38)
    return group


def fade_out_all(scene, run_time: float = 0.7) -> None:
    """Fade out all active mobjects cleanly to prevent jump cuts."""
    if scene.mobjects:
        scene.play(FadeOut(*scene.mobjects), run_time=run_time)


def scene_intro(scene, mobjects: list, run_time: float = 0.7) -> None:
    """Fade in initial mobjects smoothly."""
    scene.play(*[FadeIn(m) for m in mobjects], run_time=run_time)
