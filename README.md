# Eigenvalues and Eigenvectors — M3 Mathematics Animation

**Linear Algebra and Calculus (M3) • Internal Assessment (Project Option 1: Animation Video)**  
**Topic:** Eigenvalues and Eigenvectors — *Understanding invariant directions under linear transformations*  
**Student:** `SIDDHARTH KONDERU` | **Student ID:** `E25B070643`

---

## Project Objective

This project builds a 5-minute (300-second), Full HD (1920 × 1080, 16:9) educational mathematics animation that explains **eigenvalues and eigenvectors** visually and algebraically for second-year undergraduate students. Rather than jumping straight to formulas, the animation builds geometric intuition first—showing how a linear transformation warps space while leaving special invariant directions untouched—before deriving the characteristic equation and verifying the worked example visually.

> **Audio Note:** Per project specifications, the rendered MP4 video contains **no synthesized voice-over or background music**. A separate, slow-paced narration script synchronized to exact scene timestamps is provided in [`voiceover_script.md`](./voiceover_script.md) for manual recording.

---

## Mathematical Concepts Covered

- **Linear Transformations:** Representing a $2 \times 2$ matrix $A$ as a geometric mapping $\mathbf{v} \mapsto A\mathbf{v}$ that changes vector direction and magnitude.
- **Invariant Directions & Scaling:** The fundamental eigenpair equation $A\mathbf{v} = \lambda \mathbf{v}$ ($\mathbf{v} \neq \mathbf{0}$), distinguishing eigenvectors (invariant directions) from eigenvalues (scalar scaling factors).
- **Characteristic Equation:** Rearranging $A\mathbf{v} = \lambda \mathbf{v}$ to $(A - \lambda I)\mathbf{v} = \mathbf{0}$ and using the singularity condition $\det(A - \lambda I) = 0$.
- **Eigenspace & Scalar Multiples:** Solving $(A - \lambda I)\mathbf{v} = \mathbf{0}$ for each eigenvalue and understanding why any non-zero scalar multiple $c\mathbf{v}$ remains an eigenvector.
- **Geometric Verification:** Checking algebraic eigenpairs directly against the coordinate transformation.

---

## Mathematical Results & Verification (Worked Example)

Throughout the video, the worked example uses the symmetric $2 \times 2$ matrix:

$$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

### 1. Action on an Arbitrary Vector
$$A\mathbf{v} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + y \\ x + 2y \end{bmatrix}$$

### 2. Characteristic Equation & Eigenvalues
$$A - \lambda I = \begin{bmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{bmatrix}$$
$$\det(A - \lambda I) = (2 - \lambda)(2 - \lambda) - (1 \times 1) = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$$
$$(\lambda - 3)(\lambda - 1) = 0 \implies \mathbf{\lambda_1 = 3}, \quad \mathbf{\lambda_2 = 1}$$

### 3. Eigenvectors & Substitution Check
- **For $\lambda_1 = 3$:**
  $$(A - 3I)\mathbf{v} = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies -x + y = 0 \implies x = y \implies \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
  **Verification:** $A\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2(1) + 1(1) \\ 1(1) + 2(1) \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix} = 3\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ ✓

- **For $\lambda_2 = 1$:**
  $$(A - I)\mathbf{v} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies x + y = 0 \implies x = -y \implies \mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$$
  **Verification:** $A\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 2(1) + 1(-1) \\ 1(1) + 2(-1) \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix} = 1\begin{bmatrix} 1 \\ -1 \end{bmatrix}$ ✓

---

## Six-Scene Breakdown (~300 Seconds)

