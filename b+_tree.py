#A B+ Tree is a type of self-balancing tree data structure that is commonly used for indexing and searching in databases and file systems. It is an extension of the B-tree, where every leaf node contains the actual data, and internal nodes only store keys for navigation. The B+ Tree ensures that the data is kept sorted, which allows for efficient searching, insertion, deletion, and range queries.

#Key Features of B+ Tree:
# 1 - Balanced: All leaf nodes are at the same level, ensuring that the tree remains balanced, and search operations are efficient.
# 2 - Nodes:
# 2.1 - Internal Nodes: Contain only keys to guide the search process.
# 2.2 - Leaf Nodes: Contain actual data or references to the data.
# 3 - Ordered: Data in leaf nodes is ordered in a linked list, allowing for efficient range queries.
# 4 - Height of the Tree: The height of the tree is logarithmic, ensuring fast searching and inserting operations.

#Structure of a B+ Tree:
# 1 - Root Node: The root contains a set of keys that point to child nodes. If the tree has more than one level, the root node points to child internal nodes or leaf nodes.
# 2 - Internal Nodes: Each internal node has keys and pointers to its child nodes.
# 3 - Leaf Nodes: The leaf nodes store the actual data, and they are connected to each other in a linked list to support efficient range queries.

#Operations in B+ Trees:
# 1 - Search: Start from the root and follow the pointers to the appropriate leaf node.
# 2 - Insertion: Insert data into the correct leaf node, and if the node overflows, split it and propagate the split upwards.
# 3 - Deletion: Remove data from the leaf node and handle underflows by merging or redistributing nodes.
# 4 - Range Queries: Due to the linked list between leaf nodes, range queries can be performed efficiently.

#Example of Implementing a Simple B+ Tree in Python:

class BPlusTree:
    class Node:
        def __init__(self, leaf=False):
            self.leaf = leaf
            self.keys = []
            self.children = []

    def __init__(self, order=3):
        self.root = self.Node(leaf=True)
        self.order = order  # Max number of keys in a node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node.leaf:
            # Search in leaf nodes
            if key in node.keys:
                return True
            return False
        else:
            # Search in internal nodes
            for i in range(len(node.keys)):
                if key < node.keys[i]:
                    return self._search(node.children[i], key)
            return self._search(node.children[-1], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.order - 1:
            # Root is full, split it
            new_root = self.Node(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()  # Keep the keys sorted
        else:
            for i in range(len(node.keys)):
                if key < node.keys[i]:
                    self._insert_non_full(node.children[i], key)
                    return
            self._insert_non_full(node.children[-1], key)

    def _split_child(self, parent, index):
        node = parent.children[index]
        new_node = self.Node(leaf=node.leaf)
        mid_key = node.keys[self.order // 2]
        
        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, new_node)
        
        # Move the second half of keys and children to the new node
        new_node.keys = node.keys[self.order // 2 + 1:]
        node.keys = node.keys[:self.order // 2]
        
        if not node.leaf:
            new_node.children = node.children[self.order // 2 + 1:]
            node.children = node.children[:self.order // 2 + 1]

    def display(self):
        self._display(self.root, 0)

    def _display(self, node, level):
        print("Level", level, ":", node.keys)
        if not node.leaf:
            for child in node.children:
                self._display(child, level + 1)


# Usage example
bplus_tree = BPlusTree(order=4)
bplus_tree.insert(10)
bplus_tree.insert(20)
bplus_tree.insert(5)
bplus_tree.insert(6)
bplus_tree.insert(12)
bplus_tree.insert(30)

bplus_tree.display()

# Searching
print("Search 6:", bplus_tree.search(6))
print("Search 15:", bplus_tree.search(15))

#Explanation of the Code:
# 1 - BPlusTree Class: This class represents the B+ Tree and contains methods for insertion, search, and display.
# 2 - Node Class: This class represents a node in the tree, and each node can be a leaf or an internal node.
# 3 - Insert Method: Inserts a key into the B+ Tree. If the root is full, the tree splits and a new root is created.
# 4 - Search Method: A basic search method to find if a key exists in the tree.
# 5 - Split Child Method: This method is used when a node becomes full during insertion. It splits the node and propagates the split upwards if necessary.
# 6 - Display Method: Displays the structure of the tree (this is useful for visualization during debugging).

#Features:
# 1 - Order: The maximum number of children a node can have (which determines the maximum number of keys).
# 2 - Balanced: Ensures all leaf nodes are at the same depth.
