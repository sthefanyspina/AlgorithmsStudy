#Tarjan's Algorithm is an efficient method for finding strongly connected components (SCCs) in a directed graph. A strongly connected component is a subset of a directed graph where every vertex is reachable from every other vertex in that subset.
#The algorithm is based on Depth-First Search (DFS) and utilizes two main structures:
# 1 - Discovery time (d): The order in which each node is visited during the DFS.
# 2 - Low-link value (low): The smallest discovery time reachable from the current node (which means the smallest reachable ancestor node).
#Tarjan's algorithm operates in a single DFS pass and uses a stack to keep track of the nodes while exploring. If a node points to an ancestor that hasn’t been fully processed yet, we update the low-link values.

#Steps of Tarjan’s Algorithm:
# 1 - Perform a DFS traversal of the graph, keeping track of each node's discovery time and low-link value.
# 2 - Push nodes onto a stack during the DFS traversal.
# 3 - For each node, for every neighbor (edge):
# 3.1 - If the neighbor has not been visited, recursively perform DFS on that neighbor.
# 3.2 - After recursion, update the current node’s low-link value based on the low-link value of the neighbor.
# 3.3 - If the neighbor is already in the stack, it’s part of the current SCC, and we update the low-link value.
# 4 - When a node’s discovery time is equal to its low-link value, we have identified a strongly connected component. We pop nodes from the stack until we reach the starting node of the SCC.

#Python Implementation:

def tarjan(graph):
    index = 0  # This will track the discovery time for each node
    stack = []  # Stack to store nodes during DFS
    on_stack = set()  # Set to check if a node is in the stack
    indices = {}  # Discovery times of nodes
    low_link = {}  # Low-link values of nodes
    sccs = []  # List of strongly connected components
    
    # Helper function: Depth-First Search (DFS)
    def dfs(v):
        nonlocal index
        indices[v] = low_link[v] = index  # Set discovery time and low-link value
        index += 1
        stack.append(v)  # Push current node to stack
        on_stack.add(v)  # Mark node as being on the stack

        # Explore all neighbors of v
        for w in graph[v]:
            if w not in indices:  # If w hasn't been visited yet
                dfs(w)
                low_link[v] = min(low_link[v], low_link[w])  # Update low-link value
            elif w in on_stack:  # If w is on the stack, it's part of the current SCC
                low_link[v] = min(low_link[v], indices[w])  # Update low-link value

        # If v is a root node, pop all nodes in the current SCC
        if indices[v] == low_link[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)  # Add the current SCC to the result list

    # Run DFS for each unvisited node
    for v in graph:
        if v not in indices:
            dfs(v)
    
    return sccs

# Example Usage:
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3]
}

sccs = tarjan(graph)
print("Strongly Connected Components:", sccs)

#Explanation of Code:
# 1 - Graph Representation: The graph is represented as an adjacency list (a dictionary of lists), where the keys are nodes, and the values are lists of neighbors.
# 2 - DFS: The dfs(v) function is used to traverse the graph recursively. It updates the discovery time and low-link values and manages the stack to track nodes in the current DFS path.
# 3 - Identifying SCCs: If a node’s discovery time equals its low-link value, it means that the node is the root of an SCC. The algorithm then pops nodes from the stack until it reaches this root node.
# 4 - Returning SCCs: The SCCs are collected in the sccs list.

#Example Walkthrough:
#Given the graph:
0 -> 1
1 -> 2
2 -> 0, 3
3 -> 4
4 -> 5
5 -> 3

# 1 - The DFS starts from node 0. It visits nodes 1, 2, 3, 4, and 5.
# 2 - SCCs are identified at nodes 0, 1, and 2, which form a strongly connected component.
# 3 - SCCs also include the cycle formed by nodes 3, 4, and 5.

#Output:
#Strongly Connected Components: [[5, 4, 3], [2, 1, 0]]

#This means that:
# 1 - The SCC formed by nodes 5, 4, and 3.
# 2 - The SCC formed by nodes 2, 1, and 0.

#Complexity:
#Time complexity: O(V + E), where V is the number of vertices and E is the number of edges. This is because each vertex and edge is processed once.
#Space complexity: O(V), where V is the number of vertices, due to the storage required for the stack, indices, and low-link values.
