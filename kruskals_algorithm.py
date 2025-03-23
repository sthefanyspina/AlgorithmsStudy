#Kruskal's Algorithm is a classic algorithm used to find the Minimum Spanning Tree (MST) of a graph. The MST is a subset of the edges that connects all the vertices together, without cycles, and with the minimum possible total edge weight.

#Steps for Kruskal's Algorithm:
# 1 - Sort all edges in the graph in increasing order of their weights.
# 2 - Pick the smallest edge. If it forms a cycle (i.e., if the vertices of the edge are already connected), discard it.
# 3 - Repeat the process until you've selected  V−1 edges, where V is the number of vertices in the graph.
#The key challenge is efficiently checking whether adding an edge creates a cycle, which can be solved using the Union-Find or Disjoint Set Union (DSU) data structure.

#Python Code for Kruskal's Algorithm:

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each node is its own parent
        self.rank = [0] * n  # Rank is used for union by rank

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(n, edges):
    uf = UnionFind(n)
    mst = []
    
    # Sort edges by weight (ascending order)
    edges.sort(key=lambda x: x[2])
    
    for u, v, weight in edges:
        if uf.union(u, v):  # If u and v are in different components
            mst.append((u, v, weight))
    
    return mst

# Example usage
n = 4  # Number of vertices
edges = [
    (0, 1, 10),  # (u, v, weight)
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst = kruskal(n, edges)
print("Minimum Spanning Tree:", mst)

#Explanation:
# 1 - UnionFind Class:
# 1.1 - find(u): Returns the root of the set containing u. If u is not its own parent, it recursively finds the parent of u and applies path compression for optimization.
# 1.2 - union(u, v): Merges the sets containing u and v if they are not already connected, using the union by rank technique to keep the tree flat.
# 2 - kruskal(n, edges):
# 2.1 - n: Number of vertices in the graph.
# 2.2 - edges: List of edges represented as tuples (u, v, weight), where u and v are the vertices connected by the edge and weight is the weight of the edge.
# 2.3 - It sorts the edges by weight and then tries to add each edge to the MST if it doesn't create a cycle (using the union method from the UnionFind class).
#Output: The function returns a list of edges that form the MST.

#Example:
#Given the following edges:
(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)
#The output of the algorithm would be:
Minimum Spanning Tree: [(2, 3, 4), (0, 3, 5), (0, 1, 10)]

#Explanation of the Output:
#The edges (2, 3, 4), (0, 3, 5), and (0, 1, 10) form the minimum spanning tree.
#These edges connect all the vertices with the least total weight, and no cycles are formed.

#This implementation runs in O(E log E) time, where E is the number of edges, primarily due to the edge sorting step. The union-find operations are almost constant time,  O(α(n)), where  α(n) is the inverse Ackermann function, which grows extremely slowly.
