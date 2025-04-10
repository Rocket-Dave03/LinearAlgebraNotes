1. Add a multiple of one row to another row $$
\begin{bmatrix}
1 & 3 & 2 \\
2 & 1 & -1 \\
2 & 0 & 3
\end{bmatrix} \to \begin{bmatrix}
1 & 3 & 2 \\
4 & 7 & 3 \\
2 & 0 & 3
\end{bmatrix}\,\,(2r_{1}+r_{2}\to r_{2})
$$
2. Interchange any two rows of the [[Matrix]] $$
\begin{bmatrix}
1 & 3 & 2 \\
2 & 1 & -1  \\
2 & 0 & 3
\end{bmatrix}\to \begin{bmatrix}
1 & 3 & 2 \\
2 & 9 & 3 \\
2 & 1 & -1
\end{bmatrix}\,\,(r_{2}\leftrightarrow r_{3})
$$
3. Multiply every entry of some row by some nonzero scalar 
$$
\begin{bmatrix}
 1 & 3 & 2 \\
2 & 1 & -1 \\
2 & 0 & 3
\end{bmatrix} \to \begin{bmatrix}
1 & 3 & 2 \\
6 & 3 & -3 \\
2 & 0 & 3
\end{bmatrix}\,\,(3r_{2}\to r_{2})
$$
Any two [[Matrix|matrices]] are called *row equivalent* if there is a sequence of elementary row operation that transform one matrix into the other

> [!Example]
> $$\begin{bmatrix}1 & 3 & 2 & 13 \\2 & 3 & -1 & 5 \\2 & 0 & 1 & 5 \\ \end{bmatrix} \text{is row equivalent to}\begin{bmatrix}1 & 0 & 0 & 1 \\0 & 1 & 0 & 2 \\0 & 0 & 1 & 3 \\\end{bmatrix}$$

