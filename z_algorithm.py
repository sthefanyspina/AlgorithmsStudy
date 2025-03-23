The Z Algorithm is an efficient string matching algorithm that computes an array called the Z-array (or Z-function) for a given string. The Z-array of a string is an array where the 
𝑖
𝑡
ℎ
i 
th
  element represents the length of the longest substring starting from the 
𝑖
𝑡
ℎ
i 
th
  position of the string that is also a prefix of the string.

Key Concepts:
For a given string S of length n, the Z-array is an array Z[] of length n where Z[i] represents the length of the longest substring starting at index i that matches the prefix of the string S.

For example, for the string S = "abacaba", the Z-array would be:

ini
Copiar
S = "abacaba"
Z = [7, 0, 1, 0, 3, 0, 1]
Here:

Z[0] = 7 because the entire string is a prefix of itself.

Z[1] = 0 because there's no substring starting at index 1 that matches the prefix.

Z[2] = 1 because the substring "a" starting at index 2 matches the prefix "a" of the string.

And so on.

Applications of the Z Algorithm:
Pattern Matching: The Z algorithm is used to find occurrences of a pattern within a text by combining the pattern with the text and using the Z-array to find matching sections.

String Matching Problems: It is often used for tasks like finding all occurrences of a pattern in a string in linear time.

Z Algorithm – Steps:
Compute the Z-array for a given string.

For each position i in the string, the Z-value gives the length of the longest substring starting at i that matches the prefix of the string.

Time Complexity:
The Z algorithm runs in O(n) time, where 
𝑛
n is the length of the string, making it highly efficient for large strings.

Python Code Implementation of the Z Algorithm:
python
Copiar
def Z_function(S):
    n = len(S)
    Z = [0] * n  # Initialize Z-array with zeros
    left, right = 0, 0  # These represent the range of the current Z-box
    
    for i in range(1, n):
        if i <= right:
            # Case 1: Inside the Z-box, use previously computed Z-values
            Z[i] = min(right - i + 1, Z[i - left])
        
        # Case 2: Expand the Z-box
        while i + Z[i] < n and S[Z[i]] == S[i + Z[i]]:
            Z[i] += 1
        
        # Update the Z-box if we found a larger Z-box
        if i + Z[i] - 1 > right:
            left, right = i, i + Z[i] - 1
    
    Z[0] = n  # The entire string is a prefix of itself
    return Z

# Example usage
S = "abacaba"
Z = Z_function(S)
print("Z-array:", Z)
Explanation of the Code:
Initialization: We initialize a list Z of length n (where n is the length of the string) to store the Z-values. We also use two variables left and right to keep track of the rightmost interval (or Z-box) that we've found where the substring matches the prefix of the string.

Z-box Expansion:

For each index i from 1 to n-1, we check if i lies inside the current Z-box (i.e., if i <= right). If so, we try to use the previously computed Z-value (Z[i - left]) to speed up the calculation.

Then, we attempt to expand the Z-box from position i by checking if the characters at the corresponding positions match the prefix.

Z-box Update: After expanding the Z-box, if the new Z-box extends beyond the current right boundary, we update left and right to the new bounds of the Z-box.

Set Z[0]: We explicitly set Z[0] = n because the entire string is a prefix of itself.

Example:
For the string S = "abacaba", the Z-array would be calculated as follows:

Initial values: S = "abacaba", Z = [0, 0, 0, 0, 0, 0, 0]

Step-by-step calculation:

Z[0] = 7 because the entire string matches itself.

Z[1] = 0 because there's no match starting at index 1.

Z[2] = 1 because the substring "a" matches the prefix.

Z[3] = 0 because there's no match starting at index 3.

Z[4] = 3 because the substring "aba" matches the prefix.

Z[5] = 0 because there's no match starting at index 5.

Z[6] = 1 because the substring "a" matches the prefix.

Thus, the Z-array for "abacaba" is:

ini
Copiar
Z = [7, 0, 1, 0, 3, 0, 1]
Time Complexity:
The Z algorithm runs in O(n) time, where 
𝑛
n is the length of the string. This is because we only perform each step (expanding the Z-box or checking the next character) a constant number of times.

Space Complexity:
The space complexity is O(n) due to the storage of the Z-array.

Applications:
Pattern matching: To find all occurrences of a pattern in a text by combining the pattern and text and using the Z-array.

String matching: Solving problems like finding the longest common prefix in a string, substring matching, etc.
