#Strassen's algorithm is an optimized method for matrix multiplication that reduces the time complexity compared to the standard matrix multiplication algorithm. The standard matrix multiplication algorithm has a time complexity of  O(n 3 ), while Strassen's algorithm improves it to O(n^log7)≈O(n^2.81 ). This improvement is achieved by reducing the number of recursive matrix multiplications.

#Strassen's Algorithm Steps:
# Given two matrices, A and B, both of size  n×n, Strassen's algorithm splits each matrix into four smaller submatrices.
# 1 - Split matrix A and B into four submatrices:


​
 
B 
22
​
 
​
 )
where each 
𝐴
𝑖
𝑗
A 
ij
​
  and 
𝐵
𝑖
𝑗
B 
ij
​
  are submatrices of size 
𝑛
/
2
×
𝑛
/
2
n/2×n/2.

Compute the following seven intermediate matrices using recursive multiplication and addition of the submatrices:

𝑀
1
=
(
𝐴
11
+
𝐴
22
)
⋅
(
𝐵
11
+
𝐵
22
)
M 
1
​
 =(A 
11
​
 +A 
22
​
 )⋅(B 
11
​
 +B 
22
​
 )
𝑀
2
=
(
𝐴
21
+
𝐴
22
)
⋅
𝐵
11
M 
2
​
 =(A 
21
​
 +A 
22
​
 )⋅B 
11
​
 
𝑀
3
=
𝐴
11
⋅
(
𝐵
12
−
𝐵
22
)
M 
3
​
 =A 
11
​
 ⋅(B 
12
​
 −B 
22
​
 )
𝑀
4
=
𝐴
22
⋅
(
𝐵
21
−
𝐵
11
)
M 
4
​
 =A 
22
​
 ⋅(B 
21
​
 −B 
11
​
 )
𝑀
5
=
(
𝐴
11
+
𝐴
12
)
⋅
𝐵
22
M 
5
​
 =(A 
11
​
 +A 
12
​
 )⋅B 
22
​
 
𝑀
6
=
(
𝐴
21
−
𝐴
11
)
⋅
(
𝐵
11
+
𝐵
12
)
M 
6
​
 =(A 
21
​
 −A 
11
​
 )⋅(B 
11
​
 +B 
12
​
 )
𝑀
7
=
(
𝐴
12
−
𝐴
22
)
⋅
(
𝐵
21
+
𝐵
22
)
M 
7
​
 =(A 
12
​
 −A 
22
​
 )⋅(B 
21
​
 +B 
22
​
 )
Compute the four quadrants of the result matrix 
𝐶
C using the following formulas:

𝐶
11
=
𝑀
1
+
𝑀
4
−
𝑀
5
+
𝑀
7
C 
11
​
 =M 
1
​
 +M 
4
​
 −M 
5
​
 +M 
7
​
 
𝐶
12
=
𝑀
3
+
𝑀
5
C 
12
​
 =M 
3
​
 +M 
5
​
 
𝐶
21
=
𝑀
2
+
𝑀
4
C 
21
​
 =M 
2
​
 +M 
4
​
 
𝐶
22
=
𝑀
1
+
𝑀
3
−
𝑀
2
+
𝑀
6
C 
22
​
 =M 
1
​
 +M 
3
​
 −M 
2
​
 +M 
6
​
 
Combine the four submatrices 
𝐶
11
,
𝐶
12
,
𝐶
21
,
𝐶
22
C 
11
​
 ,C 
12
​
 ,C 
21
​
 ,C 
22
​
  to form the final result matrix 
𝐶
C.

Python Code Implementation of Strassen's Algorithm
python
Copiar
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
Explanation:
Base Case: If the matrices are 
1
×
1
1×1, we directly return their product (since no recursion is needed).

Matrix Splitting: The matrices 
𝐴
A and 
𝐵
B are split into smaller submatrices. This splitting continues recursively until the base case is reached.

Recursive Computation: The seven intermediate matrices 
𝑀
1
M 
1
​
  to 
𝑀
7
M 
7
​
  are calculated recursively using smaller subproblems.

Combining Results: After calculating the seven products, the final result is obtained by combining these intermediate matrices into the final matrix 
𝐶
C.

Complexity:
Strassen's algorithm reduces the number of multiplications in matrix multiplication from 
8
8 (in the naive approach) to 
7
7 for each recursive step. This reduces the overall time complexity from 
𝑂
(
𝑛
3
)
O(n 
3
 ) to approximately 
𝑂
(
𝑛
2.81
)
O(n 
2.81
 ).
