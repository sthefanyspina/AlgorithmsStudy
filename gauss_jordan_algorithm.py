#The Gauss-Jordan elimination algorithm is a method used to solve systems of linear equations. It transforms a given system of linear equations (represented by an augmented matrix) into reduced row echelon form (RREF). The algorithm consists of a sequence of row operations to make the matrix as simple as possible, ultimately solving the system.
#The main steps of the Gauss-Jordan algorithm are as follows:
# 1 - Forward Elimination: Convert the matrix into an upper triangular form.
# 2 - Backward Substitution: Further reduce the matrix to achieve the reduced row echelon form (RREF), where each leading entry in a row is 1, and all elements in the column containing the leading entry are 0.
#In Python, you can implement the Gauss-Jordan algorithm using basic matrix operations. Here's how it works:

#Code Implementation of Gauss-Jordan Algorithm in Python:

import numpy as np

def gauss_jordan(A, b):
    # Combine A and b into an augmented matrix
    augmented_matrix = np.hstack([A, b.reshape(-1, 1)])

    # Get the number of rows
    rows = augmented_matrix.shape[0]
    
    # Perform Gauss-Jordan elimination
    for i in range(rows):
        # Make the diagonal element 1 by dividing the whole row by the diagonal element
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        
        # Eliminate the column elements above and below the pivot (making them 0)
        for j in range(rows):
            if i != j:
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]
    
    # The last column of the augmented matrix contains the solutions
    return augmented_matrix[:, -1]

# Example usage:
A = np.array([[2, 1, -1], 
              [-3, -1, 2], 
              [-2, 1, 2]], dtype=float)

b = np.array([8, -11, -3], dtype=float)

solution = gauss_jordan(A, b)
print("Solution:", solution)

#Explanation of the Code:
# 1 - Input:
# 1.1 - A is the coefficient matrix.
# 1.2 - b is the constant vector (the right-hand side of the system of equations).
# 2 - Augmented Matrix: The coefficient matrix A and the constant vector b are combined into an augmented matrix, where A is augmented with b as the last column.
# 3 - Elimination Process:
# 3.1 - For each row, the pivot element (diagonal element) is normalized to 1 by dividing the entire row by the pivot element.
# 3.2 - Then, all other elements in the column are eliminated by subtracting multiples of the row from other rows.
# 4 - Final Solution: After performing all operations, the augmented matrix will be in reduced row echelon form, and the last column will contain the solution to the system.

#Example:
#For the system of equations:
#2x+y−z=8
#−3x−y+2z=−11
#−2x+y+2z=−3

#The solution will be output as:
#Solution: [ 2.  3. -1.]
#This means x=2, y=3, and z=−1.

#Notes:
#The matrix A must be square (i.e., it should have the same number of equations and unknowns).
#The matrix must be invertible (i.e., it should not be singular, meaning the determinant of the matrix must be non-zero).
