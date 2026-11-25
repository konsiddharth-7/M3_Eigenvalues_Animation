"""Scene 2 (0:35 - 1:15, 40s): Understanding Linear Transformations."""

from __future__ import annotations

import numpy as np
from manim import (
    Arc,
    ApplyMatrix,
    Brace,
    Create,
    DOWN,
    FadeIn,
    FadeOut,
    LEFT,
    RIGHT,
    Scene,
    Transform,
    UP,
    VGroup,
    Write,
    smooth,
)

from scenes.common import (
    BG_COLOR,
    CARD_BORDER,
    EIGEN_GREEN,
    MATRIX_A,
    ORIGINAL_CYAN,
    RESULT_YELLOW,
    TEXT_MUTED,
    TEXT_WHITE,
    TRANSFORMED_ORANGE,
    apply_matrix_coords,
    build_plane,
    build_warping_grid,
    configure_scene_background,
    fade_out_all,
    header_bar,
    highlight_box,
    make_card,
    make_eigen_line,
    make_vector,
    math_tex,
    plane_linear_transform_matrix,
    txt,
)


class Scene2Transformations(Scene):
    """Scene 2: Geometric meaning of matrix-vector multiplication (40s)."""

    def construct(self) -> None:
        configure_scene_background()
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 0:35 - 0:42 (7.0s): Header, Split Layout, Matrix A & Vector v
        # ------------------------------------------------------------------
        header = header_bar(
            "UNDERSTANDING LINEAR TRANSFORMATIONS",
            "How a 2 × 2 matrix acts on vectors in space",
            accent=ORIGINAL_CYAN,
        )
        header.set_z_index(10)

        # Left algebra panel (high z-index so warping grid never overlaps equations)
        left_panel = make_card(6.1, 5.75, border_color=CARD_BORDER, fill_opacity=0.98)
        left_panel.move_to([-3.65, -0.55, 0])
        left_panel.set_z_index(5)

        # Right coordinate plane
        plane, x_label, y_label = build_plane(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            x_length=5.6,
            y_length=5.6,
            include_numbers=True,
            font_size=14,
        )
        plane.move_to([3.3, -0.55, 0])
        x_label.next_to(plane.x_axis.get_end(), DOWN + LEFT * 0.12, buff=0.1)
        y_label.next_to(plane.y_axis.get_end(), LEFT + DOWN * 0.08, buff=0.12)
        plane.set_z_index(1)
        x_label.set_z_index(2)
        y_label.set_z_index(2)

        warping_grid = build_warping_grid(plane, grid_radius=3, line_color=ORIGINAL_CYAN, line_opacity=0.30)
        warping_grid.set_z_index(1)
        origin = plane.c2p(0, 0)

        mat_eq = math_tex(
            r"A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}",
            color=TEXT_WHITE,
            scale=1.0,
        )
        vec_eq = math_tex(
            r"\mathbf{v} = \begin{bmatrix} x \\ y \end{bmatrix}",
            color=ORIGINAL_CYAN,
            scale=1.0,
        )
        top_row = VGroup(mat_eq, vec_eq).arrange(RIGHT, buff=0.7)
        top_row.move_to([-3.65, 1.45, 0]).set_z_index(6)

        self.play(
            FadeIn(header),
            FadeIn(left_panel),
            FadeIn(plane),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(warping_grid),
            run_time=1.2,
        )
        self.play(FadeIn(mat_eq, shift=UP * 0.1), run_time=1.3)
        self.play(FadeIn(vec_eq, shift=UP * 0.1), run_time=1.3)
        self.wait(3.2)

        # ------------------------------------------------------------------
        # 0:42 - 0:54 (12.0s): Matrix-Vector Multiplication & Sample Vector
        # ------------------------------------------------------------------
        mult_eq = math_tex(
            r"\color{#FB923C}{A\mathbf{v}} = \color{#F8FAFC}{\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}} \color{#38BDF8}{\begin{bmatrix} x \\ y \end{bmatrix}} = \color{#FB923C}{\begin{bmatrix} 2x + y \\ x + 2y \end{bmatrix}}",
            color=None,
            scale=0.92,
            max_width=5.55,
        )
        mult_eq.move_to([-3.65, 0.05, 0]).set_z_index(6)
        mult_box = highlight_box(mult_eq, color=TRANSFORMED_ORANGE, buff=0.12).set_z_index(6)

        self.play(FadeIn(mult_eq, shift=UP * 0.1), run_time=2.0)
        self.play(Create(mult_box), run_time=0.8)
        self.wait(1.7)

        # Concrete sample vector v_a = [1, 0]^T -> [2, 1]^T
        ex_calc = math_tex(
            r"\color{#38BDF8}{\mathbf{v}_a = \begin{bmatrix} 1 \\ 0 \end{bmatrix}} \;\longrightarrow\; \color{#FB923C}{A\mathbf{v}_a = \begin{bmatrix} 2 \\ 1 \end{bmatrix}}",
            color=None,
            scale=0.86,
            max_width=5.5,
        )
        ex_calc.move_to([-3.65, -1.35, 0]).set_z_index(6)

        va_orig = make_vector(plane, (1, 0), color=ORIGINAL_CYAN, stroke_width=4.8).set_z_index(3)
        va_ghost = make_vector(plane, (1, 0), color=ORIGINAL_CYAN, stroke_width=3.0).set_opacity(0.45).set_z_index(2)
        va_lbl = math_tex(r"\mathbf{v}_a", color=ORIGINAL_CYAN, scale=0.75).next_to(
            plane.c2p(1, 0), DOWN, buff=0.12
        ).set_z_index(4)

        va_trans = make_vector(plane, (2, 1), color=TRANSFORMED_ORANGE, stroke_width=4.8).set_z_index(3)
        va_trans_lbl = math_tex(r"A\mathbf{v}_a", color=TRANSFORMED_ORANGE, scale=0.75).next_to(
            plane.c2p(2, 1), UP + RIGHT * 0.1, buff=0.10
        ).set_z_index(4)

        self.play(FadeIn(ex_calc, shift=UP * 0.1), Create(va_orig), FadeIn(va_lbl), run_time=1.8)
        self.add(va_ghost)
        self.wait(1.2)
        self.play(
            Create(va_trans),
            FadeIn(va_trans_lbl),
            run_time=1.8,
        )
        self.wait(2.7)

        # ------------------------------------------------------------------
        # 0:54 - 1:07 (13.0s): Transform Multiple Vectors & Compare Dir vs Mag
        # ------------------------------------------------------------------
        extra_coords = [
            (0.0, 1.0),
            (-1.0, 0.5),
            (1.5, -0.5),
        ]
        extra_orig = VGroup(*[make_vector(plane, c, color=ORIGINAL_CYAN, stroke_width=4.0).set_z_index(3) for c in extra_coords])
        extra_ghosts = VGroup(*[
            make_vector(plane, c, color=ORIGINAL_CYAN, stroke_width=2.4).set_opacity(0.35).set_z_index(2)
            for c in extra_coords
        ])
        extra_targets = [
            make_vector(plane, apply_matrix_coords(MATRIX_A, c), color=TRANSFORMED_ORANGE, stroke_width=4.0).set_z_index(3)
            for c in extra_coords
        ]

        self.play(
            FadeOut(va_orig),
            FadeOut(va_lbl),
            *[Create(v) for v in extra_orig],
            run_time=1.5,
        )
        self.add(extra_ghosts)

        mat_scene = plane_linear_transform_matrix(plane, MATRIX_A)
        self.play(
            ApplyMatrix(mat_scene, warping_grid, about_point=origin, run_time=3.2, rate_func=smooth),
            *[Transform(v, tgt, run_time=3.2, rate_func=smooth) for v, tgt in zip(extra_orig, extra_targets)],
        )
        self.wait(0.8)

        # Highlight Direction change vs Magnitude change on [1, 0] -> [2, 1]
        dir_arc = Arc(
            radius=0.82,
            start_angle=0.0,
            angle=float(np.arctan2(1.0, 2.0)),
            arc_center=origin,
            color=RESULT_YELLOW,
            stroke_width=3.2,
        ).set_z_index(4)
        theta_lbl = math_tex(r"\Delta\theta", color=RESULT_YELLOW, scale=0.7).next_to(dir_arc, RIGHT, buff=0.08).set_z_index(4)

        takeaway_box = txt(
            "A matrix maps vectors by changing direction & magnitude.",
            size=20,
            color=TEXT_WHITE,
            weight="BOLD",
            max_width=5.55,
        )
        mag_note = math_tex(
            r"\|\mathbf{v}_a\| = 1 \;\longrightarrow\; \|A\mathbf{v}_a\| = \sqrt{5} \approx 2.24",
            color=RESULT_YELLOW,
            scale=0.78,
            max_width=5.5,
        )
        bottom_notes = VGroup(mag_note, takeaway_box).arrange(DOWN, buff=0.22)
        bottom_notes.move_to([-3.65, -2.55, 0]).set_z_index(6)

        self.play(Create(dir_arc), FadeIn(theta_lbl), FadeIn(bottom_notes, shift=UP * 0.1), run_time=2.0)
        self.wait(5.5)

        # ------------------------------------------------------------------
        # 1:07 - 1:15 (8.0s): Transition to Special Invariant Directions
        # ------------------------------------------------------------------
        line_yx = make_eigen_line(plane, (1, 1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.5).set_z_index(3)
        line_ynx = make_eigen_line(plane, (1, -1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.5).set_z_index(3)
        e1 = make_vector(plane, (3, 3), color=EIGEN_GREEN, stroke_width=5.0).set_z_index(4)
        e2 = make_vector(plane, (1, -1), color=EIGEN_GREEN, stroke_width=5.0).set_z_index(4)

        bridge_txt = txt(
            "Next: What about directions that NEVER rotate?",
            size=21,
            color=EIGEN_GREEN,
            weight="BOLD",
            max_width=5.55,
        ).move_to([-3.65, -2.85, 0]).set_z_index(6)

        self.play(
            *[v.animate.set_opacity(0.22) for v in extra_orig],
            *[g.animate.set_opacity(0.15) for g in extra_ghosts],
            va_trans.animate.set_opacity(0.22),
            va_ghost.animate.set_opacity(0.15),
            FadeOut(dir_arc),
            FadeOut(theta_lbl),
            FadeOut(va_trans_lbl),
            FadeOut(bottom_notes),
            Create(line_yx),
            Create(line_ynx),
            Create(e1),
            Create(e2),
            FadeIn(bridge_txt),
            run_time=2.5,
        )
        self.wait(4.8)
        fade_out_all(self, run_time=0.7)
