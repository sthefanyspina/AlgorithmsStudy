#A Prefix Tree, also known as a Trie, is a tree-like data structure that stores a set of strings in a way that allows efficient retrieval of strings, particularly when you want to perform operations like prefix matching, autocomplete, or searching for words with common prefixes.

#Key Concepts:
# 1 - Nodes: Each node in the tree represents a single character of a string.
# 2 - Root Node: The root of the tree doesn’t represent any character but serves as the starting point.
# 3 - Edges: Each edge connects two nodes and corresponds to a character in the strings being stored.
# 4 - Words/Keys: The leaf nodes (or any node marked with a specific flag) can represent the end of a word.

#Why is it Useful?
# 1 - Efficient Prefix Searching: Tries are very efficient for operations like searching for words with a common prefix (e.g., autocomplete).
# 2 - Memory-Efficient for Storing Common Prefixes: Words that share common prefixes don’t need to be stored completely multiple times, reducing memory usage.

#Trie Structure:
# 1 - Each node contains:
# 1.1 - A dictionary or list to store child nodes.
# 1.2 - A boolean is_end_of_word flag to mark if a node is the end of a valid word.
# 2 - Operations on Trie:
# 2.1 - Insert: Insert a word into the trie.
# 2.2 - Search: Search if a word exists in the trie.
# 2.3 - StartsWith: Check if there exists any word in the trie that starts with a given prefix.

Trie Implementation in Python:

#1. Define the Node Class
#Each node will store a dictionary for its children and a boolean flag to mark whether it is the end of a word.
class TrieNode:
    def __init__(self):
        self.children = {}  # Maps character to TrieNode
        self.is_end_of_word = False

#2. Define the Trie Class
#The Trie class will handle insertions, searches, and checking for prefixes.
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node is an empty node

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node if the character doesn't exist
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    # Search for a word in the Trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Word does not exist
            node = node.children[char]
        return node.is_end_of_word  # True if it's a complete word, False if it's a prefix

    # Check if there is any word in the Trie that starts with the given prefix
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # No word starts with the given prefix
            node = node.children[char]
        return True  # The prefix exists in the Trie

#3. Example Usage
# Create a Trie object
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")

# Search for a word in the Trie
print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.search("bat"))    # True
print(trie.search("ball"))   # True
print(trie.search("bats"))   # False (no exact match)

# Check if a prefix exists
print(trie.starts_with("app"))  # True (app, apple exist)
print(trie.starts_with("bat"))  # True (bat, ball exist)
print(trie.starts_with("cat"))  # False (no words start with 'cat')

#Explanation:
# 1 - Inserting Words: When inserting a word, we traverse the trie character by character. If a character doesn’t exist in the current node's children, we create a new node for that character. Finally, we mark the last character of the word as the end of a valid word.
# 2 - Searching for a Word: To search for a word, we traverse the trie character by character. If we reach the end of the word and is_end_of_word is True, then the word exists in the trie. Otherwise, it does not exist.
# 3 - Prefix Checking: To check for a prefix, we traverse the trie as we do for searching, but we don’t need to check if it's the end of a word. We only check if we can follow the prefix characters to the end.

#Time Complexity:
# 1 - Insertion: O(m), where m is the length of the word being inserted.
# 2 - Search: O(m), where m is the length of the word being searched.
# 3 - StartsWith: O(m), where m is the length of the prefix.

#Space Complexity:
#The space complexity depends on the number of nodes created. In the worst case, if no two words share a prefix, it will take O(n * m) space, where n is the number of words and m is the maximum length of a word. However, in the best case, if many words share prefixes, the space usage can be much lower.

#Advantages:
# 1 - Efficient Search: Searching for a word or a prefix is efficient because it’s done in O(m) time, where m is the length of the word or prefix.
# 2 - Prefix Matching: This is a great advantage when you need to implement features like autocomplete or prefix matching.

#Use Cases:
# 1 - Autocomplete: For a search engine or text input, a trie can provide suggestions based on the prefix entered.
# 2 - Spell Checkers: To quickly search for valid words.
# 3 - Dictionary Implementations: Tries are used in implementations of dictionaries, where lookup, insertion, and prefix checking need to be efficient.
