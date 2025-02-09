## Topics

### What is a Linear Equation?
$$
a_{1}x_{1}+a_{2}x_{2}+\dots+a_{n}x_{n}=b
$$
where $b$ and the coefficients $a_{1},\dots,a_{n}$ are real or complex numbers (Complex numbers are not used in this course)

#### A System of Linear Equations
A collection of one or more linear equation involving the same variables
$$
\begin{align}
2x_{1}+3x_{2}+7x_{3}&=18 \\
-2x_{1}+2x_{3}&=0 \\
x_{2}&=3
\end{align}
$$
#### A Solution to a System of Linear Equations
A List of numbers $(s_{1},s_{2},\dots,s_{n})$ that makes each equation a true statement when substituted for the variables $(x_{1},x_{2},\dots,x_{n})$ eg. substituting $(1,3,1)$ into $(x_{1},x_{2},x_{3})$
$$
\begin{align}
2(1)+3(3)+7(1)&=18 \\
-2(1)+2(1)&=0 \\
(3)&=3
\end{align}
$$
Which makes all of the equations true.
#### A Solution Set
The collection of all possible solutions to a linear system is called a *solution set*
Two Linear systems are *equivalent* of they have the same solution set.

Ex.
$$
\begin{align}
2x_{1}+3x_{2}&=11 \\
-2x_{1}+2x_{1}&=-6
\end{align}
$$ 
Has one single solution $(x_{1},x_{2})=(4,1)$
$$
\begin{align}
x_{1}+4x_{2}&=8 \\
2x_{1}-x_{2}&=7
\end{align}
$$
Also has the solution $(x_{1},x_{2})=(4,1)$ 


#### Consistency
A system of linear equation is said to be *consistent* if it has at least one solution. Otherwise it is *inconsistent*.

There are $3$ options for the number of solution a system of linear equations can have.
- No solutions
- Exactly one solution
- Infinitely many solution

### Matrix

A *matrix* is a rectangular array of numbers
A matrix with $m$ rows and $n$ columns is referred to as an *m by n matrix* (or m x n matrix)
An m by n matrix has *size* m by n
*The number of rows ___always___ comes first*
$$
\begin{bmatrix}
3 & 3 \\
-2 & 2 \\
3 & 1
\end{bmatrix} \text{is a 3\,x\,2 matrix}
$$
$$
\begin{bmatrix}
4 & -2 & -2 \\
5 & -1 & 3
\end{bmatrix} \text{is a 2\,x\,3 matrix}
$$
#### Matrix Notation
(Writing systems of linear equations as matrices)

If we have:
$$
\begin{align}
x_{1}+3x_{2}+2x_{3}&=13 \\
2x_{1}+3x_{2}-x_{3}&=5 \\
2x_{1}+x_{3}&=5
\end{align}
$$$$

\text{The matrix }\begin{bmatrix}
1 & 3 & 2 \\
2 & 3 & -1 \\
2 & 0 & 1
\end{bmatrix} \text{is called the \textbf{coefficient matrix}.}
$$
Adding another column containing the constants we get
$$
\text{The matrix}
\left[
\begin{matrix}
1 & 3 & 2 \\
2 & 3 & -1 \\
2 & 0 & 1
\end{matrix}
\left|
\begin{matrix}
13 \\
5 \\
5
\end{matrix}
\right.
\right]. \text{This is the \textbf{augmented matrix}.}
$$

$$
$$
