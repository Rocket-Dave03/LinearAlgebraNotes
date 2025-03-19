# Determinant of 2x2 Matrix

If $A=\begin{bmatrix}a & b \\ c & d\end{bmatrix}$ 
the $ad-bc$ is the determinant denoted $\det(A)$

# Determinants of Larger Matrices

### Cofactor Expansion
##### Definitions
- For any $n\times n$ matrix $A$, the submatrix formed by deleting the $i$-th row and the $j$-th column is termed $A_{i,j}$
- For any $n\times n$ matrix $A$, $(i,j)$-cofactor of $A$ is neoted $C_{i,j}$ and is calculated $\large{C_{i,j}=(-1)^{i+j}\det(A_{i,j})}$
#### Determinant
For any $n\times n$ matrix $A$, the determinant is given by the cofactor expansion along the first row:
$$
\Large
\det(A)=a_{1,1}C_{1,1}+a_{1,2}C_{1,2}+\dots+a_{1,n}C_{1,n}
$$
where 
$$
\Large
\begin{align}
a_{i,j}=\text{component of matrix at row i, col j} \\
\end{align}
$$