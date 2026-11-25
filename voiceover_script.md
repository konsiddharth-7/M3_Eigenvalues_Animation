# Voice-Over Narration Script: Eigenvalues and Eigenvectors

**Target Duration:** ~300 seconds (5 minutes 00 seconds)  
**Pacing:** Slow, conversational educational pace (~85–90 words per minute, with intentional pauses for visual absorption)  
**Student:** SIDDHARTH KONDERU | **Student ID:** E25B070643  
**Spoken Word Count:** ~430 words (excluding timestamps and stage cues)

> **Recording Tip:** Read calmly and clearly. Leave 1.5 to 3 seconds of silence wherever a `[PAUSE]` cue appears so viewers can read the equations and watch the vectors move.

---

## Scene 1 — The Hook (0:00 – 0:35) [35 seconds]

**[0:00 – 0:08]**  
`[VISUAL SYNC: Opening frame fades into the 2D Cartesian grid with cyan vectors radiating from the origin.]`  
Imagine a flat grid covered with arrows, all pointing outward from the origin in different directions.

**[0:08 – 0:18]**  
`[VISUAL SYNC: The matrix transformation smoothly warps the grid and transforms all vectors to orange.]`  
Now, watch what happens when we apply a linear transformation to the entire plane. Almost every arrow swings toward a new direction and changes its length.

**[0:18 – 0:28]**  
`[VISUAL SYNC: All non-invariant vectors dim; the two green eigenvectors along y = x and y = -x pulse and glow.]`  
Wait—look closely at these two green vectors. Even as the whole grid stretches around them, neither one turns away from its original line.  
`[PAUSE: 2 seconds]`

**[0:28 – 0:35]**  
`[VISUAL SYNC: Guiding question appears, followed by the main title "EIGENVALUES & EIGENVECTORS".]`  
Why do some vectors change direction while others don't? That mystery is the heart of eigenvalues and eigenvectors.

---

## Scene 2 — Understanding Linear Transformations (0:35 – 1:15) [40 seconds]

**[0:35 – 0:47]**  
`[VISUAL SYNC: Matrix A = [[2, 1], [1, 2]] and arbitrary vector v = [x, y]^T appear on the left panel.]`  
Before solving that mystery, let's see what a matrix actually does. Take this two-by-two matrix A. When we multiply it by a vector v with coordinates x and y...

**[0:47 – 1:00]**  
`[VISUAL SYNC: Matrix-vector multiplication expands into [2x + y, x + 2y]^T; grid and basis/sample vectors animate on the right.]`  
...each output coordinate becomes a linear combination of the inputs: two x plus y on top, and x plus two y below. Geometrically, this rule warps the entire coordinate grid while keeping grid lines parallel and evenly spaced.

**[1:00 – 1:15]**  
`[VISUAL SYNC: Multiple cyan input vectors transform into orange output vectors; direction change vs. length change are highlighted.]`  
Notice how an ordinary input vector changes both its angle and its length. A matrix isn't just a grid of numbers—it's a geometric machine that moves vectors through space. So what makes those green directions special?

---

## Scene 3 — Eigenvalues and Eigenvectors (1:15 – 2:00) [45 seconds]

**[1:15 – 1:29]**  
`[VISUAL SYNC: Central equation Av = λv appears prominently, with color-coded callouts for A, v, λ, Av, and λv.]`  
Here is the central equation of the topic: A times v equals lambda times v. On the left, matrix A transforms the non-zero vector v. On the right, lambda—a single scalar—simply stretches or shrinks v without rotating it.  
`[PAUSE: 2 seconds]`

**[1:29 – 1:43]**  
`[VISUAL SYNC: Green vector along y = x transforms to 3 times its length; yellow badge λ = 3 appears.]`  
Look at a vector lying along the line y equals x. Under our transformation, it stays locked on the exact same line, but grows to three times its original length. Here, the scaling factor lambda is three.

**[1:43 – 2:00]**  
`[VISUAL SYNC: Green vector along y = -x transforms onto itself; yellow badge λ = 1 appears; both invariant lines glow with definitions.]`  
Now test a vector along y equals negative x. It doesn't rotate, and its length stays identical—a scaling factor of lambda equals one. Remember the distinction: the eigenvector is the invariant direction, and the eigenvalue is its scaling factor.

