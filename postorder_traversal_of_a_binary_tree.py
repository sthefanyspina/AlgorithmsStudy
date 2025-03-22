#In postorder traversal, the nodes of a binary tree are visited in the following order:
# 1 - Left subtree
# 2 - Right subtree
# 3 - Root node

#So, we first visit the left child, then the right child, and finally the root node for each subtree, starting from the root of the entire tree.

#Python Implementation

#1. Recursive Postorder Traversal
#In a recursive approach, you traverse the left and right subtrees first, and then visit the root node.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def postorder_traversal(root):
    if root is None:
        return []
    
    # Visit left subtree, then right subtree, then the root
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

# Example usage:
# Creating a simple binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(postorder_traversal(root))  # Output: [4, 5, 2, 3, 1]

#Explanation of Recursive Approach:
# 1 - Base Case: If the node is None, return an empty list.
# 2 - Recursive Step: Traverse the left subtree, then the right subtree, and finally add the current node’s value to the result list.

#2. Iterative Postorder Traversal
#The iterative method typically uses a stack to simulate the recursive call stack. It requires more careful management of the traversal process.

def postorder_traversal_iterative(root):
    if root is None:
        return []
    
    stack = []
    output = []
    
    while stack or root:
        if root:
            stack.append(root)
            output.append(root.value)  # Push root value to output first
            root = root.right  # Move to the right child first
        else:
            node = stack.pop()
            root = node.left  # Move to the left child next
    
    return output[::-1]  # Reverse the output to get correct postorder

# Example usage:
print(postorder_traversal_iterative(root))  # Output: [4, 5, 2, 3, 1]

#Explanation of Iterative Approach:
#We traverse the tree and push the node's value onto a stack, but we first visit the right child before the left child.
#After visiting the nodes, we reverse the output because we are collecting nodes in root-right-left order, but we want the left-right-root order of postorder traversal.

#Summary:
#Recursive approach is simple and natural, leveraging the function call stack.
#Iterative approach uses a stack explicitly to simulate the recursion, providing more control over the traversal.
