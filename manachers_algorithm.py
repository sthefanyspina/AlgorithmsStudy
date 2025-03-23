Manacher's Algorithm in Python
Manacher's Algorithm is an efficient algorithm to find the longest palindromic substring in linear time, i.e., O(n), where n is the length of the input string. It improves upon the naive approach, which could take O(n^2) time by considering every substring.

The basic idea behind Manacher’s algorithm is to use the concept of expanding around the center (similar to how we check for palindromes) but with some clever preprocessing and optimizations to reduce the time complexity.

Key Concepts of Manacher’s Algorithm
Palindrome Expansion: A palindrome is symmetric around its center. Given a string, you can expand outwards from any center (character or pair of characters) to check if it is a palindrome.

Preprocessing: Manacher's algorithm preprocesses the string by inserting a unique delimiter (such as #) between every character. This ensures that palindromes of both even and odd lengths can be handled uniformly. For example:

Input string: "abac"

Preprocessed string: "#a#b#a#c#"

Center and Right Boundary: The algorithm maintains two variables:

center: The center of the palindrome being considered.

right: The right boundary of the palindrome that expands the farthest to the right.

The idea is to expand palindromes only within this boundary to avoid unnecessary checks.

Mirroring: If a palindrome is found centered at some index, you can use symmetry to deduce the length of possible palindromes at other indices, minimizing redundant checks.

Steps of Manacher’s Algorithm
Preprocess the string: Insert delimiters (#) between characters and at the ends.

Use a helper array P[]: This array keeps track of the radius of the palindrome centered at each position.

Expand palindromes dynamically: For each position, use previously computed values to expand the palindrome as far as possible.

Manacher's Algorithm Implementation in Python
Here is an implementation of Manacher's Algorithm in Python:

python
Copiar
def manacher(s):
    # Step 1: Preprocess the string (add '#' between characters and at the ends)
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    P = [0] * n  # Array to store the length of the palindrome radius at each position
    center, right = 0, 0  # Initial values for the center and the right boundary

    # Step 2: Iterate through the string and calculate the palindromes
    for i in range(1, n - 1):
        # Step 2.1: Mirror the current position i
        mirror = 2 * center - i
        if i < right:
            P[i] = min(right - i, P[mirror])  # Use the previously computed palindrome radius

        # Step 2.2: Try to expand the palindrome around i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1

        # Step 2.3: Update center and right boundary
        if i + P[i] > right:
            center, right = i, i + P[i]

    # Step 3: Find the longest palindrome
    max_len, max_center = max((n, i) for i, n in enumerate(P))
    start = (max_center - max_len) // 2  # Calculate the starting index of the palindrome in the original string
    return s[start:start + max_len]

# Example Usage
s = "babad"
longest_palindrome = manacher(s)
print("Longest Palindromic Substring:", longest_palindrome)
Explanation of the Code:
Preprocessing: We insert a # between every character and at the ends of the string to handle even-length palindromes uniformly.

For example, "babad" becomes "#b#a#b#a#d#".

Main Loop:

We iterate over each character of the processed string t.

We use the P[] array to store the radius of the palindrome centered at each character. The length of the palindrome is stored in P[i].

If the current position i is within the right boundary (i.e., it’s part of a known palindrome), we use the previously computed palindrome radius to minimize the number of expansions.

Then we attempt to expand the palindrome centered at i by checking characters symmetrically around it.

Center and Right Boundary:

If the expanded palindrome exceeds the current right boundary, we update the center and right boundary to reflect the new palindrome's position.

Finding the Longest Palindrome: After processing, we find the maximum value in the P[] array to determine the longest palindrome's center and radius. We then calculate the starting index of the palindrome in the original string.

Time and Space Complexity:
Time Complexity: O(n), where n is the length of the string. This is because we process each character in the string exactly once, with constant time operations for each character.

Space Complexity: O(n), where n is the length of the preprocessed string (t). The array P[] stores the palindrome lengths for each character, and the string t is of length 2n + 1 (after preprocessing).

Example:
For the input string "babad", the output would be:

yaml
Copiar
Longest Palindromic Substring: bab
Summary:
Manacher’s Algorithm allows you to find the longest palindromic substring in linear time.

It uses preprocessing, center-expansion, and mirror symmetry to reduce the number of operations required compared to a brute-force approach.

It's especially useful when working with large strings or requiring efficient palindrome detection.
