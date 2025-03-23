#The A* (A-star) algorithm is one of the most popular and powerful pathfinding algorithms used for finding the shortest path between a start and a target point, particularly in grid-based maps. It's an informed search algorithm, meaning it uses both the actual cost to reach a point and an estimated cost to reach the goal from that point. The A* algorithm combines the advantages of Dijkstra's Algorithm (which finds the shortest path) and Greedy Best-First Search (which uses a heuristic to guide the search).

#Key Concepts in A* Algorithm:
# 1 - g(n): The cost to reach the current node n from the start node.
# 2 - h(n): A heuristic estimate of the cost to reach the goal from node n (often referred to as the "heuristic").
# 3 - f(n) = g(n) + h(n): The total estimated cost of the cheapest solution through n, which is used to prioritize the nodes in the open set (priority queue).
# 3.1 - f(n) is used to determine which node to explore next. The node with the lowest f(n) value is chosen for exploration.
# 4 - Open Set: A priority queue (often implemented as a min-heap) that stores nodes yet to be evaluated.
# 5 - Closed Set: A set of nodes that have already been evaluated.

#Algorithm Steps:
# 1 - Initialize:
# 1.1 - Put the start node in the open set and initialize g(start) = 0.
# 1.2 - Set the heuristic value h(start) (using an admissible heuristic, typically the straight-line distance or Manhattan distance).
# 1.3 - Set f(start) = g(start) + h(start).
# 2 - Main Loop:
# 2.1 - While there are nodes in the open set:
# 2.2 - Pick the node n from the open set with the lowest f(n) value.
# 2.3 - If n is the target node, backtrack through the parent nodes to reconstruct the path.
# 2.4 - Otherwise, move n to the closed set (since it has been processed).
# 2.5 - For each neighbor m of n:
# 2.6 - If m is in the closed set, skip it.
# 2.7 - If m is not in the open set, calculate its f(m), g(m), and h(m) values, and add it to the open set with n as its parent.
#2.8 - If m is already in the open set, check if the new g(m) is lower; if so, update the cost and parent.
# 3 - Stop Condition:
# 3.1 - If the target node is found, reconstruct the path from the target to the start node by backtracking through parent nodes.
# 3.2 - If the open set is empty and no path is found, return that no path exists.

#A* Algorithm in Python:

import heapq

# Define possible movements (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Check if a cell is within the grid bounds and not blocked
def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

# A* algorithm to find the shortest path
def a_star_algorithm(grid, start, target):
    # Grid dimensions
    rows, cols = len(grid), len(grid[0])
    
    # Open set: priority queue of nodes to explore
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, target), 0, start))  # (f, g, node)
    
    # Closed set: nodes already evaluated
    came_from = {}  # To reconstruct the path
    g_score = {start: 0}  # g(n): cost to reach node n
    f_score = {start: heuristic(start, target)}  # f(n): estimated cost (g + h)
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        
        # If we've reached the target
        if current == target:
            # Reconstruct path by backtracking through 'came_from'
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Explore neighbors
        for dx, dy in MOVES:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if is_valid(neighbor[0], neighbor[1], grid):
                tentative_g_score = current_g + 1  # All moves have a cost of 1
                
                # If this path to the neighbor is better
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, target)
                    heapq.heappush(open_set, (f_score[neighbor], tentative_g_score, neighbor))
    
    # If no path is found
    return None

# Example grid: 0 = free space, 1 = blocked cell
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting point (row, col)
target = (4, 4)  # Target point (row, col)

# Run A* Algorithm
path = a_star_algorithm(grid, start, target)

if path:
    print("Path found:", path)
else:
    print("No path found.")

#Explanation of Code:
# 1 - Heuristic Function:
# 1.1 - Here, we use Manhattan distance as the heuristic. This is the sum of the absolute differences between the x and y coordinates of two points.
# 1.2 - For example, the heuristic between (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
# 2 - Open Set:
# 2.1 - The open set is implemented using a priority queue (heapq), which stores nodes with the lowest f(n) at the front. The node's f(n) value is the sum of its actual cost (g(n)) and the heuristic estimate (h(n)).
# 3 - Main Loop:
# 3.1 - The loop continues until we find the target or exhaust the open set.
# 3.2 - The node with the lowest f(n) is popped from the open set, and its neighbors are explored.
# 4 - Reconstructing the Path:
# 4.1 - If the target node is reached, we backtrack using the came_from dictionary, which stores the parent of each node.
# 4.2 - This backtracking gives the path from the target to the start, which is then reversed to show the path from the start to the target.
# 5 - Stopping Condition:
# 5.1 - If the open set is empty and no path is found, the function returns None.

#Example Output:
#For the provided grid, the output would be:
#Path found: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
#This means the shortest path from (0, 0) to (4, 4) is the sequence of coordinates shown in the list.

#Summary:
# 1 - A* Algorithm is an efficient and flexible pathfinding algorithm.
# 2 - It combines Dijkstra's Algorithm for optimality and Greedy Best-First Search for speed by using a heuristic function.
# 3 - The algorithm guarantees finding the shortest path in grids or graphs with an appropriate heuristic, like Manhattan or Euclidean distance.
