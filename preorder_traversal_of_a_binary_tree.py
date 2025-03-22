#Preorder traversal of a binary tree is one of the depth-first search (DFS) strategies for traversing trees. In this approach, you visit the nodes of the binary tree in the following order:

# 1 - Visit the root node
# 2 - Traverse the left subtree recursively
# 3 - Traverse the right subtree recursively

#Algorithm:
# 1 - Start from the root.
# 2 - Visit the root node.
# 3 - Traverse the left child recursively.
# 4 - Traverse the right child recursively.

Python Code Example:

# Defining the structure of a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Preorder Traversal function
def preorder_traversal(root):
    if root:
        # First visit the root
        print(root.data, end=' ')
        # Then traverse the left subtree
        preorder_traversal(root.left)
        # Finally traverse the right subtree
        preorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    # Creating a binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Preorder traversal
    print("Preorder Traversal of Binary Tree:")
    preorder_traversal(root)

#Explanation:
# 1 - Node Class: This defines the structure of a tree node, with attributes for data, left, and right pointers.
# 2 - preorder_traversal Function: This function performs the preorder traversal. It first prints the root's value, then recursively traverses the left and right subtrees.

#Example Output:
#For the tree mentioned in the example, the output of the preorder traversal will be:
#Preorder Traversal of Binary Tree:
#1 2 4 5 3

#How it works:
# 1 - Start at the root (1), visit it, then move to the left child (2).
# 2 - Visit node 2, then move to its left child (4) and visit it.
# 3 - After visiting 4, backtrack to 2, visit its right child (5), and visit 5.
# 4 - Backtrack to 1 and move to its right child (3), and visit 3.
