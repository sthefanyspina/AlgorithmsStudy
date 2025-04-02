#Backtracking is a general algorithmic technique used for solving problems recursively, where the solution involves exploring all possible choices or paths and undoing (or "backtracking") when a choice leads to a solution that is not feasible. It's often used to solve problems where we need to explore all possible configurations and find a solution that satisfies the given constraints.
#In Python, backtracking typically involves a recursive function that builds a solution incrementally, step by step, and then retreats (backtracks) when it realizes that a partial solution doesn't lead to a valid full solution.

#Basic Concepts of Backtracking
# 1 - Recursive Search: At each step, you try a choice (e.g., place a number, move in a certain direction), and then recursively move to the next step.
# 2 - Pruning: If the current partial solution doesn’t meet the problem constraints, backtrack and try a different choice.
# 3 - Backtracking Step: Once a decision leads to a dead end or invalid state, you undo it and return to the previous decision point.

#Common Problems Solved with Backtracking:
# 1 - N-Queens Problem: Placing N queens on an N×N chessboard such that no two queens threaten each other.
# 2 - Sudoku Solver: Solving a Sudoku puzzle by filling in the grid with valid numbers.
# 3 - Permutations and Combinations: Generating all possible combinations or permutations of a set of elements.
# 4 - Subset Sum Problem: Finding a subset of numbers that adds up to a given sum.

#Steps in Backtracking:
# 1 - Place a queen at a valid position in the current row.
# 2 - Move to the next row and repeat the process.
# 3 - If you reach the last row, you've successfully placed all queens.
# 4 - If no valid position is found, backtrack by removing the last queen and trying the next possible position.

#Key Points About Backtracking:
# 1 - Exploration and Backtracking: You explore a decision space and undo decisions when they don’t lead to a solution.
# 2 - Recursive Nature: The solution typically involves recursion where each recursive call attempts to build a solution.
# 3 - Pruning: Some decisions are ruled out immediately if they don't lead to valid solutions, saving time and reducing unnecessary computations.
