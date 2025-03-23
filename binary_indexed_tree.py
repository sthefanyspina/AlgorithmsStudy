#A Binary Indexed Tree (BIT) or Fenwick Tree is a data structure that efficiently supports two main operations on an array:
# 1 - Point updates (update a single element in the array).
# 2 - Prefix sum queries (compute the sum of elements from the start of the array up to a given index).
#It is a space-efficient and time-efficient data structure for handling cumulative frequency tables or prefix sum queries in O(logn) time, where n is the number of elements in the array.

#Operations:
# 1 - Update: Update a specific index in the array, adding a value to it.
# 2 - Query: Compute the prefix sum (sum of elements from the start to a given index).

#Key Properties:
# 1 - Binary Indexed Tree is built on the binary representation of indices.
# 2 - It uses a bit manipulation trick to efficiently store and calculate prefix sums.

#Binary Indexed Tree (BIT) Basics:
# 1 - It stores the prefix sums in a way that allows quick updates and queries.
# 2 - The structure is built using an auxiliary array where each position in the array stores the cumulative sum for a certain range of indices.

#How it Works:
# 1 - The BIT uses the binary representation of indices to determine the range each element covers.
# 2 - Each index i in the tree is responsible for a range of elements in the array, and the size of that range is related to the least significant bit of i (in its binary representation).

#Binary Representation Insight:
# 1 - The BIT is built on the fact that the binary representation of a number shows the power-of-2 size of the range it represents.
# 2 - For an index i, the parent index is determined by i−(i&−i), and the child index can be calculated by i+(i&−i).

#Operations:
# 1 - Updating an element:
# 1.1 - To update the value at index i, add the difference to the current value at index i and propagate the change to the next indices.
# 2 - Querying the prefix sum:
# 2.1 - To compute the sum from index 1 to i, sum all the values at indices that cover the range [1,i], determined by the binary representation.

#Python Code Implementation of Binary Indexed Tree:

class BIT:
    def __init__(self, n):
        # Initialize the BIT with n elements (indexed 1 to n)
        self.n = n
        self.tree = [0] * (n + 1)  # Tree is 1-indexed

    # Update the BIT by adding value `delta` at index `i`
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i  # Move to the next index that needs to be updated

    # Query the prefix sum from index 1 to i (inclusive)
    def query(self, i):
        sum_ = 0
        while i > 0:
            sum_ += self.tree[i]
            i -= i & -i  # Move to the parent index
        return sum_

    # To get the sum of the range [l, r], use the formula:
    # sum(l, r) = query(r) - query(l-1)
    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

#Example Usage:
# Initialize a BIT for an array of size 5 (indexed 1 to 5)
bit = BIT(5)

# Update the array values:
# Adding 1 to index 1
bit.update(1, 1)

# Adding 3 to index 2
bit.update(2, 3)

# Adding 2 to index 3
bit.update(3, 2)

# Query the prefix sum from 1 to 3 (should be 1 + 3 + 2 = 6)
print(bit.query(3))  # Output: 6

# Query the sum of the range [2, 3] (should be 3 + 2 = 5)
print(bit.range_query(2, 3))  # Output: 5

# Update index 2 by adding 2 (i.e., changing it from 3 to 5)
bit.update(2, 2)

# Query the sum from 1 to 3 (should now be 1 + 5 + 2 = 8)
print(bit.query(3))  # Output: 8

#Explanation of Code:
# 1 - Initialization (__init__):
# 1.1 - The constructor initializes an array tree of size  n+1 (to use 1-based indexing) to store the cumulative sums.
# 2 - Update (update):
# 2.1 - The update method updates the value at index  i. It starts from index i, adds the difference delta, and then moves to the next index that is responsible for this range (which is computed by i += i & -i).
# 3 - Query (query):
# 3.1 - The query method computes the prefix sum from index 1 to i. It accumulates the values from the BIT by moving upwards, using the formula i -= i & -i.
# 4 - Range Query (range_query):
# 4.1 - To compute the sum of elements in a specific range [l, r], we use the formula: sum(l,r)=query(r)−query(l−1)
# 4.2 - This returns the sum of the elements between index l and r inclusively.

#Time Complexity:
# 1 - Update operation: O(logn), as we only update a few indices (related to the binary representation of i).
# 2 - Query operation: O(logn), because we only query a few indices in the BIT.

#Space complexity: 
#O(n), as we store an array of size n+1 to represent the BIT.

#Advantages:
# 1 - Efficient for Dynamic Queries: BIT is efficient for scenarios where you need to perform frequent updates and queries on an array.
# 2 - Simple Implementation: It is relatively simple to implement compared to other data structures like Segment Trees.

#Applications:
# 1 - Prefix sum calculations in dynamic arrays.
# 2 - Dynamic cumulative frequency tables.
# 3 - K-th order statistics and range queries.
# 4 - Counting inversions in an array (by maintaining cumulative frequency of numbers).
