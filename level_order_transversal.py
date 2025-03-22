#Level Order Traversal in a binary tree refers to visiting all the nodes level by level, starting from the root and moving down to each subsequent level. The nodes are processed from left to right at each level.
#In simpler terms, it’s like reading the tree level by level, row by row.

#For example, consider the following binary tree:

        1
       / \
      2   3
     / \ / \
    4  5 6  7

#In Level Order Traversal, the nodes would be visited in this order: 1, 2, 3, 4, 5, 6, 7.

#Algorithm for Level Order Traversal:
# 1 - Start from the root node.
# 2 - Use a queue to help keep track of nodes at each level.
# 3 - Dequeue a node, print it, and then enqueue its left and right children.
# 4 - Repeat until the queue is empty.

Python Code Implementation:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # Start with the root node in the queue

    while queue:
        level_nodes = []  # To store nodes at the current level
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()  # Dequeue the front node
            level_nodes.append(node.val)

            # Enqueue left and right children if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)  # Add the current level's nodes to the result

    return result

# Example usage:
# Constructing the tree:
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Calling the function to get level order traversal
result = level_order_traversal(root)
print(result)

#Explanation of the Code:
# 1 - TreeNode class: Defines a binary tree node, with attributes val, left, and right.
# 2 - level_order_traversal function:
# 2.1 - First, check if the root is None. If it is, return an empty list.
#Use a queue (FIFO structure) to help traverse the tree level by level. Initially, the queue contains only the root node.
#In each iteration, process all the nodes at the current level. The number of nodes at the current level is determined by the size of the queue.
#For each node, enqueue its left and right children (if they exist).
#After processing a level, append the values to the result list.

#Example Output:
#For the tree shown above, the output will be:
#[[1], [2, 3], [4, 5, 6, 7]]
#Each list inside the result corresponds to a level of the tree, from top to bottom.

#Time and Space Complexity:
#Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
#Space Complexity: O(n), since at worst, the queue could hold all the nodes at the last level (which is the largest level in a balanced binary tree).
