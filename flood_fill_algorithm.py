#The Flood Fill Algorithm is used to fill a connected region in a grid with a specific color or value. It’s often seen in applications like paint programs where you "fill" an area with a chosen color.
#The algorithm works by starting at a specific point (the "seed") and expanding out to neighboring points (typically, in 4 directions: up, down, left, right) until a boundary is reached, filling the area along the way. It can be implemented using Depth-First Search (DFS) or Breadth-First Search (BFS). Here, I'll show an example of how to implement it using DFS.

#Flood Fill Algorithm in Python using DFS:

def flood_fill(grid, x, y, new_color):
    # Check if the current coordinates are out of bounds
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return
    
    # Get the original color of the starting point
    original_color = grid[x][y]
    
    # If the color to fill is the same as the original color, no need to proceed
    if original_color == new_color:
        return
    
    # Define the helper function for DFS
    def dfs(x, y):
        # If current position is out of bounds or already filled with new color, return
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] != original_color:
            return
        
        # Fill the current cell with the new color
        grid[x][y] = new_color
        
        # Recursively visit the neighboring cells (4 directions)
        dfs(x + 1, y)  # down
        dfs(x - 1, y)  # up
        dfs(x, y + 1)  # right
        dfs(x, y - 1)  # left
    
    # Call DFS starting from the given point (x, y)
    dfs(x, y)

# Example usage
grid = [
    [1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1]
]

# Before flood fill
for row in grid:
    print(row)

# Start flood fill from position (0, 0) with new color 2
flood_fill(grid, 0, 0, 2)

# After flood fill
print("\nAfter flood fill:")
for row in grid:
    print(row)

#Explanation:
# 1 - Base Case: The function first checks if the current coordinates are out of bounds or if the color at the current position is different from the original color. If so, it stops the recursion.
# 2 - Color Filling: Once the algorithm identifies a position that matches the original color, it fills that cell with the new color.
# 3 - Recursion: The DFS function recursively visits neighboring cells in the grid (up, down, left, right), thus filling the connected region.
# 4 - Termination: The recursion ends once all connected cells of the original color have been filled with the new color.

#Example Output:
#Before flood fill:
[1, 1, 1, 0, 0]
[1, 1, 0, 0, 0]
[1, 0, 1, 1, 0]
[0, 0, 1, 1, 1]
#After flood fill (starting at (0, 0) with color 2):
[2, 2, 2, 0, 0]
[2, 2, 0, 0, 0]
[2, 0, 1, 1, 0]
[0, 0, 1, 1, 1]

#Notes:
#You can modify this to use BFS (breadth-first search) by using a queue instead of recursion if desired.
#The grid here is represented by a 2D list, where each cell is an integer that represents a color or value.
