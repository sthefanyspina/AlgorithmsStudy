#The Network Flow algorithm deals with the movement of resources through a network represented by a directed graph where nodes are connected by edges. The goal of network flow problems is typically to find the maximum flow from a source node to a sink node or to optimize the flow in some way.
#One of the most famous algorithms for solving Maximum Flow problems is the Ford-Fulkerson Algorithm and its improved version, the Edmonds-Karp Algorithm. These algorithms use the idea of augmenting paths to compute the maximum possible flow in a flow network.

#Steps in the Ford-Fulkerson Algorithm (Edmonds-Karp is a special case):
# 1 - Initialize the flow: Start with a flow of 0 in all edges.
# 2 - Find augmenting paths: Find a path from the source to the sink where additional flow can be pushed through. This can be done using Depth-First Search (DFS) or Breadth-First Search (BFS).
# 3 - Update residual capacities: Increase the flow along the path found, and update the residual capacities of the edges (i.e., the capacity minus the current flow).
# 4 - Repeat: Repeat steps 2-3 until no more augmenting paths can be found. The flow that has been pushed through the network is the maximum flow.

#Edmonds-Karp Algorithm (BFS version of Ford-Fulkerson):
#The Edmonds-Karp algorithm uses Breadth-First Search (BFS) to find the shortest augmenting path (the one with the least number of edges). This reduces the time complexity to O(V×E^2), where V is the number of vertices and E is the number of edges in the graph.

#Python Implementation of Edmonds-Karp Algorithm

from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[0] * vertices for _ in range(vertices)]  # Adjacency matrix to store capacity

    def bfs(self, s, t, parent):
        # BFS to find if there's a path from source (s) to sink (t)
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()

            for v in range(self.V):
                if not visited[v] and self.graph[u][v] > 0:  # If the edge has capacity left
                    if v == t:
                        parent[v] = u
                        return True
                    queue.append(v)
                    parent[v] = u
                    visited[v] = True
        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V  # To store the path
        max_flow = 0

        # Augment the flow while there is a path from source to sink
        while self.bfs(source, sink, parent):
            # Find the maximum flow through the path found by BFS
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Update residual capacities of the edges and reverse edges
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


# Example usage:

# Create a graph given in the example
g = Graph(6)  # 6 vertices
g.graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0  # Source vertex
sink = 5    # Sink vertex

max_flow = g.edmonds_karp(source, sink)
print("The maximum possible flow is:", max_flow)

#Explanation:
# 1 - Graph Class:
# 1.1 - __init__(self, vertices): Initializes the graph with a given number of vertices and an adjacency matrix to represent the capacity between nodes.
# 1.2 - bfs(self, s, t, parent): A Breadth-First Search (BFS) function to find if there’s an augmenting path from the source (s) to the sink (t). If a path is found, it stores the parent of each node in the parent list.
# 1.3 - edmonds_karp(self, source, sink): This function uses the BFS function to repeatedly find augmenting paths and update the flow in the network. It calculates the maximum flow by pushing flow along the augmenting paths.
# 2 - Example Graph:
# 2.1 - A graph with 6 nodes (0 to 5) is created, and capacities between nodes are defined in the adjacency matrix (g.graph).
# 2.2 - The edmonds_karp function is then used to find the maximum flow between the source node (0) and the sink node (5).

#Output:
#The maximum possible flow is: 23

#Key Concepts:
# 1 - Residual Capacity: The remaining capacity of an edge in the graph (i.e., original capacity minus the current flow).
# 2 - Augmenting Path: A path from the source to the sink with positive residual capacity on all edges.
# 3 - Maximum Flow: The largest flow that can be pushed from the source to the sink, respecting the capacity constraints.

#Time Complexity:
#The time complexity of the Edmonds-Karp algorithm is O(V×E^2), where V is the number of vertices, and E is the number of edges. This is due to the BFS finding augmenting paths in O(E) time, and potentially repeating this process O(E) times.

#This algorithm is widely used for solving various flow-related problems, such as:
# 1 - Maximum flow problems
# 2 - Min-cut problems
# 3 - Circulation problems
