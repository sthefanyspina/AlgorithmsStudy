#Dijkstra's algorithm is a classic algorithm used to find the shortest paths between nodes in a graph, which may represent, for example, road networks, communication networks, or any situation where you're looking to find the most efficient route between points. The algorithm works by iteratively selecting the nearest unvisited node and updating the shortest path estimates for its neighbors.

#Here's a step-by-step breakdown of how Dijkstra's algorithm works:
# 1 - Initialization:
# 1.1 - Set the distance to the start node to 0 and to infinity for all other nodes.
# 1.2 - Mark all nodes as unvisited.
# 2 - Visit the unvisited node with the smallest known distance:
# 2.1 - For the current node, check all its neighboring nodes.
# 2.2 - For each neighbor, calculate the tentative distance from the start node. If this new distance is smaller than the current known distance, update it.
# 3 - Mark the current node as visited (it will not be checked again).
# 4 - Repeat this process until you visit all nodes or until the smallest tentative distance among the unvisited nodes is infinity (which happens if there is no connection between the start node and remaining unvisited nodes).

#Example Code in Python

import heapq

def dijkstra(graph, start):
    # Priority queue to hold the vertices to be visited with their current shortest distance
    priority_queue = [(0, start)]  # (distance, node)
    
    # Dictionary to store the shortest path to each node
    shortest_paths = {start: 0}
    
    # Set of visited nodes
    visited = set()
    
    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip the node if it has already been visited
        if current_node in visited:
            continue
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Check each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            
            # Calculate the distance to the neighbor
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update the shortest path
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Example graph: an adjacency dictionary where keys are nodes and values are dictionaries of neighbors with edge weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Find the shortest paths from node 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)

#Explanation of the Code:
# 1 - Graph Representation: The graph is represented as an adjacency dictionary where each key is a node, and each value is a dictionary representing the neighboring nodes and their edge weights.
# 2 - Priority Queue: A priority queue (implemented with heapq) is used to always select the node with the smallest tentative distance. The heapq.heappop() function efficiently retrieves the node with the smallest distance.
# 3 - Shortest Path Tracking: A dictionary shortest_paths keeps track of the shortest distance from the start node to every other node in the graph.
# 4 - Processing: For each node, we examine its neighbors, calculate the tentative distances, and update the shortest path if a shorter one is found.
# 5 - Result: The algorithm returns a dictionary with the shortest path distances from the starting node to all other nodes.

#Output Example:
#For the graph provided, the output would look like:
#{'A': 0, 'B': 1, 'C': 3, 'D': 4}
#This means:
#The shortest distance from A to A is 0.
#The shortest distance from A to B is 1.
#The shortest distance from A to C is 3.
#The shortest distance from A to D is 4.

#Key Points:
#Dijkstra's algorithm assumes all edge weights are non-negative.
#The time complexity of this implementation is  O((V+E)logV), where V is the number of vertices and E is the number of edges, due to the priority queue operations.
