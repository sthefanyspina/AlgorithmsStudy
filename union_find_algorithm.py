#The Union-Find Algorithm, also known as Disjoint Set Union (DSU), is a data structure that efficiently handles the union and find operations. It's typically used to manage a collection of disjoint sets and supports two primary operations:
# 1 - Find: Determines which set a particular element is in. It can be used for checking if two elements are in the same set.
# 2 - Union: Merges two sets into one, if they are not already in the same set.
# The Union-Find data structure is often used in problems involving connected components, like determining if two nodes are in the same connected component in a graph, Kruskal's algorithm for minimum spanning trees, and other similar graph-related problems.

#Key Concepts:
# 1 - Path Compression: This optimization ensures that trees representing sets remain shallow by making nodes point directly to the root during the find operation. This speeds up future queries.
# 2 - Union by Rank (or Size): This optimization helps keep the tree balanced by always attaching the smaller tree under the root of the larger tree during the union operation. This minimizes the tree height and improves performance.

#Basic Implementation:

class UnionFind:
    def __init__(self, n):
        # Initialize parent and rank arrays
        # Each node is its own parent initially, and rank (or size) is 0
        self.parent = list(range(n))
        self.rank = [0] * n
    
    # Find operation with path compression
    def find(self, x):
        if self.parent[x] != x:
            # Recursively find the root and compress the path
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # Union operation with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank: attach the smaller tree under the larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                # If ranks are equal, make one root and increment its rank
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    # Helper function to check if two elements are connected
    def connected(self, x, y):
        return self.find(x) == self.find(y)

#How It Works:
# 1 - Initialization:
# 1.1 - parent[i] stores the representative (root) of the set containing i. Initially, every element is its own parent (i.e., every element is in its own set).
# 1.2 - rank[i] helps in balancing the tree by keeping track of the tree depth (rank). Initially, all ranks are set to 0.
# 2 - Find:
# 2.1 - To find the root of a set, the function recursively checks the parent of each element until it reaches the root. It applies path compression during this process, so all elements directly point to the root, improving future find operations.
# 3 - Union:
# 3.1 - The union operation merges two sets. If the roots are different, it uses union by rank to decide which tree to attach to the other, ensuring the smaller tree gets attached to the root of the larger tree.
# 4 - Connected:
# 4.1 - This function checks whether two elements belong to the same set by comparing their roots.

#Example Usage:
# Initialize UnionFind for 5 elements (0 to 4)
uf = UnionFind(5)

# Union some sets
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

# Check if 0 and 2 are connected (they are in the same set)
print(uf.connected(0, 2))  # Output: True

# Check if 0 and 4 are connected (they are not in the same set)
print(uf.connected(0, 4))  # Output: False

# Union two sets: set containing 2 and set containing 4
uf.union(2, 4)

# Now 0 and 4 should be connected
print(uf.connected(0, 4))  # Output: True

#Time Complexity:
# 1 - Find operation: O(α(n)), where α(n) is the inverse Ackermann function, which grows extremely slowly. For all practical purposes, it can be considered constant time.
# 2 - Union operation: O(α(n)) as well, due to the combination of path compression and union by rank.

#Applications:
# 1 - Kruskal's Algorithm for Minimum Spanning Tree (MST).
# 2 - Network Connectivity: Checking if two nodes are connected in a graph.
# 3 - Connected Components in a Graph: Identifying all components in a graph.
# 4 - Percolation problems: Determining if there is a path in a grid of blocked/open cells.
