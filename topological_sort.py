#Topological Sort is an algorithm used to order the nodes of a directed acyclic graph (DAG) in a linear sequence such that for every directed edge u→vu \to vu→v, node uuu comes before node vvv. It’s primarily used for tasks like scheduling or dependency resolution.

#Key Points:
# 1 - Directed Acyclic Graph (DAG): This is a graph where the edges have a direction and no cycles exist.
# 2 - Topological Order: A sequence of nodes where each node appears before all the nodes it points to.

#Problem Example:
#Consider a task dependency graph:
•	Task A must be completed before Task B.
•	Task B must be completed before Task C.
A valid topological order for these tasks could be: A → B → C.

#Approach:
#1.	Identify nodes with no incoming edges (in-degree 0). These can be scheduled first.
#2.	Remove these nodes from the graph, and update the in-degree of their neighbors.
#3.	Repeat the process until all nodes are processed.

#Algorithm Steps:
#1.	Compute in-degree of all nodes. The in-degree of a node is the number of incoming edges.
#2.	Queue all nodes with in-degree 0. These nodes have no dependencies and can be processed.
#3.	For each node: Remove it from the queue and reduce the in-degree of its neighbors.
#4.	If a neighbor’s in-degree becomes 0, add it to the queue.
#5.	If the queue is empty and not all nodes are processed, a cycle exists, and topological sort is not possible.

#Python Code Implementation (using Kahn’s Algorithm):

from collections import deque, defaultdict

def topological_sort(vertices, edges):
    # Step 1: Build the graph and calculate in-degrees
    in_degree = {v: 0 for v in vertices}
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Step 2: Initialize the queue with nodes that have in-degree 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    
    topological_order = []
    
    # Step 3: Process the nodes
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        
        # Decrease the in-degree of neighboring nodes
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check for cycle (if there are nodes with non-zero in-degree)
    if len(topological_order) == len(vertices):
        return topological_order
    else:
        raise ValueError("Graph has a cycle, topological sort is not possible.")

# Example Usage
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'D'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('E', 'F')]

result = topological_sort(vertices, edges)
print("Topological Sort:", result)

#Explanation of Code:
#1 - Input:
# 1.1 - ertices: A list of all nodes.
# 1.2 - edges: A list of directed edges represented as tuples.
# 2 - Graph Construction:
# 2.1 - Create an adjacency list (graph) and compute the in-degree of each node.
# 3 - Queue Initialization:
# 3.1 - Nodes with in-degree 0 (no dependencies) are added to the queue.
# 4 - Processing the Queue:
# 4.1 - Dequeue a node, add it to the result, and decrease the in-degree of its neighbors.
# 4.2 - If any neighbor's in-degree becomes 0, add it to the queue.
# 5 - Cycle Detection:
# 5.1 - If the length of the topological order is not equal to the number of vertices, it means a cycle exists.

#Output for Example:
#Topological Sort: ['A', 'B', 'D', 'C', 'E', 'F']

#Time Complexity:
#O(V + E):
#V is the number of vertices.
#E is the number of edges.
#Each node and edge is processed once.
