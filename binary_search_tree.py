#A Binary Search Tree (BST) is a type of binary tree where each node has at most two children: a left child and a right child. In a BST, the following properties hold:
# 1 - The left child of a node contains a value less than the node's value.
# 2 - The right child of a node contains a value greater than the node's value.
# 3 - This property applies recursively for each node in the tree, so for any node, all nodes in the left subtree have smaller values, and all nodes in the right subtree have larger values.

#Structure of a Node
#Each node in the BST typically has the following attributes:
# 1 - value: Stores the value of the node.
# 2 - left: Points to the left child node.
# 3 - right: Points to the right child node.

#BST Operations
#Common operations in a BST include:
# 1 - Insertion: Insert a value in the tree while maintaining the BST property.
# 2 - Searching: Find whether a value exists in the tree.
# 3 - Traversal: Visit all nodes in a specific order (Inorder, Preorder, Postorder).
# 4 - Deletion: Remove a node and re-adjust the tree.
# 5 - Finding Minimum/Maximum: Find the smallest or largest element.

#Here's a simple implementation of a BST in Python:

#1. Node Class
#A node will have the attributes: value, left child, and right child.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#2. Binary Search Tree Class
#This class will handle insertion, searching, and traversal operations.

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # Search
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # In-order Traversal (left, root, right)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

# Example Usage
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)

print("Inorder Traversal:", bst.inorder())  # [5, 10, 15, 20]
print("Search 15:", bst.search(15))  # True
print("Search 100:", bst.search(100))  # False

#Explanation:
# 1 - Node Class: This is a basic representation of a tree node that holds a value and pointers to the left and right children.
# 2 - BinarySearchTree Class:
# 2.1 - insert(): Adds a new value to the tree.
# 2.2 - search(): Looks for a value in the tree.
# 2.3 - inorder(): Traverses the tree in the "inorder" fashion (left, root, right), which gives values in sorted order for a BST.

#Example Execution:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)

# Inorder traversal will give us [5, 10, 15, 20]
print("Inorder Traversal:", bst.inorder())

# Searching for values
print("Search 15:", bst.search(15))  # True
print("Search 100:", bst.search(100))  # False

#Advantages of BST:
# 1 - Efficient Search: Since the tree is organized, searching for values can be done in O(log n) time in the best case.
# 2 - Sorted Order: An inorder traversal of a BST gives the values in sorted order.

#Considerations:
#If the tree becomes unbalanced (i.e., if values are inserted in sorted order), it degenerates into a linked list with O(n) time complexity for searching and insertion. To handle this, self-balancing trees like AVL or Red-Black trees are used.
