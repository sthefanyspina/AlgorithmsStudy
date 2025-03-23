#A Segment Tree is a binary tree data structure used for efficient range query and update operations on an array. It's particularly useful for problems where you need to perform queries (like finding the sum, minimum, or maximum of a range) and updates (modifying the value of an element) repeatedly on an array. The main advantage of a segment tree over a brute-force approach is that both query and update operations can be done in O(log n) time, making it much faster for large datasets compared to a linear approach.

#Key Operations:
# 1 - Build: Construct the segment tree from a given array.
# 2 - Query: Perform a range query (e.g., sum, min, max) over a given segment of the array.
# 3 - Update: Update an element in the array and reflect the change in the segment tree.

#Structure of a Segment Tree:
# 1 - The tree is a binary tree, where each node represents an interval (or segment) of the array.
# 2 - The leaf nodes represent individual elements of the array.
# 3 - Internal nodes represent the aggregate (sum, minimum, maximum, etc.) of the elements in their respective ranges.

#Segment Tree Example:
#Given an array arr = [1, 3, 5, 7, 9, 11], you can build a segment tree to handle queries like:
# 1 - Range Sum: Sum of elements in a specified range, e.g., sum of elements from index 1 to 3.
# 2 - Range Minimum: Minimum value in a specified range.

#Building the Segment Tree:
#The segment tree is built recursively. A node at index i stores the result of a function (like sum, min, max) over a specific segment of the array. The leaf nodes represent individual elements, and each internal node represents a combination of the results from its children.

#Algorithm:
# 1 - Build the segment tree in a recursive manner.
# 2 - For a query, traverse the tree to find the result for the desired range.
# 3 - For an update, propagate the change up the tree to update the necessary segments.

#Python Code for Segment Tree (Range Sum Query)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)  # Segment tree array
        
        # Build the segment tree
        self.build(arr)

    def build(self, arr):
        # Insert the elements in the leaves of the tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        
        # Build the tree by combining the elements
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        # Set value at the leaf node
        index += self.n  # Shift index to the leaf
        self.tree[index] = value
        
        # Update all ancestors
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, left, right):
        # Query the sum in the range [left, right]
        left += self.n  # Shift left to the leaf
        right += self.n  # Shift right to the leaf
        result = 0

        while left <= right:
            if left % 2 == 1:  # If left is odd, it's a right child
                result += self.tree[left]
                left += 1  # Move to the next node
            if right % 2 == 0:  # If right is even, it's a left child
                result += self.tree[right]
                right -= 1  # Move to the previous node
            
            left //= 2
            right //= 2

        return result


# Example usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Range sum query: sum of elements from index 1 to 3
print(seg_tree.query(1, 3))  # Output: 15 (3 + 5 + 7)

# Update: change value at index 2 to 6
seg_tree.update(2, 6)

# After the update, query the sum again
print(seg_tree.query(1, 3))  # Output: 16 (3 + 6 + 7)

#Explanation of Code:
# 1 - Initialization:
# 1.1 - The segment tree is initialized with an array arr. The size of the tree array is 2 * n because the segment tree is stored in a complete binary tree structure.
# 1.2 - The leaves of the segment tree are stored at indices from n to 2n-1, and the internal nodes are stored from 1 to n-1.
# 2 - Building the Tree:
# 2.1 - We start by placing the elements of the array into the leaves of the tree. This is done in the build function.
# 2.2 - Then, we build the internal nodes by recursively combining the values of their children. In the case of the sum segment tree, each internal node is the sum of its two children.
# 3 - Update Operation:
# 3.1 - When an update is made, we directly update the corresponding leaf node and then propagate the change up the tree to update all affected internal nodes.
# 4 - Query Operation:
# 4.1 - To query the sum of elements in a given range, we move from the leaves to the internal nodes, combining the results of the relevant segments. We use a bottom-up approach, adjusting the left and right indices as we traverse the tree.

#Time Complexity:
# 1 - Building the Tree: O(n), where n is the size of the input array.
# 2 - Query Operation: O(log n), as we only visit nodes on the path from the leaves to the root.
# 3 - Update Operation: O(log n), as we need to propagate the update through the tree.

#Space Complexity:
#O(2n) for the segment tree array, as we store both the leaves and internal nodes of the tree.

#Example Walkthrough:
For the array arr = [1, 3, 5, 7, 9, 11]:

#The segment tree will look like this after building:
                    36
                 /      \
               16        20
             /    \     /    \
            4      12   16     4
           / \    /  \  /  \   / \
          1   3  5   7  9  11  0  0

#A range sum query, such as query(1, 3), will result in the sum of elements between indices 1 and 3, which is 3 + 5 + 7 = 15.
#An update at index 2 (update(2, 6)) will modify the array and update the tree accordingly.

#Applications of Segment Trees:
# 1 - Range Sum Queries: To compute the sum of elements in a subrange of an array.
# 2 - Range Minimum/Maximum Queries: To find the minimum or maximum in a subrange.
# 3 -Dynamic Range Queries: If the array is constantly changing, a segment tree allows for efficient updates and queries.
