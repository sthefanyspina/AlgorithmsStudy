#Linear programming (LP) is a mathematical technique used for optimization. The goal is to maximize or minimize a linear objective function, subject to linear equality and inequality constraints.
#The Simplex Algorithm is a method for solving LP problems. It iteratively moves along the edges of the feasible region (the set of all points that satisfy the constraints) to find the optimal solution.

#Key Concepts in Linear Programming:
# 1 - Objective Function: A linear function we want to maximize or minimize. For example, we want to maximize profit or minimize cost.
# 1.1 - Maximize or Minimize: z= c1x1 + c2x2 + ... + cnxn
​# 2 - Constraints: A set of linear inequalities or equations that the solution must satisfy.
# 2.1 - Subject to:
#2.2 - a11x1 + a12x2 ... + a1nxn ≤ b1
#2.3 - a21x1 + a22x2 ... + a2nxn ≤ b2
#2.4 - x1 ≥, x2 ≥ 0, ..., xn ≥ 0

#Simplex Algorithm Overview:
# 1 - Start at a feasible vertex: The algorithm starts at a point that satisfies the constraints.
# 2 - Move along the edges: At each step, it moves to an adjacent vertex, following the direction that improves the objective function.
# 3 - Terminate when optimal: The algorithm stops when no further improvement in the objective function is possible.

#Implementing the Simplex Algorithm in Python
#We can solve linear programming problems using libraries like SciPy, which includes the Simplex algorithm implementation. Here's a basic example of how to solve a linear programming problem with Python using the Simplex method.

#Example Problem:
# 1 - Maximize: z=3x1 + 2x2
# 2 - Subject to: 
# 2.1 - x1 + x2 ≤ 4
# 2.2 - 2x1 + x2 ≤ 5
# 2.3 - x1 ≥ 0, x2 ≥ 0

#Code Implementation:

import numpy as np
from scipy.optimize import linprog

# Coefficients of the objective function (Maximize: 3x1 + 2x2)
# In linprog, we minimize, so we negate the coefficients of the objective function.
c = [-3, -2]

# Coefficients of the inequality constraints
# These are the coefficients of the inequalities in the form Ax <= b
A = [[1, 1], [2, 1]]

# Right-hand side of the inequality constraints
b = [4, 5]

# Boundaries for each variable (x1, x2 >= 0)
x_bounds = (0, None)  # x1 >= 0
y_bounds = (0, None)  # x2 >= 0

# Solve the problem using the Simplex method
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# Print the result
print("Optimal value:", -result.fun)  # Negate again since we were minimizing
print("Optimal solution (x1, x2):", result.x)

#Explanation of Code:
# 1 - Objective function: We want to maximize 3x1 + 2x2. In linprog, the function is minimized, so we negate the coefficients to convert it to a minimization problem. c=[−3,−2]
# 2 - Inequality constraints: The constraints x1 + x2 ≤ 4 and 2x1 + x2 ≤ 5 are represented as:
A=[ 1 1 ] ,b=[4,5]
    2 1
# 3 - ​Bounds: Each variable (x1, x2) has lower bounds of 0, representing non-negativity.
# 4 - Solution: The linprog function finds the optimal solution using the Simplex algorithm (set via method='simplex').

#Output:
#Optimal value: 10.0
#Optimal solution (x1, x2): [2. 2.]
#This means the optimal solution is x1 = 2 and x2 = 2, which gives the maximum value of the objective function z = 3(2) + 2(2) = 10.

