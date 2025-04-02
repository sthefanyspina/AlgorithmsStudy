#Strassen's algorithm is an optimized method for matrix multiplication that reduces the time complexity compared to the standard matrix multiplication algorithm. The standard matrix multiplication algorithm has a time complexity of  O(n 3 ), while Strassen's algorithm improves it to O(n^log7)≈O(n^2.81 ). This improvement is achieved by reducing the number of recursive matrix multiplications.

#Strassen's Algorithm Steps:
# Given two matrices, A and B, both of size  n×n, Strassen's algorithm splits each matrix into four smaller submatrices.
# 1 - Split matrix A and B into four submatrices:
A = (A11   A12), B = (B11  B12)
     A21   A22        B21  B22
#where each Aij and Bij are submatrices of size n/2×n/2.

# 2 - Compute the following seven intermediate matrices using recursive multiplication and addition of the submatrices:
M1 = (A11 + A22) * (B11 + B22)
M2 = (A21 + A22) * B11
M3 = A11 * (B12 - B22)
M4 = A22 * (B21 - B11)
M5 = (A11 + A12) * B22
M6 = (A21 - A11) * (B11 + B12)
M7 = (A12 - A22) * (B21 + B22)

# 3 - Compute the four quadrants of the result matrix C using the following formulas:
C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 + M3 - M2 + M6

# 4 - Combine the four submatrices C11, C12, C21, C22 to form the final result matrix C.

#Python Code Implementation of Strassen's Algorithm

import numpy as np

def strassen(A, B):
    # Base case: if the matrix is 1x1, return the product
    if A.shape[0] == 1:
        return A * B

    # Split matrices into quarters
    mid = A.shape[0] // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Calculate M1 to M7
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Calculate C11, C12, C21, C22
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6

    # Combine the four quadrants into a single matrix
    C = np.zeros((A.shape[0], B.shape[1]))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

# Example usage:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = strassen(A, B)
print("Resultant Matrix C:")
print(C)

#Explanation:
# 1 - Base Case: If the matrices are 1×1, we directly return their product (since no recursion is needed).
# 2 - Matrix Splitting: The matrices A and B are split into smaller submatrices. This splitting continues recursively until the base case is reached.
# 3 - Recursive Computation: The seven intermediate matrices M1 to M7 are calculated recursively using smaller subproblems.
# Combining Results: After calculating the seven products, the final result is obtained by combining these intermediate matrices into the final matrix C.

#Complexity:
#Strassen's algorithm reduces the number of multiplications in matrix multiplication from 8 (in the naive approach) to  7 for each recursive step. This reduces the overall time complexity from O(n^3) to approximately O(n^2.81).
