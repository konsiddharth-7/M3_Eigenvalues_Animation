"""Scene 4 (2:00 - 3:15, 75s): Mathematical Derivation of Characteristic Equation & Eigenvalues."""

from __future__ import annotations

from manim import (
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
)

from scenes.common import (
    ACCENT_RED,
    BG_COLOR,
    CARD_BORDER,
    EIGEN_GREEN,
    ORIGINAL_CYAN,
    RESULT_YELLOW,
    TEXT_MUTED,
    TEXT_WHITE,
    TRANSFORMED_ORANGE,
    configure_scene_background,
    fade_out_all,
    header_bar,
    highlight_box,
    make_card,
    math_tex,
    txt,
)


class Scene4Derivation(Scene):
    """Scene 4: Step-by-step derivation of det(A - lambda I) = 0 and eigenvalues (75s)."""

    def construct(self) -> None:
        configure_scene_background()
        self.camera.background_color = BG_COLOR

        header = header_bar(
            "MATHEMATICAL DERIVATION",
            "Deriving the characteristic equation & finding eigenvalues",
            accent=RESULT_YELLOW,
        )

        # ------------------------------------------------------------------
        # 2:00 - 2:18 (18.0s): Av = lambda v  -->  det(A - lambda I) = 0
        # ------------------------------------------------------------------
        card1 = make_card(11.6, 5.75, border_color=CARD_BORDER, fill_opacity=0.96).move_to([0, -0.55, 0])

        line1 = math_tex(
            r"\color{#F8FAFC}{A}\color{#4ADE80}{\mathbf{v}} = \color{#FACC15}{\lambda}\color{#4ADE80}{\mathbf{v}}",
            color=None,
            scale=1.25,
        )
        line2 = math_tex(
            r"\color{#F8FAFC}{A}\color{#4ADE80}{\mathbf{v}} - \color{#FACC15}{\lambda}\color{#4ADE80}{\mathbf{v}} = \mathbf{0}",
            color=None,
            scale=1.2,
        )
        note_id = txt("Insert identity matrix I so both terms act as matrices:", size=20, color=ORIGINAL_CYAN)
        line3 = math_tex(
            r"\color{#F8FAFC}{A}\color{#4ADE80}{\mathbf{v}} - \color{#FACC15}{\lambda} I \color{#4ADE80}{\mathbf{v}} = \mathbf{0}",
            color=None,
            scale=1.2,
        )
        line4 = math_tex(
            r"(A - \color{#FACC15}{\lambda} I)\color{#4ADE80}{\mathbf{v}} = \mathbf{0}",
            color=None,
            scale=1.25,
        )

        rearrange_col = VGroup(line1, line2, note_id, line3, line4).arrange(DOWN, buff=0.28)
        rearrange_col.move_to([-2.4, -0.5, 0])

        sing_card = make_card(4.8, 3.8, border_color=ACCENT_RED, fill_opacity=0.92).move_to([3.0, -0.55, 0])
        sing_title = txt("Non-zero v ≠ 0 exists only if:", size=20, color=TEXT_WHITE, weight="BOLD", max_width=4.3)
        sing_sub = txt("(A − λI) is singular\n(non-invertible)", size=20, color=ACCENT_RED)
        det_eq = math_tex(r"\det(A - \lambda I) = 0", color=RESULT_YELLOW, scale=1.15)
        det_box = highlight_box(det_eq, color=RESULT_YELLOW, buff=0.14)
        det_group = VGroup(det_eq, det_box)
        sing_col = VGroup(sing_title, sing_sub, det_group).arrange(DOWN, buff=0.35).move_to(sing_card.get_center())

        self.play(FadeIn(header), FadeIn(card1), run_time=1.0)
        self.play(FadeIn(line1, shift=UP * 0.1), run_time=1.4)
        self.wait(0.8)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=1.4)
        self.wait(0.8)
        self.play(FadeIn(note_id), FadeIn(line3, shift=UP * 0.1), run_time=1.8)
        self.wait(0.8)
        self.play(FadeIn(line4, shift=UP * 0.1), run_time=1.6)
        self.wait(1.2)
        self.play(FadeIn(sing_card), FadeIn(sing_title), FadeIn(sing_sub), run_time=1.8)
        self.play(FadeIn(det_eq), Create(det_box), run_time=1.6)
        self.play(Indicate(det_group, color=RESULT_YELLOW), run_time=1.2)
        self.wait(2.6)

        # ------------------------------------------------------------------
        # 2:18 - 2:38 (20.0s): Step 1 (Subtract lambda I) & Step 2 (Determinant)
        # ------------------------------------------------------------------
        top_strip = make_card(11.6, 1.35, border_color=RESULT_YELLOW, fill_opacity=0.95).move_to([0, 1.65, 0])
        ref_A = math_tex(r"A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}", color=TEXT_WHITE, scale=0.95)
        ref_I = math_tex(r"I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}", color=ORIGINAL_CYAN, scale=0.95)
        ref_det = math_tex(r"\det(A - \lambda I) = 0", color=RESULT_YELLOW, scale=1.05)
        ref_row = VGroup(ref_A, ref_I, ref_det).arrange(RIGHT, buff=0.85).move_to(top_strip.get_center())

        work_card = make_card(11.6, 4.15, border_color=CARD_BORDER, fill_opacity=0.96).move_to([0, -1.35, 0])

        self.play(
            FadeOut(rearrange_col),
            FadeOut(sing_card),
            FadeOut(sing_title),
            FadeOut(sing_sub),
            FadeOut(det_group),
            FadeOut(card1),
            FadeIn(top_strip),
            FadeIn(ref_row),
            FadeIn(work_card),
            run_time=1.5,
        )

        # Step 1: Subtract lambda I
        s1_lbl = txt("Step 1: Subtract λI from A", size=22, color=ORIGINAL_CYAN, weight="BOLD")
        s1_eq1 = math_tex(
            r"A - \lambda I = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}",
            color=TEXT_WHITE,
            scale=0.98,
        )
        s1_eq2 = math_tex(
            r"= \begin{bmatrix} 2 - \color{#FACC15}{\lambda} & 1 \\ 1 & 2 - \color{#FACC15}{\lambda} \end{bmatrix}",
            color=None,
            scale=1.02,
        )
        s1_row = VGroup(s1_eq1, s1_eq2).arrange(RIGHT, buff=0.35)
        s1_block = VGroup(s1_lbl, s1_row).arrange(DOWN, buff=0.22).move_to([0, -0.35, 0])

        self.play(FadeIn(s1_lbl), FadeIn(s1_eq1, shift=UP * 0.1), run_time=2.0)
        self.wait(1.0)
        self.play(FadeIn(s1_eq2, shift=RIGHT * 0.15), run_time=2.0)
        self.wait(1.5)

        # Step 2: Calculate the determinant (main diagonal in yellow, anti-diagonal in orange)
        s2_lbl = txt("Step 2: Calculate the determinant   ad − bc = 0", size=22, color=RESULT_YELLOW, weight="BOLD")
        s2_mat = math_tex(
            r"\begin{vmatrix} \color{#FACC15}{2 - \lambda} & \color{#FB923C}{1} \\ \color{#FB923C}{1} & \color{#FACC15}{2 - \lambda} \end{vmatrix} = 0",
            color=None,
            scale=1.05,
        )
        s2_arrow = math_tex(r"\Longrightarrow", color=TEXT_MUTED, scale=0.9)
        s2_prod = math_tex(
            r"\color{#FACC15}{(2 - \lambda)(2 - \lambda)} - \color{#FB923C}{(1 \times 1)} = 0",
            color=None,
            scale=1.05,
        )
        s2_row = VGroup(s2_mat, s2_arrow, s2_prod).arrange(RIGHT, buff=0.35)
        s2_block = VGroup(s2_lbl, s2_row).arrange(DOWN, buff=0.22).move_to([0, -2.35, 0])

        self.play(FadeIn(s2_lbl), FadeIn(s2_mat, shift=UP * 0.1), run_time=2.5)
        self.wait(1.2)
        self.play(FadeIn(s2_arrow), FadeIn(s2_prod, shift=RIGHT * 0.15), run_time=2.8)
        self.play(Indicate(s2_prod, color=RESULT_YELLOW), run_time=1.2)
        self.wait(4.3)

        # ------------------------------------------------------------------
        # 2:38 - 2:58 (20.0s): Step 3 — Expand Completely (Zero Skipped Steps)
        # ------------------------------------------------------------------
        s3_lbl = txt("Step 3: Expand and simplify", size=23, color=ORIGINAL_CYAN, weight="BOLD")
        s3_line0 = math_tex(
            r"(2 - \lambda)(2 - \lambda) - (1 \times 1) = 0",
            color=TEXT_MUTED,
            scale=0.95,
        )
        s3_line1 = math_tex(
            r"(2 - \lambda)^2 - 1 = 0",
            color=TEXT_WHITE,
            scale=1.08,
        )
        s3_line2 = math_tex(
            r"(4 - 4\lambda + \lambda^2) - 1 = 0",
            color=TEXT_WHITE,
            scale=1.08,
        )
        s3_line3 = math_tex(
            r"\lambda^2 - 4\lambda + 3 = 0",
            color=RESULT_YELLOW,
            scale=1.25,
        )
        s3_box = highlight_box(s3_line3, color=RESULT_YELLOW, buff=0.14)
        s3_col = VGroup(s3_lbl, s3_line0, s3_line1, s3_line2, s3_line3).arrange(DOWN, buff=0.24)
        s3_col.move_to([0, -1.35, 0])
        s3_box.move_to(s3_line3.get_center())

        self.play(
            FadeOut(s1_block),
            FadeOut(s2_block),
            FadeIn(s3_lbl),
            FadeIn(s3_line0),
            run_time=1.4,
        )
        self.wait(1.4)
        self.play(FadeIn(s3_line1, shift=UP * 0.1), run_time=2.2)
        self.wait(1.8)
        self.play(FadeIn(s3_line2, shift=UP * 0.1), run_time=2.6)
        self.wait(2.2)
        self.play(FadeIn(s3_line3, shift=UP * 0.1), Create(s3_box), run_time=2.6)
        self.wait(5.8)

        # ------------------------------------------------------------------
        # 2:58 - 3:15 (17.0s): Step 4 (Factorize) & Step 5 (Final Eigenvalues)
        # ------------------------------------------------------------------
        s4_lbl = txt("Step 4: Factorize the quadratic equation", size=23, color=ORIGINAL_CYAN, weight="BOLD")
        s4_quad = math_tex(r"\lambda^2 - 4\lambda + 3 = 0", color=TEXT_WHITE, scale=1.15)
        s4_hint = txt("Find two numbers with sum = −4 and product = +3   →   −3 and −1", size=20, color=TEXT_MUTED)
        s4_fact = math_tex(r"(\lambda - 3)(\lambda - 1) = 0", color=TEXT_WHITE, scale=1.25)

        s5_lbl = txt("Step 5: Final Eigenvalues", size=23, color=RESULT_YELLOW, weight="BOLD")
        lam1 = math_tex(r"\lambda_1 = 3", color=RESULT_YELLOW, scale=1.45)
        lam2 = math_tex(r"\lambda_2 = 1", color=RESULT_YELLOW, scale=1.45)
        lam1_box = highlight_box(lam1, color=RESULT_YELLOW, buff=0.18)
        lam2_box = highlight_box(lam2, color=RESULT_YELLOW, buff=0.18)
        lam_pair = VGroup(VGroup(lam1, lam1_box), VGroup(lam2, lam2_box)).arrange(RIGHT, buff=1.5)

        s45_col = VGroup(s4_lbl, s4_quad, s4_hint, s4_fact, s5_lbl, lam_pair).arrange(DOWN, buff=0.26)
        s45_col.move_to([0, -1.35, 0])

        self.play(
            FadeOut(s3_lbl),
            FadeOut(s3_line0),
            FadeOut(s3_line1),
            FadeOut(s3_line2),
            FadeOut(s3_box),
            Transform(s3_line3, s4_quad),
            FadeIn(s4_lbl),
            run_time=1.5,
        )
        self.play(FadeIn(s4_hint), run_time=1.8)
        self.wait(1.2)
        self.play(FadeIn(s4_fact, shift=UP * 0.1), run_time=2.2)
        self.wait(1.8)
        self.play(
            FadeIn(s5_lbl),
            FadeIn(lam1, shift=UP * 0.1),
            FadeIn(lam2, shift=UP * 0.1),
            Create(lam1_box),
            Create(lam2_box),
            run_time=2.6,
        )
        self.play(
            Indicate(lam_pair[0], color=RESULT_YELLOW),
            Indicate(lam_pair[1], color=RESULT_YELLOW),
            run_time=1.4,
        )
        self.wait(3.8)
        fade_out_all(self, run_time=0.7)