---

## Scene 4 — Mathematical Derivation (2:00 – 3:15) [75 seconds]

**[2:00 – 2:18]**  
`[VISUAL SYNC: Av = λv rearranges into (A - λI)v = 0; identity matrix I and singular matrix note appear.]`  
How do we find these special numbers algebraically? Start with A times v equals lambda times v, and move everything to one side using the identity matrix I, giving A minus lambda I, times v, equals zero.

**[2:18 – 2:34]**  
`[VISUAL SYNC: det(A - λI) = 0 is boxed and highlighted.]`  
We only care about non-zero eigenvectors. A matrix can send a non-zero vector to zero only when it collapses space—meaning the matrix A minus lambda I must be singular, so its determinant equals zero.  
`[PAUSE: 2 seconds]`

**[2:34 – 2:52]**  
`[VISUAL SYNC: Step 1 builds A - λI = [[2 - λ, 1], [1, 2 - λ]]; Step 2 highlights main and anti-diagonal determinant calculation.]`  
Let's plug in our matrix A. Subtracting lambda from the diagonal entries gives two minus lambda along the main diagonal. Taking the two-by-two determinant gives two minus lambda, squared, minus one times one, equal to zero.

**[2:52 – 3:15]**  
`[VISUAL SYNC: Step 3 expands to λ^2 - 4λ + 3 = 0; Step 4 factors into (λ - 3)(λ - 1) = 0; Step 5 boxes λ1 = 3 and λ2 = 1.]`  
Expanding the square and combining constants gives the quadratic equation: lambda squared minus four lambda plus three equals zero. Factoring gives lambda minus three times lambda minus one equals zero. So our two eigenvalues are three and one.  
`[PAUSE: 2 seconds]`

---

## Scene 5 — Finding the Eigenvectors (3:15 – 4:35) [80 seconds]

**[3:15 – 3:38]**  
`[VISUAL SYNC: Part A header; (A - 3I)v = 0 expands to [[-1, 1], [1, -1]][x, y]^T = [0, 0]^T, then -x + y = 0 and x = y.]`  
Now let's find the direction for each eigenvalue. For lambda equals three, substitute three into A minus lambda I. Both rows give the same condition: negative x plus y equals zero, so x equals y.

**[3:38 – 3:50]**  
`[VISUAL SYNC: v1 = [1, 1]^T appears, with scaled copies along y = x.]`  
Setting x equal to one gives our first eigenvector, one, one. Any non-zero multiple of this vector shares the same invariant line.

**[3:50 – 4:10]**  
`[VISUAL SYNC: Part B header; (A - I)v = 0 expands to [[1, 1], [1, 1]][x, y]^T = [0, 0]^T, then x + y = 0 and x = -y, giving v2 = [1, -1]^T.]`  
Next, for lambda equals one, A minus I gives all ones. That simplifies to x plus y equals zero, or x equals negative y. Setting x equal to one gives our second eigenvector, one, negative one.

**[4:10 – 4:35]**  
`[VISUAL SYNC: Part C split verification: graph animates A[1,1]^T -> [3,3]^T and A[1,-1]^T -> [1,-1]^T side-by-side with algebraic check.]`  
Let's verify this visually. Feeding one, one into matrix A produces three, three—exactly three times the input. Feeding one, negative one returns one, negative one—completely unchanged. Both eigenvectors stay perfectly aligned, confirming our algebra.  
`[PAUSE: 2 seconds]`

---

## Scene 6 — Interpretation and Conclusion (4:35 – 5:00) [25 seconds]

**[4:35 – 4:50]**  
`[VISUAL SYNC: Transformed grid returns with both green eigenvector axes highlighted; 3 takeaways appear sequentially.]`  
Stepping back, eigenvectors reveal the natural axes of a linear transformation. Along those special directions, a complex matrix acts just like simple scalar multiplication, and the characteristic determinant lets us uncover them every time.

**[4:50 – 5:00]**  
`[VISUAL SYNC: Closing quote appears, followed by THANK YOU card with topic, student placeholders, AI disclosure, and references.]`  
In short, eigenvalues reveal how a transformation acts along its special directions. Thank you for watching.
