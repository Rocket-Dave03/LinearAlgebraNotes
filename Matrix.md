A *matrix* is a rectangular array of numbers
A matrix with $m$ rows and $n$ columns is referred to as an *m by n matrix* (or m x n)

A $m\times n$ matrix has *size* $m$ by $n$

*The number of row is __always__ given first*

$$
\begin{bmatrix}
3 & 3 \\
2 & 2 \\
3 & 1 \\
\end{bmatrix} \text{is a } 3\times 2 \text{ matrix}
$$
$$
\begin{bmatrix}
4 & -2 & -2 \\
5 & -1 & 3
\end{bmatrix} \text{is a } 3\times 2 \text{ matrix}
$$

## Matrix Notation
### Coefficient Matrix
If have a system of linear equations
$$
\begin{align}
x_{1}+3x_{2}+2x_{3}&=13 \\
2x_{1}+3x_{2}-x_{3}&=5 \\
2x_{1}-x_{3}&=5
\end{align}
$$
The matrix $\begin{bmatrix}1 & 3 & 2 \\ 2 & 3 & -1  \\ 2 & 0 & -1\end{bmatrix}$ is called the *coefficient matrix*
### Augmented Matrix
If we add in another column, consisting of the constants we get the matrix $$\left[\begin{matrix}1 & 3 & 2 \\ 2 & 3 & -1 \\ 2 & 0 & -1\end{matrix}\left|\,\begin{matrix}13 \\ 5 \\ 5\end{matrix}\right.\right]$$
This called the *augmented matrix*
