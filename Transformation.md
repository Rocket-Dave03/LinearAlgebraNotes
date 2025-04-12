# Definitions
### Transformation
A function (or transformation)  $\large{f:A\to B}$  is a rule that assigns every element in set $A$ to an element in set $B$. 

The set $A$ is called the **domain** of $F$ and set $B$ is called the *co-domain* of $f$ ^domain
### Range
The **range** if a transformation function $\large{f: A\to B}$ is the set of all possible values $f(a)$ where $a \in A$

# Matrix Transformation
If $A$ is an $m\times n$ matrix, then if $x$ is any vector in $R^n$, let
$$
T(x)=Ax
$$
Observe that this takes any vector in $R^n$ and "transforms" it into a vector in $R^m$ 
This is a **matrix transformation** denoted $\large{x\mapsto Ax}$

> [!Example]
> $T:R^{3}\to R^{2}$ defined by $T\left(\begin{bmatrix}x_{1} \\ x_{2} \\ x_{3}\end{bmatrix}\right)=\begin{bmatrix}2 & 2 & -3 \\ 3 & -1 & 2\end{bmatrix}\begin{bmatrix}x_{1}  \\ x_{2} \\ x_{3}\end{bmatrix}$
# Linear Transformation
A **linear transformation** $\large{T:R^n\to R^m}$ is a function where the following conditions hold for any vectors $\vec{u},\vec{v} \in R^n$ and $c$ is any scalar
1. $\large T(u+v)=T(u) + T(v)$
2. $\large T(cu)=c \cdot T(u)$

> [!Note]
> Every [[#Matrix Transformation]] is a *linear transformation*

For any linear transformation $\large T: R^n\to R^m$ the following are true:
1. $T(0)=0$
2. $T(-u)=-T(u) \text{ for all } u \in R^n$
3. $T(u-v)=T(u)-T(v) "\text{ for all } u,v \in R^n$
4. $T(au+bv)=aT(u)+bT(v) \text{ for all } u,v \in R^n \text{ and scalars } a,b$
