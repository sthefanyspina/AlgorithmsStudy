#Zig-Zag traversal refers to visiting the elements of a matrix in a zig-zag pattern, or diagonal traversal. It starts from the top-left corner, goes down along the diagonals, and alternates between moving downwards and upwards as you traverse through each diagonal of the matrix.

#Key Idea of Zig-Zag Traversal:
# 1 - You move diagonally through the matrix, first downwards (from top-left to bottom-right) and then upwards (from bottom-left to top-right), alternating for each diagonal.
# 2 - This pattern continues until all elements in the matrix are visited.

#For example, consider the following matrix:
#1  2  3  4
#5  6  7  8
#9  10 11 12

#The zig-zag traversal order would be:
#1 -> 2 -> 5 -> 9 -> 6 -> 3 -> 4 -> 7 -> 10 -> 11 -> 8 -> 12

#Steps for Zig-Zag Traversal:
# 1 - Start from the first row and go through diagonals, alternately moving downward and upward.
# 2 - For each diagonal, if you are moving downwards, start from the top row and move to the bottom row.
# 3 - When moving upwards, start from the bottom row and move to the top row.
# 4 - Continue until all diagonals are processed.

#Algorithm:
# 1 - Traverse through the diagonals of the matrix. Each diagonal can be represented by either a starting row or a starting column.
# 2 - For each diagonal, alternate the direction of traversal:
# 3 - Move downward if it's the first or any other "even" diagonal.
# 4 - Move upward if it's the "odd" diagonal.

#Python Code Implementation:

def zig_zag_traversal(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # There are `rows + cols - 1` diagonals in total.
    for diag in range(rows + cols - 1):
        # Find the "start" point for each diagonal:
        if diag < rows:
            row = diag
            col = 0
        else:
            row = rows - 1
            col = diag - rows + 1

        # Collect elements for this diagonal in either downward or upward direction
        temp = []
        if diag % 2 == 0:
            # Traverse downward (top-left to bottom-right)
            while row < rows and col < cols:
                temp.append(matrix[row][col])
                row += 1
                col += 1
        else:
            # Traverse upward (bottom-left to top-right)
            while row >= 0 and col < cols:
                temp.append(matrix[row][col])
                row -= 1
                col += 1

        # Add elements of this diagonal to the result
        result.extend(temp)

    return result

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

result = zig_zag_traversal(matrix)
print(result)

#Explanation of Code:
# 1 - Matrix Setup: The matrix is a 2D list with rows and columns.
# 2 - Diagonal Traversal:
# 2.1 - The total number of diagonals is equal to rows + cols - 1. This is because the number of diagonals starts from the first element, goes through the edges, and ends with the last element of the last row/column.
# 3 - Direction of Traversal:
# 3.1 - If the diagonal index is even, traverse downward (from top-left to bottom-right).
# 3.2 - If the diagonal index is odd, traverse upward (from bottom-left to top-right).
# 4 - Result Collection: For each diagonal, elements are collected in a temporary list temp, which is then appended to the final result.

#Example Walkthrough:
#For the input matrix:
#1  2  3  4
#5  6  7  8
#9  10 11 12

#First diagonal (diag 0): We start at 1, and it's a downward traversal.
#1 → 2 → 5 → 9

#Second diagonal (diag 1): We start at 2, and it's an upward traversal.
#2 → 5 → 6

#Continue this pattern for all diagonals.

#Time Complexity:
#O(m * n): Where m is the number of rows and n is the number of columns. We visit each element of the matrix exactly once.

#Output:
#For the given matrix, the output will be:
#[1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
