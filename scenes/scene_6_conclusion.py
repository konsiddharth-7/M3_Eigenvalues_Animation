"""Scene 6 (4:35 - 5:00, 25s): Interpretation, Takeaways, and Closing Credits."""

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
    build_plane,
    build_warping_grid,
    configure_scene_background,
    fade_out_all,
    header_bar,
    make_card,
    make_eigen_line,
    make_vector,
    math_tex,
    plane_linear_transform_matrix,
    txt,
)


class Scene6Conclusion(Scene):
    """Scene 6: Summary takeaways, core insight quote, and closing frame (25s)."""

    def construct(self) -> None:
        configure_scene_background()
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 4:35 - 4:49 (14.0s): Transformed Grid + Both Eigenvectors + 3 Takeaways
        # ------------------------------------------------------------------
        header = header_bar(
            "INTERPRETATION & KEY TAKEAWAYS",
            "Seeing the geometry behind the algebra",
            accent=EIGEN_GREEN,
        )
        header.set_z_index(10)

        left_panel = make_card(6.35, 5.75, border_color=CARD_BORDER, fill_opacity=0.98)
        left_panel.move_to([-3.52, -0.55, 0]).set_z_index(5)

        plane, x_label, y_label = build_plane(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            x_length=5.5,
            y_length=5.5,
            include_numbers=True,
            font_size=14,
        )
        plane.move_to([3.38, -0.55, 0]).set_z_index(1)
        x_label.next_to(plane.x_axis.get_end(), DOWN + LEFT * 0.12, buff=0.1).set_z_index(2)
        y_label.next_to(plane.y_axis.get_end(), LEFT + DOWN * 0.08, buff=0.12).set_z_index(2)

        grid = build_warping_grid(plane, grid_radius=3, line_color=ORIGINAL_CYAN, line_opacity=0.28).set_z_index(1)
        origin = plane.c2p(0, 0)
        mat_scene = plane_linear_transform_matrix(plane, MATRIX_A)

        line_yx = make_eigen_line(plane, (1, 1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.6).set_z_index(2)
        line_ynx = make_eigen_line(plane, (1, -1), extent=3.8, color=EIGEN_GREEN, stroke_width=2.6).set_z_index(2)
        v1 = make_vector(plane, (3, 3), color=EIGEN_GREEN, stroke_width=5.2).set_z_index(4)
        v2 = make_vector(plane, (1, -1), color=EIGEN_GREEN, stroke_width=5.2).set_z_index(4)
        v1_tag = math_tex(r"\lambda_1 = 3", color=RESULT_YELLOW, scale=0.75).next_to(plane.c2p(3, 3), LEFT, buff=0.14).set_z_index(4)
        v2_tag = math_tex(r"\lambda_2 = 1", color=RESULT_YELLOW, scale=0.75).next_to(plane.c2p(1, -1), RIGHT, buff=0.14).set_z_index(4)

        self.play(
            FadeIn(header),
            FadeIn(left_panel),
            FadeIn(plane),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(grid),
            run_time=1.0,
        )
        self.play(
            ApplyMatrix(mat_scene, grid, about_point=origin, run_time=1.8, rate_func=smooth),
            Create(line_yx),
            Create(line_ynx),
            Create(v1),
            Create(v2),
            FadeIn(v1_tag),
            FadeIn(v2_tag),
        )

        # Three final takeaways
        t1_box = make_card(5.8, 1.35, border_color=EIGEN_GREEN, fill_opacity=0.92).set_z_index(6)
        t1_txt = txt(
            "1. Eigenvectors preserve their direction\n    under a linear transformation.",
            size=20,
            color=TEXT_WHITE,
            max_width=5.4,
        ).move_to(t1_box.get_center()).set_z_index(7)

        t2_box = make_card(5.8, 1.25, border_color=RESULT_YELLOW, fill_opacity=0.92).set_z_index(6)
        t2_txt = txt(
            "2. Eigenvalues determine the scaling factor.",
            size=20,
            color=TEXT_WHITE,
            max_width=5.4,
        ).move_to(t2_box.get_center()).set_z_index(7)

        t3_box = make_card(5.8, 1.45, border_color=ORIGINAL_CYAN, fill_opacity=0.92).set_z_index(6)
        t3_label = txt("3. Eigenvalues are calculated using:", size=20, color=TEXT_WHITE)
        t3_eq = math_tex(r"\det(A - \lambda I) = 0", color=RESULT_YELLOW, scale=0.88)
        t3_inner = VGroup(t3_label, t3_eq).arrange(DOWN, buff=0.12).move_to(t3_box.get_center()).set_z_index(7)

        takeaways = VGroup(
            VGroup(t1_box, t1_txt),
            VGroup(t2_box, t2_txt),
            VGroup(t3_box, t3_inner),
        ).arrange(DOWN, buff=0.32).move_to([-3.52, -0.55, 0])

        for item in takeaways:
            self.play(FadeIn(item, shift=RIGHT * 0.12), run_time=1.4)
        self.play(
            Indicate(v1, color=RESULT_YELLOW),
            Indicate(v2, color=RESULT_YELLOW),
            run_time=1.2,
        )
        self.wait(5.8)

        # ------------------------------------------------------------------
        # 4:49 - 5:00 (11.0s): Core Quote + Final THANK YOU & Credits Frame
        # ------------------------------------------------------------------
        quote_card = make_card(11.8, 2.2, border_color=RESULT_YELLOW, fill_opacity=0.97)
        quote_txt = txt(
            "\"Eigenvalues reveal how a transformation acts\nalong its special directions.\"",
            size=32,
            color=RESULT_YELLOW,
            weight="BOLD",
            max_width=11.0,
        ).move_to(quote_card.get_center())
        quote_group = VGroup(quote_card, quote_txt)

        self.play(
            FadeOut(header),
            FadeOut(left_panel),
            FadeOut(takeaways),
            FadeOut(plane),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(grid),
            FadeOut(line_yx),
            FadeOut(line_ynx),
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v1_tag),
            FadeOut(v2_tag),
            FadeIn(quote_group, shift=UP * 0.12),
            run_time=1.2,
        )
        self.wait(2.5)

        # Final Closing Frame (THANK YOU + Topic, Student ID, AI Disclosure, References)
        credits_card = make_card(12.0, 6.4, border_color=EIGEN_GREEN, fill_opacity=0.97)
        ty_title = txt("THANK YOU", size=48, color=TEXT_WHITE, weight="BOLD")
        topic_line = txt(
            "Topic: Eigenvalues and Eigenvectors — Invariant Directions Under Linear Transformations",
            size=20,
            color=EIGEN_GREEN,
            weight="BOLD",
            max_width=11.2,
        )
        student_line = txt(
            "Course: Linear Algebra & Calculus (M3)   |   Student: SIDDHARTH KONDERU   |   ID: E25B070643",
            size=18,
            color=RESULT_YELLOW,
            max_width=11.2,
        )
        ai_line = txt(
            "AI Tools Disclosure: AI tools assisted with Python/Manim scripting, MathJax SVG rendering, and\n"
            "narration drafting. All mathematical derivations and eigenpair verifications were checked independently.",
            size=16,
            color=TEXT_MUTED,
            max_width=11.0,
        )
        ref_line = txt(
            "References:  1) G. Strang, Introduction to Linear Algebra (5th ed.)   •   "
            "2) 3Blue1Brown, Essence of Linear Algebra (Ch. 14)   •   3) M3 Lecture Notes",
            size=16,
            color=TEXT_MUTED,
            max_width=11.2,
        )

        credits_body = VGroup(ty_title, topic_line, student_line, ai_line, ref_line).arrange(DOWN, buff=0.35)
        credits_body.move_to(credits_card.get_center())
        credits_all = VGroup(credits_card, credits_body)

        self.play(
            FadeOut(quote_group, shift=UP * 0.1),
            FadeIn(credits_all, shift=UP * 0.1),
            run_time=1.3,
        )
        self.wait(5.3)
        fade_out_all(self, run_time=0.7)
