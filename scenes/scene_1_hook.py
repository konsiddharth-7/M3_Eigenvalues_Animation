"""Scene 1 (0:00 - 0:35, 35s): The Hook — Introducing invariant directions."""

from __future__ import annotations

import numpy as np
from manim import (
    Arc,
    ApplyMatrix,
    Create,
    DOWN,
    FadeIn,
    FadeOut,
    Indicate,
    LEFT,
    RIGHT,
    Scene,
    SurroundingRectangle,
    Transform,
    UP,
    VGroup,
    Write,
    smooth,
)

from scenes.common import (
    AXIS_COLOR,
    BG_COLOR,
    CARD_BG,
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
    make_card,
    make_eigen_line,
    make_vector,
    math_tex,
    plane_linear_transform_matrix,
    txt,
)


class Scene1Hook(Scene):
    """Scene 1: Visual puzzle of vectors under a linear transformation (35s)."""

    def construct(self) -> None:
        configure_scene_background()
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 0:00 - 0:03.5 : Clean Opening Frame (M3 Assessment Requirement)
        # ------------------------------------------------------------------
        badge = txt(
            "LINEAR ALGEBRA & CALCULUS (M3)  •  INTERNAL ASSESSMENT",
            size=18,
            color=ORIGINAL_CYAN,
            weight="BOLD",
        )
        open_title = txt("EIGENVALUES & EIGENVECTORS", size=50, color=TEXT_WHITE, weight="BOLD")
        open_sub = txt(
            "Understanding invariant directions under linear transformations",
            size=24,
            color=TEXT_MUTED,
        )
        student_tag = txt("SIDDHARTH KONDERU   |   E25B070643", size=20, color=RESULT_YELLOW)

        opening_group = VGroup(badge, open_title, open_sub, student_tag).arrange(DOWN, buff=0.3)
        opening_card = make_card(11.2, 4.3, border_color=ORIGINAL_CYAN)
        opening_group.move_to(opening_card.get_center())
        opening_all = VGroup(opening_card, opening_group)

        self.play(FadeIn(opening_all, shift=UP * 0.15), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(opening_all), run_time=0.7)

        # ------------------------------------------------------------------
        # 0:03.5 - 0:09.5 : 2D Cartesian Grid & Multiple Origin Vectors
        # ------------------------------------------------------------------
        plane, x_label, y_label = build_plane(
            x_range=(-5, 5, 1),
            y_range=(-4, 4, 1),
            x_length=9.0,
            y_length=7.2,
            include_numbers=True,
        )
        warping_grid = build_warping_grid(plane, grid_radius=4, line_color=ORIGINAL_CYAN, line_opacity=0.28)
        origin = plane.c2p(0, 0)

        # Ordinary vectors (change direction & magnitude) + 2 special vectors on y=x and y=-x
        ordinary_coords = [
            (2.0, 0.0),
            (0.0, 1.5),
            (-2.0, 0.0),
            (0.0, -1.5),
            (2.0, -1.0),
            (-1.0, 2.0),
        ]
        eigen_coords = [
            (1.0, 1.0),    # maps to (3, 3) along y = x
            (1.5, -1.5),   # maps to (1.5, -1.5) along y = -x
        ]

        ordinary_vecs = VGroup(*[make_vector(plane, c, color=ORIGINAL_CYAN, stroke_width=4.2) for c in ordinary_coords])
        special_vecs = VGroup(*[make_vector(plane, c, color=ORIGINAL_CYAN, stroke_width=4.8) for c in eigen_coords])
        all_vecs = VGroup(*ordinary_vecs, *special_vecs)

        # Ghost references keep the original directions visible during motion
        ghost_vecs = VGroup(*[
            make_vector(plane, c, color=ORIGINAL_CYAN, stroke_width=2.4).set_opacity(0.28)
            for c in ordinary_coords + eigen_coords
        ])

        self.play(FadeIn(plane), FadeIn(x_label), FadeIn(y_label), FadeIn(warping_grid), run_time=1.4)
        self.play(*[Create(v) for v in all_vecs], run_time=1.8)
        self.add(ghost_vecs)
        self.wait(2.8)

        # ------------------------------------------------------------------
        # 0:09.5 - 0:18.5 : Apply Linear Transformation A = [[2,1],[1,2]]
        # ------------------------------------------------------------------
        mat_scene = plane_linear_transform_matrix(plane, MATRIX_A)

        ordinary_targets = [
            make_vector(plane, apply_matrix_coords(MATRIX_A, c), color=TRANSFORMED_ORANGE, stroke_width=4.2)
            for c in ordinary_coords
        ]
        special_targets = [
            make_vector(plane, apply_matrix_coords(MATRIX_A, c), color=TRANSFORMED_ORANGE, stroke_width=5.0)
            for c in eigen_coords
        ]

        transform_anims = [
            ApplyMatrix(mat_scene, warping_grid, about_point=origin, run_time=3.5, rate_func=smooth),
            *[Transform(v, tgt, run_time=3.5, rate_func=smooth) for v, tgt in zip(ordinary_vecs, ordinary_targets)],
            *[Transform(v, tgt, run_time=3.5, rate_func=smooth) for v, tgt in zip(special_vecs, special_targets)],
        ]
        self.play(*transform_anims)
        self.wait(1.0)

        # Show angle change arcs on two ordinary vectors to emphasize direction change
        # Vector (2,0) -> (4,2): angle 0 -> atan2(2, 4)
        arc1 = Arc(
            radius=1.1,
            start_angle=0.0,
            angle=float(np.arctan2(2.0, 4.0)),
            arc_center=origin,
            color=TRANSFORMED_ORANGE,
            stroke_width=3.0,
        )
        # Vector (0,1.5) -> (1.5,3): angle pi/2 -> atan2(3, 1.5)
        ang2_end = float(np.arctan2(3.0, 1.5))
        arc2 = Arc(
            radius=1.0,
            start_angle=np.pi / 2,
            angle=ang2_end - np.pi / 2,
            arc_center=origin,
            color=TRANSFORMED_ORANGE,
            stroke_width=3.0,
        )
        callout_shift = txt("Most vectors rotate and stretch", size=22, color=TRANSFORMED_ORANGE, weight="BOLD")
        callout_bg = make_card(4.6, 0.65, border_color=TRANSFORMED_ORANGE, fill_opacity=0.92)
        callout_shift.move_to(callout_bg.get_center())
        callout_box = VGroup(callout_bg, callout_shift).to_corner(UP + LEFT, buff=0.35)

        self.play(Create(arc1), Create(arc2), FadeIn(callout_box), run_time=1.2)
        self.wait(3.3)

        # ------------------------------------------------------------------
        # 0:18.5 - 0:27.5 : Highlight the Two Invariant Directions
        # ------------------------------------------------------------------
        line_yx = make_eigen_line(plane, (1, 1), extent=4.2, color=EIGEN_GREEN, stroke_width=2.6)
        line_ynx = make_eigen_line(plane, (1, -1), extent=4.2, color=EIGEN_GREEN, stroke_width=2.6)

        lbl_yx = math_tex(r"y = x", color=EIGEN_GREEN, scale=0.85).move_to(plane.c2p(3.5, 3.0))
        lbl_ynx = math_tex(r"y = -x", color=EIGEN_GREEN, scale=0.85).move_to(plane.c2p(3.3, -2.5))

        eigen_badge_bg = make_card(5.4, 0.65, border_color=EIGEN_GREEN, fill_opacity=0.92)
        eigen_badge_txt = txt("Two special vectors keep their exact direction", size=21, color=EIGEN_GREEN, weight="BOLD")
        eigen_badge_txt.move_to(eigen_badge_bg.get_center())
        eigen_badge = VGroup(eigen_badge_bg, eigen_badge_txt).to_corner(UP + LEFT, buff=0.35)

        self.play(
            FadeOut(arc1),
            FadeOut(arc2),
            FadeOut(callout_box),
            *[v.animate.set_opacity(0.18) for v in ordinary_vecs],
            *[g.animate.set_opacity(0.10) for g in ghost_vecs],
            warping_grid.animate.set_opacity(0.16),
            special_vecs[0].animate.set_color(EIGEN_GREEN).set_stroke(width=6.5),
            special_vecs[1].animate.set_color(EIGEN_GREEN).set_stroke(width=6.5),
            Create(line_yx),
            Create(line_ynx),
            FadeIn(lbl_yx),
            FadeIn(lbl_ynx),
            FadeIn(eigen_badge),
            run_time=1.8,
        )
        self.play(
            Indicate(special_vecs[0], color=RESULT_YELLOW, scale_factor=1.12),
            Indicate(special_vecs[1], color=RESULT_YELLOW, scale_factor=1.12),
            run_time=1.5,
        )
        self.wait(5.7)

        # ------------------------------------------------------------------
        # 0:27.5 - 0:35.0 : Guiding Question & Title Reveal
        # ------------------------------------------------------------------
        backdrop = make_card(12.2, 3.6, border_color=RESULT_YELLOW, fill_color=BG_COLOR, fill_opacity=0.94)
        question = txt(
            "\"Why do some vectors change direction while others don't?\"",
            size=32,
            color=RESULT_YELLOW,
            weight="BOLD",
            max_width=11.4,
        )
        question.move_to(backdrop.get_center())

        self.play(
            FadeOut(eigen_badge),
            FadeIn(backdrop),
            Write(question),
            run_time=1.8,
        )
        self.wait(2.2)

        final_title = txt("EIGENVALUES & EIGENVECTORS", size=54, color=TEXT_WHITE, weight="BOLD")
        final_sub = txt(
            "Invariant directions under linear transformations",
            size=24,
            color=EIGEN_GREEN,
        )
        title_group = VGroup(final_title, final_sub).arrange(DOWN, buff=0.25).move_to(backdrop.get_center())
        title_border = SurroundingRectangle(backdrop, color=EIGEN_GREEN, buff=0.0, corner_radius=0.16, stroke_width=2.5)

        self.play(
            FadeOut(question, shift=UP * 0.15),
            Transform(backdrop, title_border.copy().set_fill(BG_COLOR, opacity=0.96)),
            FadeIn(title_group, shift=UP * 0.15),
            run_time=1.4,
        )
        self.wait(1.4)
        fade_out_all(self, run_time=0.7)
