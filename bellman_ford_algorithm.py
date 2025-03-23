#The Bellman-Ford algorithm is an algorithm used for finding the shortest path from a single source node to all other nodes in a weighted graph. It is particularly useful because it can handle graphs with negative weight edges and can also detect negative weight cycles.

#Key Properties of Bellman-Ford:
# 1 - Handles Negative Weights: Unlike Dijkstra's algorithm, Bellman-Ford works with graphs that contain negative weight edges.
# 2 - Detects Negative Weight Cycles: It can detect negative weight cycles in the graph, i.e., cycles that reduce the total path length if you keep traveling around them.

#Steps of the Bellman-Ford Algorithm:
# 1 - Initialization:
# 1.1 - Initialize the distance to the source vertex to 0 and all other vertices to infinity (inf).
# 2 - Relaxation:
# 2.1 - Iterate over all edges and update the distance to the destination vertex if the current path is shorter than the previously known path. This step is repeated for V-1 times, where V is the number of vertices.
# 3 - Negative Weight Cycle Check:
# 3.1 - After V-1 iterations, if any edge can still be relaxed, it indicates a negative weight cycle.

#Bellman-Ford Algorithm Code in Python
#Here is a Python implementation of the Bellman-Ford algorithm:

class Edge:
    def __init__(self, u, v, weight):
        self.u = u  # start node
        self.v = v  # end node
        self.weight = weight  # weight of the edge

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # number of vertices
        self.edges = []  # list to store edges

    def add_edge(self, u, v, weight):
        self.edges.append(Edge(u, v, weight))  # add edge to the list

    def bellman_ford(self, src):
        # Step 1: Initialize distances from source to all other vertices as INFINITE
        dist = [float("inf")] * self.V
        dist[src] = 0  # distance from source to itself is always 0

        # Step 2: Relax all edges (V - 1) times
        for _ in range(self.V - 1):
            for edge in self.edges:
                if dist[edge.u] != float("inf") and dist[edge.u] + edge.weight < dist[edge.v]:
                    dist[edge.v] = dist[edge.u] + edge.weight

        # Step 3: Check for negative-weight cycles
        for edge in self.edges:
            if dist[edge.u] != float("inf") and dist[edge.u] + edge.weight < dist[edge.v]:
                print("Graph contains negative weight cycle")
                return None  # If negative cycle is detected

        return dist

# Example usage:
# Create a graph with 5 vertices (0 to 4)
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

# Run Bellman-Ford algorithm from source vertex 0
distances = g.bellman_ford(0)

if distances:
    print("Shortest distances from source vertex 0:")
    for i in range(len(distances)):
        print(f"Vertex {i}: {distances[i]}")

#Explanation of the Code:
# 1 - Edge Class: This class represents an edge in the graph, which has a start node (u), an end node (v), and a weight for the edge.
# 2 - Graph Class: The graph class holds:
# 2.1 - The number of vertices V.
# 2.2 - A list of edges.
# 2.3 - A method add_edge to add an edge to the graph.
# 2.4 - A method bellman_ford to run the Bellman-Ford algorithm.
# 3 - Initialization:
# 3.1 - The dist list is initialized with infinity (inf), and the distance to the source vertex is set to 0.
# 4 - Relaxation: The edges are relaxed for V-1 times, updating the shortest known distances.
# 5 - Negative Cycle Check: After the relaxation step, the algorithm checks if any edge can still be relaxed, indicating a negative weight cycle.

#Time Complexity:
#O(V * E): Where V is the number of vertices and E is the number of edges. This is because we perform V-1 relaxations over all edges.

#Example Output:
#For the graph in the example, the output might look like this:
Shortest distances from source vertex 0:
Vertex 0: 0
Vertex 1: -1
Vertex 2: 2
Vertex 3: -2
Vertex 4: 1
