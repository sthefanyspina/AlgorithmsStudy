#The N-Queens problem is a classic problem in computer science and artificial intelligence. It asks you to place N queens on an N x N chessboard in such a way that no two queens threaten each other. In chess, a queen can attack another queen if they share the same row, column, or diagonal.

#The Problem:
# 1 - Place N queens on an N x N chessboard such that no two queens can attack each other.
# 2 - You need to find all the possible ways to place the queens.

#Constraints:
# 1 - No two queens can share the same row.
# 2 - No two queens can share the same column.
# 3 - No two queens can share the same diagonal.

#Solution Explanation:
#This problem can be solved using Backtracking, a general algorithm for finding all (or some) solutions to computational problems, particularly constraint satisfaction problems like N-Queens.

#Backtracking Approach:
# 1 - We place queens one by one in each row.
# 2 - For each row, try placing a queen in each column (but ensure it doesn't conflict with any previously placed queens).
# 3 - If placing a queen in a column of the current row doesn't cause any conflicts, we move to the next row.
# 4 - If a conflict arises, we backtrack and move the queen in the previous row to a new position.

#Key Considerations:
# 1 - Rows: Each queen must be placed in a distinct row.
# 2 - Columns: Each queen must be placed in a distinct column.
# 3 - Diagonals: The key part of the algorithm is checking if the queen on the current row and column doesn't share the same diagonal with previously placed queens. There are two types of diagonals:
# 3.1 - "main" diagonal: Difference between row and column (row - col).
# 3.2 - "anti" diagonal: Sum of row and column (row + col).
#We need to keep track of these diagonal constraints to ensure no two queens are placed on the same diagonal.

#Python Implementation:

def solveNQueens(n):
    # To store the solution
    solutions = []
    
    # Helper function to check if it's safe to place a queen
    def isSafe(row, col, cols, diag1, diag2):
        # Check if the column or diagonals are already occupied
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False
        return True
    
    # Backtracking function to find all solutions
    def backtrack(row, n, cols, diag1, diag2, board):
        # If we have placed queens in all rows, add the current board to solutions
        if row == n:
            solutions.append(["".join(row) for row in board])
            return
        
        # Try placing a queen in each column
        for col in range(n):
            if isSafe(row, col, cols, diag1, diag2):
                # Mark the current position as occupied
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Place the queen
                board[row][col] = 'Q'
                
                # Move to the next row
                backtrack(row + 1, n, cols, diag1, diag2, board)
                
                # Backtrack, remove the queen
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

    # Initial board setup (all positions are empty)
    board = [['.' for _ in range(n)] for _ in range(n)]
    # Sets to keep track of columns and diagonals that are under attack
    cols = set()
    diag1 = set()
    diag2 = set()
    
    # Start backtracking from the first row
    backtrack(0, n, cols, diag1, diag2, board)
    
    return solutions

# Example Usage
n = 4
result = solveNQueens(n)
for solution in result:
    for row in solution:
        print(row)
    print()

#Explanation of the Code:
# 1 - Helper function isSafe(row, col, cols, diag1, diag2):
# 1.1 - Checks whether it's safe to place a queen at position (row, col).
# 1.2 - It ensures that no queen has already been placed in the same column or on the same diagonal (both main and anti-diagonal).
# 2 - Backtracking function backtrack(row, n, cols, diag1, diag2, board):
# 2.1 - This function attempts to place queens row by row.
# 2.2 - For each row, it tries placing the queen in each column and checks whether it's safe using the isSafe function.
# 2.3 - If it's safe, it places the queen and recursively tries to place queens in subsequent rows.
# 2.4 - If the entire board is successfully filled, the solution is added to the solutions list.
# 2.5 - The function backtracks by removing the queen and trying the next possible position.
# 3 - Base Case:
# 3.1 - If all rows have been filled, the current arrangement of queens is a valid solution, and it is added to the solutions list.
# 4 - Result:
# 4.1 - The function returns a list of all valid solutions, where each solution is represented as a list of strings (each string represents a row of the chessboard).

#Example:
#For n = 4, the possible solutions would be:
. Q . .
. . . Q
Q . . .
. . Q .
and

. . Q .
Q . . .
. . . Q
. Q . .
#Each solution is a valid arrangement where no two queens threaten each other.

#Time Complexity:
#The time complexity of the backtracking approach is O(N!), where N is the size of the board. This is because, in the worst case, the algorithm needs to try all possible placements for the queens, and there are N rows and N columns to explore. However, the backtracking approach eliminates many invalid placements early, so the actual number of operations is much smaller in practice.
