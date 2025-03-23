#A Suffix Tree is a compressed trie (or prefix tree) that represents all the suffixes of a given string. It is a powerful data structure used for solving a wide range of problems on strings, such as pattern matching, finding repeated substrings, and longest common substring problems. The main idea behind a Suffix Tree is to create a tree where each path from the root to a leaf represents a suffix of the input string.

#Key Properties of Suffix Trees:
# 1 -String Representation: A suffix tree for a string S contains all the suffixes of S as its paths.
# 2 - Efficient Operations: Operations like searching for a substring, finding the longest repeated substring, or checking if a string is a suffix can be done in O(m) time, where m is the length of the pattern being searched, making it very efficient.
# 3 - Compact Representation: While the naive construction of a suffix tree takes O(n^2) time, efficient algorithms such as Ukkonen's algorithm can build the tree in O(n) time.

#Suffix Tree Construction (Naive Version)
#The naive way to construct a suffix tree is as follows:
# 1 - For each suffix of the string, insert it into a trie.
# 2 - For each new suffix, iterate through all its characters and add nodes accordingly.
#However, this approach is inefficient. The more efficient algorithm to build a suffix tree is Ukkonen's Algorithm, which constructs the tree in O(n) time.

#Python Code for Naive Suffix Tree

class SuffixTree:
    def __init__(self, string):
        self.string = string
        self.tree = {}
        self.build_tree()

    def build_tree(self):
        """Build a Naive Suffix Tree"""
        n = len(self.string)
        for i in range(n):
            suffix = self.string[i:]
            self._insert_suffix(suffix, i)

    def _insert_suffix(self, suffix, index):
        """Insert a suffix into the tree"""
        current_node = self.tree
        for i, char in enumerate(suffix):
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
            # Store the index where the suffix starts
            if i == len(suffix) - 1:
                current_node['$'] = index  # '$' marks the end of a string

    def search(self, pattern):
        """Search for a pattern in the suffix tree"""
        current_node = self.tree
        for char in pattern:
            if char not in current_node:
                return False
            current_node = current_node[char]
        return True

    def display(self):
        """Display the suffix tree"""
        def print_tree(node, level=0):
            for key, value in node.items():
                if key == '$':
                    print("  " * level + key + ": " + str(value))
                else:
                    print("  " * level + key)
                    print_tree(value, level + 1)

        print_tree(self.tree)

# Example usage
string = "banana"
suffix_tree = SuffixTree(string)

print("Suffix Tree for 'banana':")
suffix_tree.display()

pattern = "ana"
print(f"Search for '{pattern}':", suffix_tree.search(pattern))

#Explanation of the Code:
# 1 - SuffixTree Class:
# 1.1 - The SuffixTree class is initialized with a string and constructs a naive suffix tree.
# 1.2 - The build_tree method generates all the suffixes of the string and inserts them into the tree using the _insert_suffix method.
# 1.3 - The _insert_suffix method adds each character of the suffix to the tree. A node is created for each character, and when we reach the end of the suffix, we mark the end with '$' and store the index.
# 2 - Search Method:
# 2.1 - The search method looks for a given pattern in the tree. It traverses through the tree based on the characters in the pattern.
# 2.2 - If the pattern exists, the method returns True; otherwise, it returns False.
# 3 - Display Method:
# 3.1 - The display method prints the tree structure. It recursively prints each level of the tree to visualize the suffix tree.

#Example Output:
#For the string "banana", the suffix tree will look like this:
#Suffix Tree for 'banana':
b
  a
    n
      a
        n
          a
            $
  a
    n
      a
        n
          a
            $
  n
    a
      n
        a
          $
  a
    n
      a
        $
  n
    a
      $

#Searching for a Pattern:
#If you search for the pattern "ana", the output will be:
Search for 'ana': True

#Time Complexity:
# 1 - The time complexity for constructing the suffix tree with the naive approach is O(n^2), where n is the length of the string. This is because each suffix has to be inserted individually, and inserting a string of length k takes O(k) time.
# 2 - Searching for a pattern takes O(m) time, where m is the length of the pattern being searched.

#Space Complexity:
#The space complexity of this naive implementation is O(n^2) because in the worst case, the tree can have up to n^2 nodes (one for each substring of the string).

#Efficient Suffix Tree Construction (Ukkonen's Algorithm):
#For efficient construction, Ukkonen’s algorithm can build a suffix tree in O(n) time. Implementing this algorithm is quite complex, but it's far more efficient for large strings. This algorithm builds the tree incrementally, handling each suffix in constant time after preprocessing.

#Applications of Suffix Trees:
# 1 - Pattern Matching: Efficiently search for substrings in linear time.
# 2 - Longest Repeated Substring: Find the longest substring that repeats in the string.
# 3 - Longest Common Substring: Find the longest substring that two strings have in common.
# 4 - Substring Counting: Count the number of occurrences of a substring in the string.
