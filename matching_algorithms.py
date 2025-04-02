#Matching algorithms in Python refer to techniques used to find correspondences or patterns between data, whether it's strings, numbers, or other types of information. These algorithms can be useful in a variety of fields like text processing, machine learning, and data science. Here’s an overview of common matching algorithms used in Python, and how they work:

#1. String Matching Algorithms
#These algorithms are primarily used to find occurrences of a pattern (substring) within a text (string).
# 1 - Naive String Matching The simplest approach to string matching is the naive method, which checks for a match by sliding the pattern across the text and checking character by character.
#Example:

def naive_match(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            print(f"Pattern found at index {i}")

text = "ABABAACAABABABA"
pattern = "ABA"
naive_match(text, pattern)

# 2 - Knuth-Morris-Pratt (KMP) Algorithm KMP improves upon the naive approach by avoiding redundant checks. It preprocesses the pattern to create a partial match table, which helps skip ahead when a mismatch is found.

#Example:

def KMP_search(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m  # Longest Prefix Suffix (LPS) array
    j = 0  # index for pattern

    # Preprocess the pattern to create the LPS array
    def compute_lps_array():
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    i += 1

    compute_lps_array()
    
    # Search phase
    i = 0  # index for text
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

text = "ABABAACAABABABA"
pattern = "ABA"
KMP_search(text, pattern)

# 3 - Rabin-Karp Algorithm This is a hashing-based algorithm that computes a hash value for the pattern and the substrings of the text, and then compares the hash values to find matches.
#Example:

def rabin_karp_search(text, pattern):
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number
    m, n = len(pattern), len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1

    # Calculate the value of h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the initial hash values of pattern and first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # Slide the pattern over the text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")
        
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:
                text_hash += q

text = "ABABAACAABABABA"
pattern = "ABA"
rabin_karp_search(text, pattern)

#2. Graph Matching Algorithms
#These algorithms are used to find correspondences between nodes or subgraphs, commonly used in computer networks, social networks, etc.

#2.1 - Graph Isomorphism This problem involves checking if two graphs are identical, or finding a mapping between their nodes.

import networkx as nx
G1 = nx.Graph()
G2 = nx.Graph()

# Add edges to both graphs
G1.add_edges_from([(1, 2), (2, 3), (3, 4)])
G2.add_edges_from([(4, 3), (3, 2), (2, 1)])

# Check if the graphs are isomorphic
isomorphic = nx.is_isomorphic(G1, G2)
print(f"Graphs are isomorphic: {isomorphic}")

#3. Set Matching Algorithms
#These are often used for matching items based on sets or collections of data, like comparing elements of two lists.
# 3.1 - Set Intersection and Difference Python’s set operations (intersection(), difference(), symmetric_difference()) are used to find matches or differences between two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection = set1.intersection(set2)
print(f"Intersection: {intersection}")

difference = set1.difference(set2)
print(f"Difference: {difference}")

#4. Fuzzy Matching Algorithms
#These algorithms are useful for finding matches that are close but not exactly the same, typically used in applications like spell-checking or text similarity.
# 4.1 - FuzzyWuzzy fuzzywuzzy is a Python library for string matching using Levenshtein Distance. It helps find how similar two strings are.

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

string1 = "hello world"
string2 = "helo world"

# Compare strings
ratio = fuzz.ratio(string1, string2)
print(f"Similarity: {ratio}%")

#You can also match a string to a list of options using process.extractOne() or process.extract().
choices = ["hello", "hell", "hallo", "helloo"]
best_match = process.extractOne("helo", choices)
print(best_match)
