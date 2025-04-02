#Dynamic Programming (DP) is a technique used in computer science and mathematics to solve problems by breaking them down into smaller subproblems. The key idea is that the solution to the overall problem can be constructed from the solutions to its subproblems. This is particularly useful when the same subproblems are being solved multiple times, as it allows us to store their solutions and avoid redundant computations.

#Key Concepts of Dynamic Programming:
# 1 - Overlapping Subproblems: A problem has overlapping subproblems if the problem can be divided into subproblems that are reused multiple times. In such cases, solving the subproblem once and storing the result helps improve efficiency.
# 2 - Optimal Substructure: A problem exhibits optimal substructure if the solution to the problem can be derived from the solutions to its subproblems.

#Types of Dynamic Programming:
# 1 - Top-Down (Memoization): In this approach, you start solving the problem from the top (main problem) and recursively break it down into subproblems, storing their results to avoid redundant computations.
# 2 - Bottom-Up (Tabulation): This approach solves the problem starting from the smallest subproblems and iteratively builds up to the solution of the original problem. It doesn't use recursion and typically fills in a table (array).

#Dynamic Programming in Python:
#Let's look at an example of Dynamic Programming: the Fibonacci Sequence.

#Example: Fibonacci Sequence
#The Fibonacci sequence is defined as:
#F(0) = 0
#F(1) = 1
#F(n) = F(n-1) + F(n-2) for n > 1

#A naive recursive approach would recompute values multiple times. DP helps by storing previously computed values.

#Top-Down Approach (Memoization):

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Example usage
print(fib_memo(10))  # Output: 55

#Explanation: In the memoization approach, we use a dictionary memo to store the results of subproblems. Before solving a subproblem, we check if its result is already computed (cached). If so, we return it; otherwise, we compute it, store it, and return the result.

#Bottom-Up Approach (Tabulation):

def fib_tab(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

# Example usage
print(fib_tab(10))  # Output: 55

#Explanation: In the tabulation approach, we iteratively build up the solution. We create a table (list) where table[i] stores the value of F(i). We start with the base cases (F(0) and F(1)), then use a loop to compute values for larger n by using previously computed values in the table.

#General Approach to Solving DP Problems:
# 1 - Define the subproblems: Break down the problem into smaller subproblems.
# 2 - Identify the base cases: Determine the simple cases where you can directly return a result without further computation.
# 3 - Recurrence relation: Establish a relationship between the current problem and its subproblems.
# 4 - Memoization or Tabulation: Decide whether to use top-down (memoization) or bottom-up (tabulation) approach based on the problem.
# 5 - Solve the problem: Implement the solution based on the recurrence relation, either using recursion with memoization or iterative tabulation.

#Example 2: 0/1 Knapsack Problem
#Consider the 0/1 Knapsack Problem, where you are given a set of items, each with a weight and value, and a knapsack with a weight capacity. You need to find the maximum value you can fit into the knapsack without exceeding the weight capacity.

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))  # Output: 7

#Explanation: We define dp[i][w] as the maximum value obtainable with the first i items and a knapsack capacity of w. If the current item can fit in the knapsack (weights[i-1] <= w), we either include it or exclude it, and update the DP table accordingly.
