"""Scene 3 (1:15 - 2:00, 45s): Eigenvalues and Eigenvectors — Central Concept."""

from __future__ import annotations

from manim import (
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


class Scene3EigenConcept(Scene):
    """Scene 3: Introduce Av = lambda v and demonstrate invariant directions (45s)."""

    def construct(self) -> None:
        configure_scene_background()
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 1:15 - 1:30 (15.0s): Fundamental Equation Av = lambda v + Legend
        # ------------------------------------------------------------------
        header = header_bar(
            "EIGENVALUES & EIGENVECTORS",
            "The fundamental equation: Av = λv",
            accent=EIGEN_GREEN,
        )
        header.set_z_index(10)

        eq_card = make_card(6.4, 1.75, border_color=RESULT_YELLOW, fill_opacity=0.96)
        eq_card.move_to([0, 1.35, 0])
        main_eq = math_tex(
            r"\color{#F8FAFC}{A}\color{#4ADE80}{\mathbf{v}} \;=\; \color{#FACC15}{\lambda}\color{#4ADE80}{\mathbf{v}}",
            color=None,
            scale=1.9,
        ).move_to(eq_card.get_center())

        self.play(FadeIn(header), FadeIn(eq_card), FadeIn(main_eq, shift=UP * 0.12), run_time=1.8)

        # 5 visual symbol legend rows cleanly arranged below eq_card
        legend_specs = [
            (r"\color{#F8FAFC}{A}", "transformation matrix", TEXT_WHITE),
            (r"\color{#4ADE80}{\mathbf{v}}", "non-zero eigenvector  (v ≠ 0)", EIGEN_GREEN),
            (r"\color{#FACC15}{\lambda}", "corresponding eigenvalue (scalar)", RESULT_YELLOW),
            (r"\color{#FB923C}{A\mathbf{v}}", "transformed vector", TRANSFORMED_ORANGE),
            (r"\color{#FACC15}{\lambda}\color{#4ADE80}{\mathbf{v}}", "scaled version of original vector", RESULT_YELLOW),
        ]
        legend_rows = VGroup()
        for sym_tex, desc, accent in legend_specs:
            pill = make_card(8.8, 0.56, border_color=CARD_BORDER, fill_opacity=0.90, corner_radius=0.1)
            sym = math_tex(sym_tex, color=None, scale=0.82)
            eq_sign = txt("=", size=22, color=TEXT_MUTED)
            label = txt(desc, size=22, color=accent, weight="BOLD")
            sym.move_to(pill.get_left() + RIGHT * 0.85)
            eq_sign.move_to(pill.get_left() + RIGHT * 1.55)
            label.next_to(eq_sign, RIGHT, buff=0.28)
            legend_rows.add(VGroup(pill, sym, eq_sign, label))

        legend_rows.arrange(DOWN, buff=0.14).move_to([0, -1.45, 0])

        for row in legend_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.9)
        self.wait(4.7)

        # Compact equation to top-left panel and bring in right-side coordinate plane
        left_panel = make_card(6.0, 5.75, border_color=CARD_BORDER, fill_opacity=0.98)
        left_panel.move_to([-3.7, -0.55, 0]).set_z_index(5)

        compact_eq = math_tex(
            r"\color{#F8FAFC}{A}\color{#4ADE80}{\mathbf{v}} = \color{#FACC15}{\lambda}\color{#4ADE80}{\mathbf{v}}",
            color=None,
            scale=1.25,
        ).move_to([-3.7, 1.55, 0]).set_z_index(6)
        compact_box = highlight_box(compact_eq, color=CARD_BORDER, buff=0.14).set_z_index(6)

        plane, x_label, y_label = build_plane(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            x_length=5.6,
            y_length=5.6,
            include_numbers=True,
            font_size=14,
        )
        plane.move_to([3.3, -0.55, 0]).set_z_index(1)
        x_label.next_to(plane.x_axis.get_end(), DOWN + LEFT * 0.12, buff=0.1).set_z_index(2)
        y_label.next_to(plane.y_axis.get_end(), LEFT + DOWN * 0.08, buff=0.12).set_z_index(2)

        grid = build_warping_grid(plane, grid_radius=3, line_color=ORIGINAL_CYAN, line_opacity=0.26).set_z_index(1)
        origin = plane.c2p(0, 0)

        self.play(
            FadeOut(legend_rows),
            FadeOut(eq_card),
            Transform(main_eq, compact_eq),
            FadeIn(left_panel),
            FadeIn(compact_box),
            FadeIn(plane),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(grid),
            run_time=1.8,
        )
        # Wait remainder of 15.0s -> 1.8 + 5*0.9 + 4.7 + 1.8 = 12.8 -> +2.2s? Wait: let's keep exact timing!
        self.wait(2.2)

        # ------------------------------------------------------------------
        # 1:30 - 1:43 (13.0s): Vector along y = x, Stretches 3x, lambda = 3
        # ------------------------------------------------------------------
        line_yx = make_eigen_line(plane, (1, 1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.4).set_z_index(2)
        lbl_yx = math_tex(r"y = x", color=EIGEN_GREEN, scale=0.72).move_to(plane.c2p(3.2, 2.5)).set_z_index(3)

        v1_init = make_vector(plane, (1, 1), color=EIGEN_GREEN, stroke_width=5.2).set_z_index(4)
        v1_ghost = make_vector(plane, (1, 1), color=ORIGINAL_CYAN, stroke_width=3.2).set_opacity(0.45).set_z_index(3)
        v1_scaled = make_vector(plane, (3, 3), color=EIGEN_GREEN, stroke_width=5.5).set_z_index(4)

        case1_title = txt("Case 1: Vector along y = x", size=22, color=EIGEN_GREEN, weight="BOLD")
        case1_eq = math_tex(
            r"A\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix} = \color{#FACC15}{3}\color{#4ADE80}{\begin{bmatrix} 1 \\ 1 \end{bmatrix}}",
            color=None,
            scale=0.86,
        )
        case1_note = txt("Same direction  •  3× longer", size=20, color=TEXT_WHITE)
        lam1_badge = math_tex(r"\lambda_1 = 3", color=RESULT_YELLOW, scale=1.25)
        lam1_box = highlight_box(lam1_badge, color=RESULT_YELLOW, buff=0.14)
        lam1_group = VGroup(lam1_badge, lam1_box)

        case1_panel = VGroup(case1_title, case1_eq, case1_note, lam1_group).arrange(DOWN, buff=0.25)
        case1_panel.move_to([-3.7, -1.15, 0]).set_z_index(6)

        self.play(Create(line_yx), FadeIn(lbl_yx), Create(v1_init), FadeIn(case1_title), run_time=1.8)
        self.add(v1_ghost)
        self.wait(0.8)

        mat_scene = plane_linear_transform_matrix(plane, MATRIX_A)
        grid_copy_1 = grid.copy()
        self.play(
            ApplyMatrix(mat_scene, grid, about_point=origin, run_time=2.8, rate_func=smooth),
            Transform(v1_init, v1_scaled, run_time=2.8, rate_func=smooth),
        )
        self.play(FadeIn(case1_eq), FadeIn(case1_note), run_time=1.5)
        self.play(FadeIn(lam1_group), Indicate(lam1_group, color=RESULT_YELLOW), run_time=1.5)
        self.wait(4.6)

        # ------------------------------------------------------------------
        # 1:43 - 1:54 (11.0s): Vector along y = -x, Unchanged, lambda = 1
        # ------------------------------------------------------------------
        # Restore warping grid smoothly for the second test
        self.play(
            FadeOut(case1_panel),
            FadeOut(v1_ghost),
            v1_init.animate.set_opacity(0.35),
            Transform(grid, grid_copy_1),
            run_time=1.0,
        )

        line_ynx = make_eigen_line(plane, (1, -1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.4).set_z_index(2)
        lbl_ynx = math_tex(r"y = -x", color=EIGEN_GREEN, scale=0.72).move_to(plane.c2p(2.9, -3.1)).set_z_index(3)

        v2_init = make_vector(plane, (1, -1), color=EIGEN_GREEN, stroke_width=5.5).set_z_index(4)
        v2_target = make_vector(plane, (1, -1), color=EIGEN_GREEN, stroke_width=5.5).set_z_index(4)

        case2_title = txt("Case 2: Vector along y = -x", size=22, color=EIGEN_GREEN, weight="BOLD")
        case2_eq = math_tex(
            r"A\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \color{#FACC15}{1}\color{#4ADE80}{\begin{bmatrix} 1 \\ -1 \end{bmatrix}}",
            color=None,
            scale=0.86,
        )
        case2_note = txt("Same direction  •  Same length (1×)", size=20, color=TEXT_WHITE)
        lam2_badge = math_tex(r"\lambda_2 = 1", color=RESULT_YELLOW, scale=1.25)
        lam2_box = highlight_box(lam2_badge, color=RESULT_YELLOW, buff=0.14)
        lam2_group = VGroup(lam2_badge, lam2_box)

        case2_panel = VGroup(case2_title, case2_eq, case2_note, lam2_group).arrange(DOWN, buff=0.25)
        case2_panel.move_to([-3.7, -1.15, 0]).set_z_index(6)

        self.play(Create(line_ynx), FadeIn(lbl_ynx), Create(v2_init), FadeIn(case2_title), run_time=1.6)
        self.play(
            ApplyMatrix(mat_scene, grid, about_point=origin, run_time=2.5, rate_func=smooth),
            Indicate(v2_init, color=RESULT_YELLOW, scale_factor=1.18, run_time=2.5),
        )
        self.play(FadeIn(case2_eq), FadeIn(case2_note), run_time=1.3)
        self.play(FadeIn(lam2_group), Indicate(lam2_group, color=RESULT_YELLOW), run_time=1.3)
        self.wait(3.3)

        # ------------------------------------------------------------------
        # 1:54 - 2:00 (6.0s): Highlight Both Invariant Directions & Distinction
        # ------------------------------------------------------------------
        distinction_1 = VGroup(
            txt("Eigenvector (v)", size=22, color=EIGEN_GREEN, weight="BOLD"),
            txt("The special invariant direction", size=19, color=TEXT_WHITE),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        distinction_2 = VGroup(
            txt("Eigenvalue (λ)", size=22, color=RESULT_YELLOW, weight="BOLD"),
            txt("The scaling factor along v", size=19, color=TEXT_WHITE),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        distinction_group = VGroup(distinction_1, distinction_2).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        distinction_group.move_to([-3.7, -1.25, 0]).set_z_index(6)

        self.play(
            FadeOut(case2_panel),
            v1_init.animate.set_opacity(1.0),
            Indicate(line_yx, color=EIGEN_GREEN, scale_factor=1.03),
            Indicate(line_ynx, color=EIGEN_GREEN, scale_factor=1.03),
            FadeIn(distinction_group, shift=UP * 0.1),
            run_time=1.8,
        )
        self.wait(3.5)
        fade_out_all(self, run_time=0.7)
