#The Lee Algorithm is a pathfinding algorithm used primarily for finding the shortest path in a grid-like environment. It is commonly employed in robot navigation, routing, and other applications that require navigating a grid. Lee's algorithm is a breadth-first search (BFS) algorithm, so it guarantees finding the shortest path in an unweighted grid.

#Key Features:
# 1 - Unweighted Grid: The algorithm works on grids where the cost of moving from one cell to another is uniform.
# 2 - Breadth-First Search (BFS): Since it uses BFS, it explores all possible nodes level by level.
# 3 - Shortest Path: It guarantees the shortest path in terms of the number of steps required to go from the start node to the target node.

#Steps in Lee's Algorithm:
#Initialize:
# 1.1 - Mark all cells as unvisited except the starting point.
# 1.2 - Create a queue to hold the cells to be explored, starting with the source cell.
# 1.3 - Mark the distance from the source cell as 0 and initialize other cells with infinity (inf).
# 2 - Explore Neighbors:
# 2.1 - While the queue is not empty, pop a cell from the queue.
# 2.2 - Explore its neighbors (up, down, left, right).
# 2.3 - If a neighbor has not been visited yet, mark it with the correct distance (current cell's distance + 1) and add it to the queue.
# 3 - Stop Condition:
# 3.1 - The algorithm stops if the target cell is reached, or all reachable cells are visited.
# 4 - Backtrack to Find the Path:
# 4.1 - If the target is reached, backtrack from the target to the source using the distance values to reconstruct the path.

#Example in Python:
#Here's how you can implement Lee’s algorithm in Python:

from collections import deque

# Define possible movements (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to check if a cell is within the grid bounds and not blocked
def is_valid(x, y, grid, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

# Lee's Algorithm to find the shortest path
def lee_algorithm(grid, start, target):
    # Grid dimensions
    rows, cols = len(grid), len(grid[0])
    
    # Initialize visited array and distance array
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    
    # Queue for BFS
    queue = deque([start])
    visited[start[0]][start[1]] = True
    distance[start[0]][start[1]] = 0
    
    # Perform BFS
    while queue:
        x, y = queue.popleft()
        
        # If we reach the target, return the distance
        if (x, y) == target:
            return distance[x][y]
        
        # Explore all 4 possible moves
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid, visited):
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    # If there's no path to the target, return -1
    return -1

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

# Run the Lee's Algorithm
shortest_distance = lee_algorithm(grid, start, target)

if shortest_distance != -1:
    print(f"The shortest path length is: {shortest_distance}")
else:
    print("No path found.")

#Explanation:
# 1 - Grid Representation: The grid is represented as a 2D list, where 0 represents an open cell (free space), and 1 represents a blocked cell.
# 2 - Queue Initialization: The algorithm starts with the source cell and explores all possible neighboring cells. The distance to each cell is updated as we explore it.
# 3 - Neighbor Exploration: We check all four neighboring cells (up, down, left, right), making sure the new cell is valid (inside the grid, not blocked, and not visited before).
# 4 - Distance Tracking: The distance is incremented each time we move to a valid neighboring cell.
# 5 - Termination: If the target is found, the distance is returned; otherwise, it returns -1 indicating no path exists.

#Example Output:
#For the provided grid, the output would be:
The shortest path length is: 8
This means the shortest path from (0, 0) to (4, 4) consists of 8 steps.
