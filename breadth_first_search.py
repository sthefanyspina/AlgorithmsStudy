#Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root node (or any arbitrary node in the case of a graph) and explores all the neighboring nodes at the present depth level before moving on to nodes at the next depth level.

#Key Characteristics of BFS:
# 1 - Queue-based: BFS uses a queue to keep track of the nodes that need to be explored.
# 2 - Level by level: BFS explores nodes level by level, meaning it first visits all nodes at depth 1, then all nodes at depth 2, and so on.
# 3 - Shortest Path: BFS can be used to find the shortest path in an unweighted graph.

Steps in BFS:
# 1 - Start at a given node (usually the root or starting node).
# 2 - Enqueue the starting node to the queue and mark it as visited.
# 3 - While the queue is not empty, do the following:
# 3.1 - Dequeue a node from the queue.
# 3.2 - Visit all its unvisited neighbors, mark them as visited, and enqueue them.
# 4 - Repeat until all nodes are explored.

#Python Implementation of BFS:

from collections import deque

def bfs(graph, start):
    # Create a queue for BFS and add the starting node to it
    queue = deque([start])
    
    # Create a set to track visited nodes
    visited = set()
    
    # Mark the start node as visited
    visited.add(start)
    
    # List to store the order of traversal
    traversal_order = []
    
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        
        # Add the node to the traversal order
        traversal_order.append(node)
        
        # Visit all the unvisited neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Mark the neighbor as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal_order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS starting from node 'A'
result = bfs(graph, 'A')
print("BFS Traversal Order:", result)

#xplanation:
# 1 - The graph is represented as an adjacency list, where each key is a node, and the value is a list of neighboring nodes.
# 2 - The bfs function starts at a given node (e.g., 'A') and explores the graph in a breadth-first manner.
# 3 - A queue (deque) is used to keep track of nodes to visit, and a set (visited) ensures each node is only processed once.
# 4 - The function returns the order in which nodes are visited during the BFS traversal.

#Example Output:
#BFS Traversal Order: ['A', 'B', 'C', 'D', 'E', 'F']
#In this example, BFS starts from node 'A', then explores its neighbors 'B' and 'C', then moves to their neighbors, and so on. The result is a breadth-first traversal of the graph.