| Scene | Time | Duration | Summary |
|---|---|---|---|
| **1. The Hook** | `0:00 – 0:35` | 35 s | Introduces the grid transformation puzzle and highlights two green vectors that keep their direction. |
| **2. Understanding Linear Transformations** | `0:35 – 1:15` | 40 s | Demonstrates matrix-vector multiplication $A\mathbf{v} = [2x+y, x+2y]^T$ and compares angle vs. length changes. |
| **3. Eigenvalues & Eigenvectors** | `1:15 – 2:00` | 45 s | Explains $A\mathbf{v} = \lambda\mathbf{v}$ and animates $y=x$ ($\lambda=3$) and $y=-x$ ($\lambda=1$). |
| **4. Mathematical Derivation** | `2:00 – 3:15` | 75 s | Derives $(A - \lambda I)\mathbf{v} = \mathbf{0}$, $\det(A - \lambda I) = 0$, and solves $\lambda_1 = 3, \lambda_2 = 1$ step by step. |
| **5. Finding the Eigenvectors** | `3:15 – 4:35` | 80 s | Solves for $\mathbf{v}_1 = [1, 1]^T$ and $\mathbf{v}_2 = [1, -1]^T$, shows scalar multiples, and visually verifies both. |
| **6. Interpretation & Conclusion** | `4:35 – 5:00` | 25 s | Recaps 3 key takeaways on the transformed grid and displays final credits & disclosure. |

---

## Tools & Technologies Used

- **Python 3.12** & **Manim Community (`manim`)** — programmatic mathematical animation engine
- **MathJax (`mathjax-full` via Node.js)** — standalone LaTeX-to-SVG vector typography rendering
- **FFmpeg / FFprobe** — lossless MP4 scene concatenation, silent stream packaging, and verification
- **NumPy** — matrix/vector calculations
- **ReportLab** — storyboard PDF generation

---

## Project File Structure

```text
M3_Eigenvalues_Animation/
├── main.py                        # Master renderer & FFmpeg stitcher
├── generate_storyboard_pdf.py     # Generates storyboard.pdf
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── storyboard.md                  # 6-scene storyboard (Markdown)
├── storyboard.pdf                 # 6-scene storyboard (PDF for submission)
├── voiceover_script.md            # Timestamped ~430-word slow-paced script
├── scenes/
│   ├── __init__.py
│   ├── common.py                  # Palette, MathJax SVG helper, grid & vector tools
│   ├── scene_1_hook.py            # Scene 1 (0:00–0:35)
│   ├── scene_2_transformations.py # Scene 2 (0:35–1:15)
│   ├── scene_3_eigen_concept.py   # Scene 3 (1:15–2:00)
│   ├── scene_4_derivation.py      # Scene 4 (2:00–3:15)
│   ├── scene_5_eigenvectors.py    # Scene 5 (3:15–4:35)
│   └── scene_6_conclusion.py      # Scene 6 (4:35–5:00)
├── assets/
│   └── mathjax/                   # MathJax LaTeX -> SVG converter
└── output/
    └── eigenvalues_eigenvectors.mp4  # Final 1080p 16:9 silent MP4 (~300s)
```

---

## Installation & Rendering Instructions

### 1. System Prerequisites (macOS / Homebrew)
```bash
brew install ffmpeg cairo pango pkg-config node
```

### 2. Python & MathJax Setup
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd assets/mathjax
npm install
cd ../..
```

### 3. Render the Animation
```bash
# Full HD 1920x1080 (16:9, 30fps, silent MP4)
python main.py

# Fast 480p preview render
python main.py --preview

# Render a single scene (1–6) at 1080p
python main.py --scene 4
```

Output video will be written to `output/eigenvalues_eigenvectors.mp4`.

---

## AI Tools Disclosure

In accordance with the M3 Internal Assessment originality policy:
- AI coding assistance was used to help write the Python/Manim scene scripts, MathJax SVG integration, storyboard formatting, and narration script draft.
- All mathematical definitions, derivations, matrix calculations, eigenvalue/eigenvector substitutions, and visual checks were independently verified.

## References

1. Strang, G. *Introduction to Linear Algebra* (5th ed.), Wellesley-Cambridge Press.
2. Sanderson, G. (3Blue1Brown). *Essence of Linear Algebra — Chapter 14: Eigenvectors and Eigenvalues*.
3. M3 Linear Algebra and Calculus Course Lecture Notes.
