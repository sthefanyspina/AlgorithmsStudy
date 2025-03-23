#The Rabin-Karp Algorithm is another efficient string matching algorithm, often used when multiple patterns need to be searched in a text. It’s based on hashing, where a hash value is computed for the pattern and then compared with the hash values of substrings in the text. If the hash values match, we do a direct comparison of the characters to ensure there’s no collision.

#Steps:
# 1 - Compute Hash of Pattern: Calculate the hash value of the pattern.
# 2 - Compute Hash for Substrings of Text: Slide a window of the size of the pattern across the text and compute hash values for each substring.
# 3 - Check for Match: If the hash of a substring in the text matches the hash of the pattern, perform a direct comparison to verify that it’s not a hash collision.
# 4 - Roll the Hash: When the window slides, adjust the hash value in constant time using a technique called rolling hash.

Rolling Hash:
#The rolling hash technique allows us to compute the hash for the next window in constant time, avoiding the need to recompute the hash for every substring from scratch.
#The hash function we use is typically:
#H(s)=(s0 ⋅b m−1 +s 1 ⋅b m−2 +⋯+s m−1​ ⋅b 0 )modp
#Where:
#𝑠0,𝑠1,…,𝑠𝑚−1 are the characters of the string, 
#b is a base value (a constant)
#p is a large prime number (to reduce collisions).

#Rabin-Karp Algorithm in Python

def rabin_karp(text, pattern):
    # Constants for the hashing
    d = 256  # Number of characters in the input alphabet (extended ASCII)
    q = 101  # A prime number to mod the hash (to reduce collisions)
    
    n = len(text)
    m = len(pattern)
    
    # Calculate the hash of the pattern and the first window of the text
    hash_pattern = 0
    hash_text = 0
    h = 1  # The value of d^(m-1) % q (used for rolling hash)
    
    # Calculate the initial hash values for the pattern and the first window of text
    for i in range(m-1):
        h = (h * d) % q
    
    for i in range(m):
        hash_pattern = (d * hash_pattern + ord(pattern[i])) % q
        hash_text = (d * hash_text + ord(text[i])) % q
    
    # Slide the pattern over the text
    for i in range(n - m + 1):
        # If the hashes match, do a character-by-character check
        if hash_pattern == hash_text:
            # Verify if the actual string matches (to avoid hash collisions)
            if text[i:i+m] == pattern:
                print(f"Pattern found at index {i}")
        
        # Roll the hash: remove the old character and add the new one
        if i < n - m:
            hash_text = (d * (hash_text - ord(text[i]) * h) + ord(text[i + m])) % q
            
            # If the hash becomes negative, adjust it
            if hash_text < 0:
                hash_text += q

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
rabin_karp(text, pattern)

#Explanation of the Code:
# 1 - Preprocessing the Pattern and Initial Text Window:
# 1.1 - The pattern and the first window of the text are hashed.
# 1.2 - We compute the hash values using a base d and a large prime q. This is done for both the pattern and the first substring of the text that matches the pattern's length.
# 2 - Rolling Hash:
# 2.1 - For each subsequent substring of the text, we update the hash by removing the contribution of the character that is sliding out of the window and adding the character that is sliding into the window.
# 2.2 - The rolling hash uses the formula:
# 2.3 - new hash=(d×(old hash−ord(text[i])×h)+ord(text[i+m]))modq
# 2.4 - h is calculated as 𝑑𝑚−1 modq and is used to subtract the old character's contribution.
# 3 - Direct Comparison:
# 3.1 - If the hash values of the pattern and the substring match, we do a direct comparison of the characters to avoid collisions, because different substrings could have the same hash value.

#Time Complexity:
# 1 - Hash Calculation: For the first window and the pattern, it's O(m), where m is the length of the pattern.
# 2 - Rolling Hash Updates: For each slide of the window, the hash is updated in constant time O(1). This gives a total of O(n), where n is the length of the text.
# 3 - Character Comparison: In the worst case (when hash values match often), the algorithm does character comparisons which take  O(m) time. Thus, the worst case time complexity is  O(n⋅m), but the expected time complexity is O(n+m).

#Space Complexity:
The space complexity is O(1) (excluding the space used by the text and pattern) since we only need a constant amount of space for the hash values.

#Example Output:
#For the text "ABABDABACDABABCABAB" and the pattern "ABABCABAB", the output will be:
#Pattern found at index 10

#Why Use Rabin-Karp?
#Multiple Pattern Search: One of the major advantages of Rabin-Karp is that it’s very efficient when searching for multiple patterns. You can hash all patterns and then compare their hashes against the text.
#Efficiency: It performs well on average, especially when hash collisions are rare, and it allows for quick substring searches in constant time when using the rolling hash technique.

#Limitations:
#Collisions: If two different substrings have the same hash value, the algorithm might produce false positives. Although this is rare if a good hash function is used, it still requires character-by-character comparison to verify the match.
