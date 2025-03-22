#Inorder Traversal is one of the ways to traverse a binary tree. In this method, we visit the nodes in the following order:
# 1 - Traverse the left subtree.
# 2 - Visit the root node.
# 3 - Traverse the right subtree.
#For a binary tree, the traversal would result in visiting the nodes in the order of "Left -> Root -> Right."

#Steps for Inorder Traversal:
# 1 - Start with the root node.
# 2 - Recursively visit the left subtree.
# 3 - Visit the root node.
# 4 - Recursively visit the right subtree.

#Inorder Traversal Implementation in Python
#You can implement Inorder Traversal using both recursion and iteration. Let's start with the recursive approach.

#Recursive Inorder Traversal:

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Recursive Inorder Traversal function
def inorder_traversal(root):
    if root is None:
        return []
    
    # Traverse left subtree, visit root, then traverse right subtree
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Example usage:
# Creating a binary tree: 
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorder_traversal(root))  # Output: [4, 2, 5, 1, 3]

#Explanation:
# 1 - If the current node is None, we return an empty list.
# 2 - We recursively call inorder_traversal on the left subtree.
# 3 - Add the value of the root node (root.val).
# 4 - Recursively call inorder_traversal on the right subtree.
# 5 - Combine the results by adding the left subtree result, the root node value, and the right subtree result.

#Iterative Inorder Traversal (Using a Stack):
#An iterative approach to Inorder Traversal uses a stack to simulate the recursion.

def inorder_traversal_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            # Go to the leftmost node
            stack.append(current)
            current = current.left
        
        # Pop from stack and visit the node
        current = stack.pop()
        result.append(current.val)
        
        # Go to the right node
        current = current.right
    
    return result

# Example usage:
print(inorder_traversal_iterative(root))  # Output: [4, 2, 5, 1, 3]

#Explanation:
# 1 - Use a stack to store nodes as you go down to the leftmost node.
# 2 - Once there are no more left children, pop a node from the stack and visit it.
# 3 - Then, move to the right child and repeat the process.

Summary:
Recursive Method: Easy to implement and uses function call stack.

Iterative Method: More efficient for large trees (since it avoids using the system's function call stack) and uses an explicit stack.
