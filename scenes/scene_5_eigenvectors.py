"""Scene 5 (3:15 - 4:35, 80s): Finding the Eigenvectors & Visual Verification."""

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


class Scene5Eigenvectors(Scene):
    """Scene 5: Solving for v1, v2 and visually verifying Av = lambda v (80s)."""

    def construct(self) -> None:
        configure_scene_background()
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 3:15 - 3:43 (28.0s): PART A — Eigenvector for lambda_1 = 3
        # ------------------------------------------------------------------
        header = header_bar(
            "FINDING THE EIGENVECTORS",
            "Part A: Solving (A − 3I)v = 0 for λ₁ = 3",
            accent=EIGEN_GREEN,
        )
        header.set_z_index(10)

        left_card = make_card(7.35, 5.75, border_color=CARD_BORDER, fill_opacity=0.96).move_to([-2.95, -0.55, 0])
        right_card = make_card(4.55, 5.75, border_color=EIGEN_GREEN, fill_opacity=0.94).move_to([3.45, -0.55, 0])

        a1 = math_tex(r"(A - \color{#FACC15}{3}I)\color{#4ADE80}{\mathbf{v}} = \mathbf{0}", color=None, scale=1.05)
        a2 = math_tex(
            r"\begin{bmatrix} 2 - 3 & 1 \\ 1 & 2 - 3 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            color=TEXT_WHITE,
            scale=0.92,
        )
        a3 = math_tex(
            r"\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            color=TEXT_WHITE,
            scale=0.92,
        )
        a4 = math_tex(r"-x + y = 0 \quad\Longrightarrow\quad x = y", color=ORIGINAL_CYAN, scale=1.0)
        a5 = math_tex(
            r"\color{#4ADE80}{\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}}",
            color=None,
            scale=1.1,
        )
        a5_box = highlight_box(a5, color=EIGEN_GREEN, buff=0.14)
        a5_group = VGroup(a5, a5_box)

        col_a = VGroup(a1, a2, a3, a4, a5_group).arrange(DOWN, buff=0.25).move_to(left_card.get_center())

        # Right card: Any non-zero scalar multiple is also an eigenvector
        r_title = txt("Any non-zero scalar multiple\nis also an eigenvector!", size=20, color=EIGEN_GREEN, weight="BOLD")
        mini_plane, m_xl, m_yl = build_plane(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            x_length=3.3,
            y_length=3.3,
            include_numbers=False,
        )
        mini_plane.move_to([3.45, -0.45, 0])
        m_line = make_eigen_line(mini_plane, (1, 1), extent=2.6, color=EIGEN_GREEN, stroke_width=2.0)
        mv_1 = make_vector(mini_plane, (1, 1), color=EIGEN_GREEN, stroke_width=4.5)
        mv_2 = make_vector(mini_plane, (2, 2), color=ORIGINAL_CYAN, stroke_width=3.5)
        mv_neg = make_vector(mini_plane, (-1, -1), color=RESULT_YELLOW, stroke_width=3.5)

        r_formula = math_tex(
            r"c\begin{bmatrix} 1 \\ 1 \end{bmatrix}, \; c \neq 0",
            color=TEXT_WHITE,
            scale=0.88,
        )
        r_title.move_to([3.45, 1.75, 0])
        r_formula.move_to([3.45, -2.75, 0])

        self.play(FadeIn(header), FadeIn(left_card), FadeIn(right_card), run_time=1.0)
        self.play(FadeIn(a1, shift=UP * 0.1), run_time=1.6)
        self.wait(1.0)
        self.play(FadeIn(a2, shift=UP * 0.1), run_time=2.5)
        self.wait(1.2)
        self.play(FadeIn(a3, shift=UP * 0.1), run_time=2.5)
        self.wait(1.5)
        self.play(FadeIn(a4, shift=UP * 0.1), run_time=2.6)
        self.wait(1.8)
        self.play(FadeIn(a5, shift=UP * 0.1), Create(a5_box), run_time=2.4)
        self.play(Indicate(a5_group, color=EIGEN_GREEN), run_time=1.2)

        # Show scalar multiples visual
        self.play(
            FadeIn(r_title),
            FadeIn(mini_plane),
            Create(m_line),
            Create(mv_1),
            FadeIn(r_formula),
            run_time=2.2,
        )
        self.play(Create(mv_2), Create(mv_neg), run_time=1.8)
        self.wait(4.7)

        # ------------------------------------------------------------------
        # 3:43 - 4:07 (24.0s): PART B — Eigenvector for lambda_2 = 1
        # ------------------------------------------------------------------
        header_b = header_bar(
            "FINDING THE EIGENVECTORS",
            "Part B: Solving (A − I)v = 0 for λ₂ = 1",
            accent=EIGEN_GREEN,
        )
        full_card = make_card(11.6, 5.75, border_color=CARD_BORDER, fill_opacity=0.96).move_to([0, -0.55, 0])

        b1 = math_tex(r"(A - \color{#FACC15}{1}I)\color{#4ADE80}{\mathbf{v}} = \mathbf{0}", color=None, scale=1.08)
        b2 = math_tex(
            r"\begin{bmatrix} 2 - 1 & 1 \\ 1 & 2 - 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            color=TEXT_WHITE,
            scale=0.96,
        )
        b3 = math_tex(
            r"\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            color=TEXT_WHITE,
            scale=0.96,
        )
        b4 = math_tex(r"x + y = 0 \quad\Longrightarrow\quad x = -y", color=ORIGINAL_CYAN, scale=1.05)
        b5 = math_tex(
            r"\color{#4ADE80}{\mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}} \quad (\text{and any } c\mathbf{v}_2,\; c \neq 0)",
            color=None,
            scale=1.05,
        )
        b5_box = highlight_box(b5, color=EIGEN_GREEN, buff=0.14)
        b5_group = VGroup(b5, b5_box)

        col_b = VGroup(b1, b2, b3, b4, b5_group).arrange(DOWN, buff=0.26).move_to(full_card.get_center())

        part_a_objs = [
            left_card, right_card, col_a, r_title, mini_plane, m_line, mv_1, mv_2, mv_neg, r_formula
        ]
        self.play(
            *[FadeOut(m) for m in part_a_objs],
            Transform(header, header_b),
            FadeIn(full_card),
            run_time=1.4,
        )
        self.play(FadeIn(b1, shift=UP * 0.1), run_time=1.8)
        self.wait(1.0)
        self.play(FadeIn(b2, shift=UP * 0.1), run_time=2.6)
        self.wait(1.2)
        self.play(FadeIn(b3, shift=UP * 0.1), run_time=2.6)
        self.wait(1.5)
        self.play(FadeIn(b4, shift=UP * 0.1), run_time=2.8)
        self.wait(1.8)
        self.play(FadeIn(b5, shift=UP * 0.1), Create(b5_box), run_time=2.5)
        self.play(Indicate(b5_group, color=EIGEN_GREEN), run_time=1.2)
        self.wait(3.6)

        # ------------------------------------------------------------------
        # 4:07 - 4:35 (28.0s): PART C — Visual & Algebraic Verification
        # ------------------------------------------------------------------
        header_c = header_bar(
            "VISUAL VERIFICATION",
            "Part C: Confirming both eigenpairs geometrically under A",
            accent=RESULT_YELLOW,
        )

        left_verify = make_card(6.15, 5.75, border_color=CARD_BORDER, fill_opacity=0.98)
        left_verify.move_to([-3.62, -0.55, 0]).set_z_index(5)

        plane, x_label, y_label = build_plane(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            x_length=5.6,
            y_length=5.6,
            include_numbers=True,
            font_size=14,
        )
        plane.move_to([3.32, -0.55, 0]).set_z_index(1)
        x_label.next_to(plane.x_axis.get_end(), DOWN + LEFT * 0.12, buff=0.1).set_z_index(2)
        y_label.next_to(plane.y_axis.get_end(), LEFT + DOWN * 0.08, buff=0.12).set_z_index(2)

        grid = build_warping_grid(plane, grid_radius=3, line_color=ORIGINAL_CYAN, line_opacity=0.24).set_z_index(1)
        grid_initial = grid.copy()
        origin = plane.c2p(0, 0)

        line_yx = make_eigen_line(plane, (1, 1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.4).set_z_index(2)
        line_ynx = make_eigen_line(plane, (1, -1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.4).set_z_index(2)

        self.play(
            FadeOut(full_card),
            FadeOut(col_b),
            Transform(header, header_c),
            FadeIn(left_verify),
            FadeIn(plane),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(grid),
            Create(line_yx),
            Create(line_ynx),
            run_time=1.6,
        )

        # Verify v1 = [1, 1]^T -> [3, 3]^T = 3[1, 1]^T
        v1_title = txt("Check 1:  λ₁ = 3,   v₁ = [1, 1]ᵀ", size=20, color=EIGEN_GREEN, weight="BOLD")
        v1_eq = math_tex(
            r"A\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix} = \color{#FACC15}{3}\color{#4ADE80}{\begin{bmatrix} 1 \\ 1 \end{bmatrix}}",
            color=None,
            scale=0.80,
            max_width=5.6,
        )
        v1_desc = txt("Stretches 3× along y = x (direction preserved)", size=18, color=TEXT_WHITE)
        v1_block = VGroup(v1_title, v1_eq, v1_desc).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        v1_block.move_to([-3.62, 1.4, 0]).set_z_index(6)

        vec1 = make_vector(plane, (1, 1), color=ORIGINAL_CYAN, stroke_width=5.0).set_z_index(4)
        vec1_ghost = make_vector(plane, (1, 1), color=ORIGINAL_CYAN, stroke_width=3.0).set_opacity(0.45).set_z_index(3)
        vec1_target = make_vector(plane, (3, 3), color=EIGEN_GREEN, stroke_width=5.5).set_z_index(4)
        vec1_lbl = math_tex(r"3\mathbf{v}_1 = [3,3]^T", color=EIGEN_GREEN, scale=0.7).next_to(
            plane.c2p(3, 3), LEFT, buff=0.15
        ).set_z_index(4)

        mat_scene = plane_linear_transform_matrix(plane, MATRIX_A)

        self.play(FadeIn(v1_title), FadeIn(v1_eq), Create(vec1), run_time=1.8)
        self.add(vec1_ghost)
        self.play(
            ApplyMatrix(mat_scene, grid, about_point=origin, run_time=2.6, rate_func=smooth),
            Transform(vec1, vec1_target, run_time=2.6, rate_func=smooth),
        )
        self.play(FadeIn(vec1_lbl), FadeIn(v1_desc), run_time=1.2)
        self.wait(1.8)

        # Verify v2 = [1, -1]^T -> [1, -1]^T = 1[1, -1]^T
        v2_title = txt("Check 2:  λ₂ = 1,   v₂ = [1, −1]ᵀ", size=20, color=EIGEN_GREEN, weight="BOLD")
        v2_eq = math_tex(
            r"A\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \color{#FACC15}{1}\color{#4ADE80}{\begin{bmatrix} 1 \\ -1 \end{bmatrix}}",
            color=None,
            scale=0.80,
            max_width=5.6,
        )
        v2_desc = txt("Unchanged 1× along y = −x (direction preserved)", size=18, color=TEXT_WHITE)
        v2_block = VGroup(v2_title, v2_eq, v2_desc).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        v2_block.move_to([-3.62, -0.45, 0]).set_z_index(6)

        vec2 = make_vector(plane, (1, -1), color=EIGEN_GREEN, stroke_width=5.5).set_z_index(4)
        vec2_lbl = math_tex(r"1\mathbf{v}_2 = [1,-1]^T", color=EIGEN_GREEN, scale=0.7).next_to(
            plane.c2p(1, -1), RIGHT, buff=0.14
        ).set_z_index(4)

        self.play(
            Transform(grid, grid_initial),
            FadeIn(v2_title),
            FadeIn(v2_eq),
            Create(vec2),
            run_time=1.6,
        )
        self.play(
            ApplyMatrix(mat_scene, grid, about_point=origin, run_time=2.5, rate_func=smooth),
            Indicate(vec2, color=RESULT_YELLOW, scale_factor=1.18, run_time=2.5),
        )
        self.play(FadeIn(vec2_lbl), FadeIn(v2_desc), run_time=1.2)
        self.wait(1.8)

        # Final Eigenpair Summary Cards
        sum_card = make_card(5.65, 1.45, border_color=RESULT_YELLOW, fill_opacity=0.95).set_z_index(6)
        sum_row1 = math_tex(
            r"\color{#FACC15}{\text{Eigenvalue } 3} \;\longrightarrow\; \color{#4ADE80}{\text{Eigenvector } \begin{bmatrix} 1 \\ 1 \end{bmatrix}}",
            color=None,
            scale=0.78,
        )
        sum_row2 = math_tex(
            r"\color{#FACC15}{\text{Eigenvalue } 1} \;\longrightarrow\; \color{#4ADE80}{\text{Eigenvector } \begin{bmatrix} 1 \\ -1 \end{bmatrix}}",
            color=None,
            scale=0.78,
        )
        sum_text = VGroup(sum_row1, sum_row2).arrange(DOWN, buff=0.16).move_to(sum_card.get_center()).set_z_index(7)
        sum_group = VGroup(sum_card, sum_text).move_to([-3.62, -2.45, 0])

        self.play(FadeIn(sum_group, shift=UP * 0.1), run_time=1.8)
        self.play(Indicate(sum_card, color=RESULT_YELLOW), run_time=1.2)
        self.wait(8.2)
        fade_out_all(self, run_time=0.7)
