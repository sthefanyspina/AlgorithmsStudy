#A commonly used approach to detect cycles in a directed graph is using Depth-First Search (DFS) along with a recursion stack. Here's how it works:
# 1 - DFS Traversal:
# 1.1 - Perform DFS on the graph starting from each unvisited vertex.
# 1.2 - During the DFS traversal, mark the current vertex as visited and also mark it as in the recursion stack (i.e., it's part of the current DFS path).
# 2 - Cycle Detection:
# 2.1 - If during DFS traversal, we reach a vertex that is already in the recursion stack, it means we've encountered a back edge, which indicates a cycle.
# 3 - Marking Vertices:
# 3.1 - A vertex is visited once it has been fully explored (i.e., all its neighbors have been processed).
# 3.2 - A vertex is in the recursion stack if it's part of the current DFS call. This helps to detect back edges.

#Steps for Cycle Detection:
# 1 - Use a visited[] array to keep track of visited vertices.
# 2 - Use a recursion stack (in_stack[]) to track vertices currently in the DFS call.
# 3 - If you encounter a vertex that is already in the recursion stack during DFS, you have detected a cycle.

#Python Code for Cycle Detection in a Directed Graph

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = {i: [] for i in range(vertices)}  # adjacency list representation of the graph

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Add edge from u to v

    def dfs(self, v, visited, in_stack):
        visited[v] = True
        in_stack[v] = True

        # Explore all neighbors
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, in_stack):
                    return True
            elif in_stack[neighbor]:
                # If the neighbor is already in the recursion stack, a cycle is found
                return True

        in_stack[v] = False  # Backtrack: remove the vertex from the recursion stack
        return False

    def detect_cycle(self):
        visited = [False] * self.V
        in_stack = [False] * self.V

        # Call DFS for every unvisited vertex
        for vertex in range(self.V):
            if not visited[vertex]:
                if self.dfs(vertex, visited, in_stack):
                    return True

        return False


# Example usage
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # This creates a cycle: 0 -> 1 -> 2 -> 0
g.add_edge(3, 2)

if g.detect_cycle():
    print("Graph contains a cycle")
else:
    print("Graph doesn't contain a cycle")

#Explanation of the Code:
# 1 - Graph Representation: The graph is represented using an adjacency list. The Graph class has a method add_edge(u, v) to add a directed edge from vertex u to vertex v.
# 2 - DFS Function:
# 2.1 - dfs(v, visited, in_stack) is a recursive function that performs DFS starting from vertex v.
# 2.2 - It marks the vertex v as visited and adds it to the recursion stack.
# 2.3 - It explores all neighbors of v. If any neighbor is in the recursion stack (i.e., it's part of the current DFS path), a cycle is detected.
# 2.4 - Once all neighbors are processed, the vertex is removed from the recursion stack.
# 3 - Cycle Detection:
# 3.1 - The detect_cycle() function iterates through all vertices and starts a DFS if the vertex hasn't been visited yet.
# 3.2 - If a cycle is detected in any DFS traversal, it immediately returns True.
# 3.3 - If no cycles are found after processing all vertices, it returns False.

#Example:
#For the graph:
0 -> 1 -> 2 -> 0 (cycle)
    |
    v
    3
#The code will output:
#Graph contains a cycle

#Time Complexity: O(V+E)
#Each vertex is visited once during DFS traversal, and each edge is checked once.
#V is the number of vertices and E is the number of edges in the graph.

#Space Complexity: O(V)
#The space is used by the visited[] and in_stack[] arrays, both of size V.

#Key Points:
# 1 - The DFS is used to explore the graph.
# 2 - The recursion stack (in_stack[]) helps to identify back edges (cycles).
# 3 - This approach efficiently detects cycles in a directed graph.
