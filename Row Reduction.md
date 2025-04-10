Any matrix can be row reduced (transformed by [[Elementary Row Operations]] into more than one matrix in [[Echelon Forms#Row echelon form|echelon form]]) The resultant matrix obtained depends on the specific [[Elementary Row Operations]] picked and are not unique

However the [[Echelon Forms#Reduced Row Echelon Form|reduced row echelon form]] matrix obtained for any matrix is unique. No mater what [[Elementary Row Operations|operations]] are chosen the result will be the same


![[Theorems#Theorem 1]]

# Definitions
- *Pivot position*: the positions in a matrix that contain the [[Echelon Forms#Leading Entry|leading entry]] of a [[Echelon Forms#Non-Zero row/column|non-zero row]] 
- *Pivot column* a column that contains a pivot position

# Gaussian Elimination
Is a methodical process that converts any [[Matrix]] into a [[Echelon Forms#Reduced Row Echelon Form|row reduced echelon]] matrix. It identifies [[Pivot]]

1. Locate the left-most [[Echelon Forms#Non-Zero row/column|non-zero column]]. This is your pivot column. Locate the top-most entry in the pivot column. This is your pivot position.
2. Use the operation $r_{i}\leftrightarrow r_{j}$ if necessary to move a non-zero entry into the pivot position.  
3. For each row $r_{i}$ below the pivot row, transform the entry in the pivot column to 0 using [[Elementary Row Operations]].  
4. If your matrix is in [[Echelon Forms#Row echelon form|Roe echelon form]], identify the bottom-most [[Echelon Forms#Non-Zero row/column|non-zero row]] and go to step 5. Otherwise, repeat steps 1-4 but choose your pivot column in step 1 from the submatrix obtained by eliminating all previous pivot rows.  
5. Find the [[Echelon Forms#Leading Entry|leading entry]] in this row. This is a pivot position. Use a [[Elementary Row Operations|row operation]] to transform the leading entry into a 1. Then use [[Elementary Row Operations|row operations]] to transform all entries above this leading 1 into a 0.  
6. If the matrix is in [[Echelon Forms#Reduced Row Echelon Form|Reduced Row Echelon form]], stop. Otherwise repeat step 5 for the next row up.