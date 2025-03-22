#Depth-First Search (DFS) is an algorithm for traversing or searching through a graph or tree. It starts at the root (or an arbitrary node in the case of a graph) and explores as far as possible along each branch before backtracking.
#DFS can be implemented either recursively or iteratively. Here’s a breakdown of how it works and how it can be implemented in Python:

#How DFS works:
# 1 - Start at a node: Begin at the starting node (usually the root or an arbitrary node).
# 2 - Explore each branch: Visit the node and explore its neighbors. If the node has unvisited neighbors, move to one of them.
# 3 - Backtrack: If the current node has no unvisited neighbors, backtrack to the previous node and repeat the process.
# 4 - Repeat: Continue the process until all nodes are visited.

#DFS can be applied to trees or graphs. In a graph, you may encounter cycles, so it’s crucial to mark nodes as visited to prevent going in circles.

#DFS Implementation in Python (Recursive Approach):

# Graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS recursive function
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes
    visited.add(node)  # Mark the node as visited
    print(node)  # Process the node (e.g., print it)
    
    # Visit all the neighbors of the node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Call DFS starting from node 'A'
dfs_recursive(graph, 'A')

#DFS Implementation in Python (Iterative Approach using Stack):

# DFS iterative function using a stack
def dfs_iterative(graph, start):
    visited = set()  # To keep track of visited nodes
    stack = [start]  # Start with the initial node
    
    while stack:
        node = stack.pop()  # Get the current node
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node)  # Process the node (e.g., print it)
            
            # Add all unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Call DFS starting from node 'A'
dfs_iterative(graph, 'A')

#Explanation of the Code:
#Graph Representation: In both examples, the graph is represented as an adjacency list, where each node is associated with a list of its neighbors.

#Recursive DFS:
# 1 - The function dfs_recursive() starts at the given node and explores its neighbors recursively.
# 2 - The visited set keeps track of nodes that have been visited to avoid revisiting nodes.

#Iterative DFS:
# 1 - The iterative approach uses a stack to keep track of nodes. Nodes are processed by popping them from the stack.
# 2 - Neighbors of a node are added to the stack if they haven’t been visited yet.

#Time and Space Complexity:
#Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. Each node and edge is visited once.
#Space Complexity: O(V), since the space is required to store the visited nodes and the stack (or recursive call stack).
