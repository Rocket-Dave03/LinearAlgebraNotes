When a system of linear equations is consistent and it has at least one [[Variable types#free variable|free variable]], it has infinitely many solutions. In this case, the value of the [[Variable types#Basic Variable| basic variable]] can be expressed in terms of the value of the [[Variable types#free variable|free variable]].

# Example 
$$
\left[\begin{matrix}
1 & 0 & 4 & 0 & 2 \\
0 & 1 & -5 & 0 & -3 \\
0 & 0 & 0 & 1 & -4 \\
0 & 0 & 0 & 0 & 0 
\end{matrix}\left|\,\begin{matrix} 
0 \\
2 \\
4 \\
0
\end{matrix}\right.\right]
$$
Write the general solution
$$
\begin{align}
x_{1}+4x_{3}+2x_{5}&=0 \\
x_{2}-5x_{3}-3x_{5}&=2 \\
x_{4}-4x_{5}&=4 \\ \\
\text{Basic: }&x_{1},x_{2},x_{4} \\
\text{Free: }&x_{3},x_{5}
\end{align}
$$
Solve for the basic variables
$$
\begin{align}
x_{1}&=-4x_{3}-2x_{5} \\
x_{2}&=2+5x_{3}+3x_{5} \\
x_{3}&=x_{3} \\
x_{4}&=4+4x_{5} \\
x_{5}&=x_{5}
\end{align}
$$
$$
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4} \\
x_{5}
\end{bmatrix}=\begin{bmatrix}
0 \\
2 \\
0 \\
4 \\
0
\end{bmatrix}+x_{3}\begin{bmatrix}
-4 \\
5 \\
1 \\
4 \\
0
\end{bmatrix}+x_{5}\begin{bmatrix}
-2 \\
3 \\
0 \\
4 \\
1
\end{bmatrix}
$$
![[Theorems#Theorem 2]]
