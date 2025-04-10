# Linear Dependence
A set for vectors $u_{1},u_{2},\dots,u_{k}$ is *linearly dependent* if there is exist scalars $c_{1},c_{2}\dots,c_{k}$ not all zero, such that $c_{1}u_{1}+c_{2}u_{2},\dots,c_{k}u_{k}=0$

Example
$$
\left\{\begin{bmatrix}1 \\2 \\1\end{bmatrix}\right\},\begin{bmatrix}
2\\1\\-3
\end{bmatrix}\begin{bmatrix}
3 \\
5 \\
-2
\end{bmatrix}
\begin{bmatrix}
1 \\
0 \\
1
\end{bmatrix}$$
Is linearly independent since
$$
2\begin{bmatrix}
1 \\
2 \\
1
\end{bmatrix}
+1
\begin{bmatrix}
2 \\
1 \\
-3
\end{bmatrix}
-1\begin{bmatrix}
3 \\
5 \\
-2
\end{bmatrix}
-1\begin{bmatrix}
1 \\
0 \\
1
\end{bmatrix}=\begin{bmatrix}
0 \\
0 \\
0
\end{bmatrix}
$$
# Linear Independence
A set of vectors $\{u_{1},u_{2},\dots,u_{K}\}$ is *linearly independent* if the only scalars $c_{1},c_{2},\dots,c_{k}$ that satisfy $c_{1}u_{1}+c_{2}u_{2}+\dots+c_{k}u_{k}=0$ are $c_{1}=c_{2}=\dots=c_{k}=0$

# Linear Independence of Matrix Columns
The columns of a matrix $A$ are linearly independent if and only if the equation $Ax = 0$ has only the trivial solution.

Facts:  
- The columns of a matrix $A$ are linearly *independent* if the matrix equation $Ax$ has $x = 0$ as its unique solution.  
- The columns of a matrix $A$ are linearly *dependent* if the matrix equations $Ax = 0$ has an infinite number of solutions.  
- The columns of a matrix $A$ are linearly *independent* if the matrix equation $Ax = b$ has at most one solution.  
- The columns of a matrix $A$ are linearly *dependent* if the matrix equation $Ax = b$ has an infinite number of solutions. 

![[Theorems#Theorem 7]]

![[Theorems#Theorem 8]]

![[Theorems#Theorem 9]]