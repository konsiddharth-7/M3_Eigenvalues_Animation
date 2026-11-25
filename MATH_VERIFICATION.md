# Mathematical Verification Report
## Eigenvalues and Eigenvectors — Worked Example Verification

**Matrix Under Analysis:**
$$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

---

## ✅ 1. Matrix-Vector Multiplication (Scene 2)

For arbitrary vector $\mathbf{v} = [x, y]^T$:

$$A\mathbf{v} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2(x) + 1(y) \\ 1(x) + 2(y) \end{bmatrix} = \begin{bmatrix} 2x + y \\ x + 2y \end{bmatrix}$$

**Sample check** — $[1, 0]^T$:
$$A\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2(1) + 1(0) \\ 1(1) + 2(0) \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix} \quad \checkmark$$

Length change: $\|[1,0]^T\| = 1$ → $\|[2,1]^T\| = \sqrt{4+1} = \sqrt{5} \approx 2.236 \quad \checkmark$

---

## ✅ 2. Characteristic Equation Derivation (Scene 4)

**Step 1:** Starting from $A\mathbf{v} = \lambda\mathbf{v}$ with $\mathbf{v} \neq \mathbf{0}$:

$$A\mathbf{v} - \lambda\mathbf{v} = \mathbf{0} \implies (A - \lambda I)\mathbf{v} = \mathbf{0}$$

For a non-trivial solution (eigenvector $\mathbf{v} \neq \mathbf{0}$) to exist, $(A - \lambda I)$ must be singular:

$$\det(A - \lambda I) = 0$$

**Step 2:** Construct $A - \lambda I$:

$$A - \lambda I = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix}$$

**Step 3:** Compute the determinant:

$$\det\begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix} = (2-\lambda)(2-\lambda) - (1)(1)$$

$$= (2-\lambda)^2 - 1$$

$$= 4 - 4\lambda + \lambda^2 - 1$$

$$= \lambda^2 - 4\lambda + 3$$

**Step 4:** Set equal to zero and factorize:

$$\lambda^2 - 4\lambda + 3 = 0$$

Factoring: find two numbers that multiply to $+3$ and add to $-4$: they are $-3$ and $-1$.

$$(\lambda - 3)(\lambda - 1) = 0$$

**Verification of factorization:**
$$(\lambda-3)(\lambda-1) = \lambda^2 - \lambda - 3\lambda + 3 = \lambda^2 - 4\lambda + 3 \quad \checkmark$$

**Step 5:** Eigenvalues:

$$\boxed{\lambda_1 = 3, \quad \lambda_2 = 1}$$

---

## ✅ 3. Eigenvector for $\lambda_1 = 3$ (Scene 5, Part A)

Solve $(A - 3I)\mathbf{v} = \mathbf{0}$:

$$A - 3I = \begin{bmatrix} 2-3 & 1 \\ 1 & 2-3 \end{bmatrix} = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}$$

System of equations:
- Row 1: $-x + y = 0 \implies x = y$
- Row 2: $x - y = 0 \implies x = y$ (same equation — consistent ✓, as expected for a rank-1 matrix)

Setting $x = 1$: $y = 1$, so:

$$\boxed{\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}}$$

Any non-zero scalar multiple $c\mathbf{v}_1$ (where $c \neq 0$) is also an eigenvector for $\lambda_1 = 3$.

**Direct verification:**

$$A\mathbf{v}_1 = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2(1)+1(1) \\ 1(1)+2(1) \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix} = 3\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \lambda_1 \mathbf{v}_1 \quad \checkmark$$

---

## ✅ 4. Eigenvector for $\lambda_2 = 1$ (Scene 5, Part B)

Solve $(A - I)\mathbf{v} = \mathbf{0}$:

$$A - I = \begin{bmatrix} 2-1 & 1 \\ 1 & 2-1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$$

System of equations:
- Row 1: $x + y = 0 \implies x = -y$
- Row 2: $x + y = 0$ (identical — consistent ✓)

Setting $x = 1$: $y = -1$, so:

$$\boxed{\mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}}$$

**Direct verification:**

$$A\mathbf{v}_2 = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 2(1)+1(-1) \\ 1(1)+2(-1) \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix} = 1\cdot\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \lambda_2 \mathbf{v}_2 \quad \checkmark$$

---

## ✅ 5. Orthogonality Check (Bonus — Valid for Symmetric Matrices)

Since $A$ is real symmetric ($A = A^T$), the Spectral Theorem guarantees eigenvectors corresponding to **distinct** eigenvalues are orthogonal.

$$\mathbf{v}_1 \cdot \mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ -1 \end{bmatrix} = (1)(1) + (1)(-1) = 1 - 1 = 0 \quad \checkmark$$

The eigenvectors $[1,1]^T$ (along $y=x$) and $[1,-1]^T$ (along $y=-x$) are **perpendicular**. This matches the visual animation.

---

## ✅ 6. Trace & Determinant Consistency Check

For a $2 \times 2$ matrix $A$, the characteristic polynomial satisfies:

$$\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$$

- $\text{tr}(A) = 2 + 2 = 4$
- $\det(A) = (2)(2) - (1)(1) = 4 - 1 = 3$
- Expected: $\lambda^2 - 4\lambda + 3 = 0$ ✓
- Also: $\lambda_1 + \lambda_2 = 3 + 1 = 4 = \text{tr}(A)$ ✓
- Also: $\lambda_1 \times \lambda_2 = 3 \times 1 = 3 = \det(A)$ ✓

All results are **mathematically consistent and independently verified**.

---

## Summary Table

| Quantity | Expected | Computed | Status |
|---|---|---|---|
| Characteristic polynomial | $\lambda^2 - 4\lambda + 3 = 0$ | Same | ✅ |
| Eigenvalue 1 | $\lambda_1 = 3$ | $\lambda_1 = 3$ | ✅ |
| Eigenvalue 2 | $\lambda_2 = 1$ | $\lambda_2 = 1$ | ✅ |
| Eigenvector for $\lambda_1 = 3$ | direction $[1,1]^T$ | $v_1 = [1,1]^T$ | ✅ |
| Eigenvector for $\lambda_2 = 1$ | direction $[1,-1]^T$ | $v_2 = [1,-1]^T$ | ✅ |
| $A[1,1]^T$ | $[3,3]^T$ | $[3,3]^T$ | ✅ |
| $A[1,-1]^T$ | $[1,-1]^T$ | $[1,-1]^T$ | ✅ |
| $\lambda_1 + \lambda_2$ = tr(A) | $4$ | $3+1=4$ | ✅ |
| $\lambda_1 \times \lambda_2$ = det(A) | $3$ | $3\times1=3$ | ✅ |
| Orthogonality $v_1 \cdot v_2$ | $0$ | $0$ | ✅ |
