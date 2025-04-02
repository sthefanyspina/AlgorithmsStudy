#The Cocke-Younger-Kasami (CYK) Algorithm is a dynamic programming algorithm used to parse a string and determine whether it can be generated by a context-free grammar (CFG). It is particularly useful for grammars in Chomsky Normal Form (CNF), which is a simplified form of context-free grammar. The CYK algorithm works in bottom-up fashion to check if a given string can be derived from a given CFG.

#Steps to explain the CYK algorithm:
# 1 - Input:
# 1.1 - A string S of length n.
# 1.2 - A context-free grammar (CFG) in Chomsky Normal Form, i.e., a set of production rules where each production is of the form A → BC or A → a (where A, B, and C are non-terminals and a is a terminal).
# 2 - Output:
# 2.1 - A Boolean value indicating whether the string can be generated by the given CFG or not.
# 3 - Table Construction:
# 3.1 - Create a 2D table P of size n x n, where n is the length of the string. Each entry P[i][j] stores the set of non-terminals that can generate the substring of S from index i to j.
# 4 - Filling the Table:
# 4.1 - For each length of substring l from 1 to n, and for each starting point i, the algorithm looks at all possible ways to split the substring into two smaller substrings (i.e., divide the substring into two parts and check the production rules for each part).
# 4.2 - If a production rule matches, update the table entry.
# 5 - Final Check:
# 5.1 - At the end, check if the start symbol (usually S) is in the set P[0][n-1] (the entry corresponding to the entire string).

#Example:
#Consider a CFG in CNF:
#S → AB
#A → a
#B → b
#String to parse: "ab"

#Python Implementation of the CYK Algorithm:

def cyk_algorithm(grammar, string):
    n = len(string)
    # Initialize a table of n x n (since string has n characters)
    P = [[set() for _ in range(n)] for _ in range(n)]
    
    # Step 1: Populate the table for substrings of length 1
    for i in range(n):
        for lhs, rhs in grammar.items():
            if string[i] in rhs:
                P[i][i].add(lhs)

    # Step 2: Fill the table for substrings of length > 1
    for length in range(2, n + 1):  # length is the length of the substring
        for i in range(n - length + 1):  # i is the start index of the substring
            j = i + length - 1  # j is the end index of the substring
            # Check all possible splits of the substring
            for k in range(i, j):
                for lhs, rhs in grammar.items():
                    if len(rhs) == 2:  # Rule of form A → BC
                        B, C = rhs
                        if B in P[i][k] and C in P[k+1][j]:
                            P[i][j].add(lhs)
    
    # Step 3: Check if the start symbol is in the table entry for the entire string
    start_symbol = 'S'
    return start_symbol in P[0][n-1]


# Example Grammar in CNF
grammar = {
    'S': [('A', 'B')],
    'A': ['a'],
    'B': ['b']
}

# Example string
string = "ab"

# Running the CYK algorithm
result = cyk_algorithm(grammar, string)
print(f"The string '{string}' is {'accepted' if result else 'rejected'} by the grammar.")

#Explanation of Code:
# 1 - Grammar Representation:
# 1.1 - The grammar is represented as a dictionary, where the keys are non-terminal symbols, and the values are lists of production rules. For example, 'S': [('A', 'B')] means S → AB, and 'A': ['a'] means A → a.
# 2 - CYK Table:
# 2.1 - The table P is a 2D list where P[i][j] stores the set of non-terminal symbols that can derive the substring string[i:j+1].
# 3 - Base Case:
# 3.1 - The base case fills in P[i][i] with non-terminals that directly generate string[i] (i.e., those whose production is a terminal symbol).
# 4 - Recursive Case:
# 4.1 - The main loop fills in P[i][j] by considering all possible ways to split the substring string[i:j+1] and checking whether a production rule can be applied for each split.
# 5 - Final Check:
# 5.1 - The final check verifies whether the start symbol (in this case 'S') is present in P[0][n-1], indicating whether the entire string can be generated by the CFG.

#Example Execution:
#The string 'ab' is accepted by the grammar.
#This means the string "ab" can be derived from the given CFG.

#Time Complexity:
#The time complexity of the CYK algorithm is O(n^3), where n is the length of the string. This is due to the three nested loops:
# 1 - One for the length of substrings (n),
# 2 - One for the starting index (n),
# 3 - One for the splitting point (n).
#Thus, it is quite efficient for relatively small strings but can be slow for larger strings
