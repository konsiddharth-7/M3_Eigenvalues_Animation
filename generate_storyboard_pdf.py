"""Generate a clean PDF version of the 6-Scene Storyboard for GitHub submission."""

from __future__ import annotations

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def build_pdf(output_path: Path) -> None:
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=landscape(A4),
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontSize=18,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=4,
    )
    meta_style = ParagraphStyle(
        "MetaStyle",
        parent=styles["Normal"],
        fontSize=9.5,
        textColor=colors.HexColor("#334155"),
        leading=13,
    )
    cell_style = ParagraphStyle(
        "CellStyle",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#0F172A"),
    )
    head_style = ParagraphStyle(
        "HeadStyle",
        parent=styles["Normal"],
        fontSize=9,
        leading=11,
        textColor=colors.white,
        fontName="Helvetica-Bold",
    )

    story = [
        Paragraph("6-Scene Storyboard: Eigenvalues and Eigenvectors", title_style),
        Paragraph(
            "<b>Course:</b> Linear Algebra &amp; Calculus (M3) Internal Assessment &nbsp;|&nbsp; "
            "<b>Format:</b> 1920 x 1080 (16:9) MP4, ~300s (5:00) &nbsp;|&nbsp; "
            "<b>Student:</b> SIDDHARTH KONDERU (E25B070643)",
            meta_style,
        ),
        Paragraph(
            "<b>Learning Objective:</b> By the end of this video, the viewer will be able to understand, "
            "calculate, and geometrically interpret eigenvalues and eigenvectors of a 2 x 2 matrix as "
            "invariant directions and scaling factors under a linear transformation.",
            meta_style,
        ),
        Spacer(1, 6 * mm),
    ]

    rows = [
        [
            Paragraph("Scene &amp; Timing", head_style),
            Paragraph("Purpose", head_style),
            Paragraph("Visual &amp; Animation Plan", head_style),
            Paragraph("Mathematical Content &amp; Sync", head_style),
        ],
        [
            Paragraph("<b>1. The Hook</b><br/>0:00 - 0:35 (35s)", cell_style),
            Paragraph("Spark curiosity and introduce invariant directions.", cell_style),
            Paragraph(
                "Opening assessment frame fades into 2D grid with 8 cyan vectors. "
                "Matrix A warps grid; ordinary vectors rotate/stretch to orange; "
                "2 green vectors on y=x and y=-x stay aligned. Question &amp; title reveal.",
                cell_style,
            ),
            Paragraph(
                "A = [[2,1],[1,2]]. Non-invariant vectors rotate; [1,1]<sup>T</sup> and "
                "[1.5,-1.5]<sup>T</sup> stay collinear. Prompt: <i>Why do some vectors change direction while others don't?</i>",
                cell_style,
            ),
        ],
        [
            Paragraph("<b>2. Linear Transformations</b><br/>0:35 - 1:15 (40s)", cell_style),
            Paragraph("Explain matrix multiplication as space transformation.", cell_style),
            Paragraph(
                "Split screen: algebra left, live plane right. Introduces A and v=[x,y]<sup>T</sup>, "
                "animates Av=[2x+y, x+2y]<sup>T</sup>, warps grid and multiple sample vectors, "
                "highlights angle vs. length changes, bridges to special lines.",
                cell_style,
            ),
            Paragraph(
                "A = [[2,1],[1,2]], v=[x,y]<sup>T</sup>, Av=[2x+y, x+2y]<sup>T</sup>. "
                "Sample: [1,0]<sup>T</sup> -&gt; [2,1]<sup>T</sup> (length 1 -&gt; sqrt(5)).",
                cell_style,
            ),
        ],
        [
            Paragraph("<b>3. Eigenvalues &amp; Eigenvectors</b><br/>1:15 - 2:00 (45s)", cell_style),
            Paragraph("Define Av = lambda v and distinguish direction vs. scale.", cell_style),
            Paragraph(
                "Color-coded equation Av = lambda v with 5 symbol legend pills. "
                "Animates y=x stretching 3x (lambda=3) and y=-x staying 1x (lambda=1). "
                "Highlights both dashed invariant lines.",
                cell_style,
            ),
            Paragraph(
                "Av = lambda v (v != 0). Along y=x: A[1,1]<sup>T</sup> = 3[1,1]<sup>T</sup> (lambda=3). "
                "Along y=-x: A[1,-1]<sup>T</sup> = 1[1,-1]<sup>T</sup> (lambda=1).",
                cell_style,
            ),
        ],
        [
            Paragraph("<b>4. Mathematical Derivation</b><br/>2:00 - 3:15 (75s)", cell_style),
            Paragraph("Derive characteristic equation and solve eigenvalues.", cell_style),
            Paragraph(
                "One-step-at-a-time derivation: rearranges Av=lambda v, highlights singular matrix "
                "condition, constructs A - lambda I, highlights determinant diagonals, expands, "
                "factors, and boxes eigenvalues in yellow.",
                cell_style,
            ),
            Paragraph(
                "(A - lambda I)v = 0 =&gt; det(A - lambda I) = 0. "
                "(2 - lambda)<sup>2</sup> - 1 = 0 =&gt; lambda<sup>2</sup> - 4 lambda + 3 = 0 "
                "=&gt; (lambda - 3)(lambda - 1) = 0 =&gt; lambda<sub>1</sub>=3, lambda<sub>2</sub>=1.",
                cell_style,
            ),
        ],
        [
            Paragraph("<b>5. Finding Eigenvectors</b><br/>3:15 - 4:35 (80s)", cell_style),
            Paragraph("Compute v1, v2 and verify visually under A.", cell_style),
            Paragraph(
                "Part A solves (A-3I)v=0 and illustrates scalar multiples c[1,1]<sup>T</sup>. "
                "Part B solves (A-I)v=0. Part C animates both vectors on a split-screen plane "
                "alongside exact matrix-multiplication checks.",
                cell_style,
            ),
            Paragraph(
                "lambda=3: -x+y=0 =&gt; v<sub>1</sub>=[1,1]<sup>T</sup>; A[1,1]<sup>T</sup>=[3,3]<sup>T</sup>. "
                "lambda=1: x+y=0 =&gt; v<sub>2</sub>=[1,-1]<sup>T</sup>; A[1,-1]<sup>T</sup>=[1,-1]<sup>T</sup>.",
                cell_style,
            ),
        ],
        [
            Paragraph("<b>6. Interpretation &amp; Conclusion</b><br/>4:35 - 5:00 (25s)", cell_style),
            Paragraph("Reinforce takeaways and present closing credits.", cell_style),
            Paragraph(
                "Transformed grid returns with green eigenvector axes and 3 numbered takeaway cards. "
                "Concludes with summary quote and THANK YOU frame (topic, student placeholders, "
                "AI disclosure, references).",
                cell_style,
            ),
            Paragraph(
                "Takeaways: (1) Eigenvectors preserve direction; (2) Eigenvalues give scaling; "
                "(3) Found via det(A - lambda I) = 0.",
                cell_style,
            ),
        ],
    ]

    table = Table(rows, colWidths=[42 * mm, 44 * mm, 92 * mm, 91 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#CBD5E1")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(table)
    doc.build(story)


if __name__ == "__main__":
    build_pdf(Path(__file__).resolve().parent / "storyboard.pdf")
    print("Generated storyboard.pdf")
