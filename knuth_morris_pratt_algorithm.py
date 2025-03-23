#The Knuth-Morris-Pratt (KMP) algorithm is an efficient string matching (or substring searching) algorithm that searches for a pattern within a text. It is more efficient than the naive approach, which may result in a time complexity of O(n×m), where n is the length of the text and m is the length of the pattern. The KMP algorithm improves this to O(n+m) time complexity.

#The Key Idea
#The idea behind KMP is to avoid re-examining characters in the text that have already been matched. When a mismatch occurs, instead of starting the search from the next character, the algorithm uses information from previously matched characters to "skip" ahead.

#Components of KMP Algorithm:
# 1 - Prefix Function (LPS array): The key to the KMP algorithm is the Longest Prefix which is also Suffix (LPS) array. This array helps to decide how many characters we can safely skip when a mismatch occurs.
# 1.1 - LPS[i] gives the length of the longest proper prefix of the substring pattern[0..i] which is also a suffix of this substring.
# 1.2 - The LPS array can be constructed in linear time O(m).
# 2 - Matching Process: Using the LPS array, the algorithm efficiently finds the pattern in the text. The idea is that when a mismatch occurs at position i in the pattern, instead of moving i back to 0, we can use LPS[i-1] to decide the next position to compare.

#Steps:
# 1 - Preprocess the pattern to create the LPS array.
# 2 - Search the pattern in the text using the LPS array.

#KMP Algorithm in Python

# Step 1: Build the LPS (Longest Prefix Suffix) array
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m  # LPS array
    length = 0  # length of the previous longest prefix suffix
    i = 1  # we start checking from the second character

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Try to find a smaller length
            else:
                lps[i] = 0
                i += 1

    return lps

# Step 2: Implement the KMP pattern search algorithm
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # Step 2a: Build the LPS array for the pattern
    lps = build_lps(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]  # Use LPS to skip ahead
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Use LPS to skip ahead
            else:
                i += 1  # Move to next character in text
    
    # If we reach here, the pattern is not found
    if j != m:
        print("Pattern not found in text.")

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)

#Explanation:
# 1 - build_lps(pattern):
# 1.1 - This function builds the LPS array (Longest Prefix Suffix). It starts by comparing the first character with the next. If they match, we increment the length and store it in the LPS array. If there’s a mismatch, we look back into the LPS array to find a smaller prefix to match.
# 2 - kmp_search(text, pattern):
# 2.1 - This function performs the actual search using the text and the pattern. It iterates through the text, and when a match is found, it checks the next character in the pattern using the LPS array to skip ahead when a mismatch occurs.

#Example Output:
#For the text "ABABDABACDABABCABAB" and pattern "ABABCABAB", the algorithm will output:
#Pattern found at index 10

#Time Complexity:
# 1 - Building the LPS array: O(m), where m is the length of the pattern.
# 2 - Searching the pattern in the text: O(n), where n is the length of the text.
# Thus, the total time complexity is O(n+m), which is significantly faster than the naive approach.

#Space Complexity:
#LPS array: O(m) for storing the longest prefix-suffix information.
