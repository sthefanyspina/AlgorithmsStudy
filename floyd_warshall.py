#The Floyd-Warshall algorithm is an all-pairs shortest path algorithm that is used to find the shortest paths between all pairs of vertices in a weighted graph. It works by iteratively considering whether a path through an intermediate vertex would be shorter than the direct path between two vertices.

#Key Points:
#It is used to find the shortest paths in a weighted graph (both positive and negative weights, but no negative weight cycles).
#It works by progressively trying to improve the shortest path between every pair of nodes.
#The time complexity of the Floyd-Warshall algorithm is O(V 3 ), where V is the number of vertices in the graph.

#Steps:
#Start with a graph where the distance between each pair of vertices is initialized as infinity (or a very large number), except for the diagonal (distance from a node to itself), which is set to 0.
#For each possible intermediate vertex, check whether a path from vertex i to vertex j passing through this intermediate vertex would be shorter than the previously known path. If it is, update the distance.

#Python Implementation:

# Floyd-Warshall Algorithm
def floyd_warshall(graph):
    # Get the number of vertices
    V = len(graph)

    # Create a distance matrix and initialize it with the given graph values
    dist = [row[:] for row in graph]  # Make a copy of the graph matrix

    # Floyd-Warshall algorithm
    for k in range(V):  # Consider each vertex as an intermediate vertex
        for i in range(V):  # Loop over each row
            for j in range(V):  # Loop over each column
                # If the path through vertex k is shorter than the direct path from i to j
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
# Create a graph as an adjacency matrix
# graph[i][j] represents the edge weight from vertex i to vertex j
# Use float('inf') to represent no path between vertices

graph = [
    [0, 3, float('inf'), float('inf')],
    [float('inf'), 0, 1, float('inf')],
    [float('inf'), float('inf'), 0, 7],
    [2, float('inf'), float('inf'), 0]
]

# Apply Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Output the shortest paths matrix
for row in shortest_paths:
    print(row)

#Explanation:
# 1 - Input graph: The graph variable is represented as an adjacency matrix where graph[i][j] indicates the weight of the edge from vertex i to vertex j. If there is no edge between the vertices, we use float('inf') to represent this.
# 2 - Distance matrix (dist): Initially, dist is a copy of the input graph. The matrix will be updated as we go through the algorithm, considering each vertex as an intermediate node to potentially improve the shortest paths between all pairs of nodes.
# 3 - Triple Nested Loops:
# 3.1 - The outer loop (with index k) represents the intermediate vertex we're considering.
# 3.2 - The middle and inner loops (with indices i and j) represent the pair of vertices for which we're calculating the shortest path.
# 3.3 - If the direct path from vertex i to vertex j is longer than the path that goes through vertex k, we update dist[i][j].

#Output:
#For the given graph, the output matrix will show the shortest path distances between every pair of vertices. For example:
[0, 3, 4, 10]
[4, 0, 1, 8]
[9, 6, 0, 7]
[2, 5, 6, 0]

#Time Complexity:
#The time complexity of the Floyd-Warshall algorithm is O(V3), where V is the number of vertices.
#The three nested loops result in O(V3) operations, which can be slow for very large graphs.
