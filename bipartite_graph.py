#A Bipartite Graph is a type of graph where the vertices can be divided into two disjoint sets such that no two vertices within the same set are adjacent. In other words, each edge connects a vertex from one set to a vertex from the other set.
#To determine if a graph is bipartite, one efficient way is to check if we can color the graph using two colors. This can be done using Breadth-First Search (BFS) or Depth-First Search (DFS).
#The general approach to solving this problem involves:
# 1 - Assigning a color to a node (either 0 or 1).
# 2 - Attempting to assign the opposite color to all its neighbors.
# 3 - If at any point two adjacent nodes have the same color, the graph is not bipartite.
# 4 - If all nodes can be colored alternately, then the graph is bipartite.

#Steps for the Algorithm:
# 1 - Initialize the colors for each node as -1 (indicating that no node has been colored).
# 2 - Iterate through all components of the graph using BFS or DFS.
# 3 - Check adjacent nodes: If two adjacent nodes have the same color, the graph is not bipartite.

#Code Implementation Using BFS
#Here’s how you could implement this algorithm in Python using BFS:

from collections import deque

# Function to check if the graph is bipartite
def is_bipartite(graph):
    # Create a color array to store the color of each node
    color = [-1] * len(graph)
    
    # Function to perform BFS
    def bfs(start):
        queue = deque([start])
        color[start] = 0  # Assign the first color
        
        while queue:
            node = queue.popleft()
            # Check all adjacent nodes
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If neighbor hasn't been colored
                    # Color the neighbor with the opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # If the neighbor has the same color, it's not bipartite
                    return False
        return True

    # Check for all components of the graph
    for node in range(len(graph)):
        if color[node] == -1:  # If node is not colored yet
            if not bfs(node):
                return False
    return True

# Example usage
# Graph represented as adjacency list
graph = [
    [1, 3],    # Node 0 is connected to Node 1 and Node 3
    [0, 2],    # Node 1 is connected to Node 0 and Node 2
    [1, 3],    # Node 2 is connected to Node 1 and Node 3
    [0, 2]     # Node 3 is connected to Node 0 and Node 2
]

# Check if the graph is bipartite
if is_bipartite(graph):
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")

#Explanation:
# 1 - Graph Representation: The graph is represented as an adjacency list where each index represents a node and contains a list of its neighbors.
# 2 - Color Array: The color array keeps track of the colors of each node. Initially, all nodes are colored -1 (uncolored).
# 3 - BFS Function: For each uncolored node, we perform a BFS. Starting from a node, we color it with 0 and its neighbors with 1, alternating colors as we go through the graph. If we find two adjacent nodes with the same color, we return False.
# 4 - Main Function: We check for all nodes (in case the graph has multiple disconnected components). If any component is not bipartite, the function returns False.

#Time Complexity:
#The time complexity is O(V + E), where V is the number of vertices and E is the number of edges. This is because we visit every vertex and edge once during the BFS traversal.

#Example:
For the graph given:

0 -- 1
|    |
3 -- 2
The graph is bipartite because we can color the nodes as follows:
Node 0: color 0
Node 1: color 1
Node 2: color 0
Node 3: color 1
