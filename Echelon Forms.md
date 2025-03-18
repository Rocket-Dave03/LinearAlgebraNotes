## Definitions
#### Non-Zero row/column
A *non-zero* row of a column in a matrix means a row or column that contains at least one non-zero entry.
#### Leading Entry
A *leading entry* of a row refers to the leftmost non-zero entry in a non-zero row.
# Row echelon form
A matrix is in row echelon form (or just echelon form) if
1. Each [[Echelon Forms#Non-Zero row/column|Non-zero row]] lies above every zero row (ie. if any zero rows are present they are at the bottom)
2. The [[Echelon Forms#Leading Entry|leading entry]] of a [[Echelon Forms#Non-Zero row/column|non-zero row]] lies in a column to the right of the column contain the leading entry of any preceding row (ie. leading entries are down and to the right of previous leading entries)
3. If a column contains the [[Echelon Forms#Leading Entry|leading entry]] of some row, then all entries of that column below the leading entry are $0$ (entries above may or may-not be zero)

# Reduced Row Echelon Form
A matrix is in reduce row echelon form if:
1. It is in [[Echelon Forms#Row echelon form|row echelon form]]
2. The [[Echelon Forms#Leading Entry|leading entry]] of each [[Echelon Forms#Non-Zero row/column|non-zero row]] is 1
3. If a column contains the [[Echelon Forms#Leading Entry|leading entry]] of some row, then all the other entries of that column are 0