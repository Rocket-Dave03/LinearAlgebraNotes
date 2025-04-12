# Theorem 1
Each [[Matrix|matrix]] is equivalent to one and one one [[Echelon Forms#Reduced Row Echelon Form|reduced echelon]] matrix

# Theorem 2
A linear system is consistent if and only if the rightmost column of the [[Matrix#Augmented Matrix|Augmented Matrix]] is non a [[Row Reduction#*Pivot column*|pivot column]].

If a linear system is consistent then the solution set contains either 
1. A unique solution (when there are no free variables)
2. Infinitely many solutions (when there is at least one free variable)

# Theorem 3
If A is a $m\times n$ matrix, with columns $a_{1},\dots,a_{n}$ and if $b \in R^m$ , the matrix equation
$$
Ax=b
$$
Has the same solution set as the vector equation
$$
x_{1}a_{1}+\dots+x_{n}a_{n}=b
$$
Which, in turn, as the same solution set as the system of linear equations whose augmented matrix is
$$
\begin{bmatrix}
a_{1} & \dots & a_{n} & b
\end{bmatrix}
$$
# Theorem 4
Let $A$ be a $m \times n$ [[Matrix]]. The the following statements are logically equivalent. The is, is, for a particular $A$, either they are all true statements or they are all false.
1. For each $b$ in $R^m$, the equation $Ax = b$ has a solution
2. Each $b$ in $R^m$ is a linear combination of the columns of $A$
3. The columns if $A$ [[Span]] $R^m$
4. The is a [[Row Reduction#*Pivot position*|pivot position]] in every row of $A$


*Note: This theorem uses the [[Matrix#Coefficient Matrix|coefficient matrix]] $A$, not the [[Matrix#Augmented Matrix|augmented matrix]] $\begin{bmatrix}A & b\end{bmatrix}$*

# Theorem 5
If $A$ is a $m \times n$ matrix, $u$ and $v$ are vectors in $R^n$ and $c$ is a scalar then.
1. $A(u+v) = Au +Av$
2. $A(cu)=c(Au)$

# Theorem 7
An indexed set $S = \{v_{1}, ..., v_{n} \}$ of two or more vectors is linearly dependent if and only if at least one of the vectors in $S$ is a linear combination of the others. 
In fact, if $S$ is linearly dependent and $v_{1}\neq 0$ , then some $v_{j}$ (with $j > 1$) is a linear combination of the preceding vectors $v_{1},\dots,v_{j-1}$ 

# Theorem 8 
If a set contains more vectors than there are entries in each vector, then the set is linearly dependent. That is, any set $\{v_{1}, ..., v_p \}$ in $R^m$ is linearly dependent if $p > n$
# Theorem 9
If a set $\{v_{1},\dots,v_{p}\}$ in $R_{n}$ contains the zero vector, then the set is [[Linear Independence#Linear Dependence|linearly dependent]]
# Theorem  10

let $\large T:R^n\to R^m$ be a [[Transformation#Linear Transformation|linear transformation]]. Then there exists a unique [[Matrix]] $A$ such that
$$
T(x)=Ax
$$
For all $x \in R^n$

In fact, $A$ is the $m\times n$ matrix whose $jth$ column is the vector $T(e_j)$ where $e_{j}$ is the $jth$ column of the identity matrix in $R^n$
The matrix $A$ is called the **standard matrix for the linear transformation $T$**
# Theorem 13
The pivot columns of a matrix $A$ from a basis from the [[Column Space|column space]] of $A$
# Theorem 14
If a matrix $A$ has $n$ columns, then the [[Rank|rank]] of $A$ plus the [[Dimension|dimension]] of the [[Null Space|null space]] of $A$ is equal to n
$$
\large{rank(A)+dim(Null(A))=n}
$$
# Theorem 15
Also called the basis theorem
