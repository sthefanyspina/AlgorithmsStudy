#The Convex Hull of a set of points is the smallest convex polygon that encloses all the points in the set. In computational geometry, finding the convex hull is a fundamental problem with applications in computer graphics, pathfinding, and more.
#Several algorithms can be used to compute the convex hull of a set of points. Some of the most well-known ones are:
# 1 - Graham's Scan Algorithm
# 2 - Jarvis's March (Gift Wrapping)
# 3 - QuickHull Algorithm
# 4 - Divide and Conquer

#1. Graham's Scan Algorithm
#This algorithm sorts the points and then constructs the convex hull by processing them in sorted order. It works in O(n log n) time due to sorting.

#Steps:
# 1 - Sort the points based on the polar angle with respect to a pivot (typically the point with the lowest y-coordinate).
# 2 - Process the points in sorted order and maintain a stack of points that represent the current convex hull.

Python Code:

import matplotlib.pyplot as plt

def orientation(p, q, r):
    # Returns the orientation of the triplet (p, q, r)
    # 0 -> p, q and r are collinear
    # 1 -> Clockwise
    # 2 -> Counterclockwise
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def graham_scan(points):
    # Sort the points by polar angle
    points = sorted(points, key=lambda x: (x[0], x[1]))
    # Build the convex hull
    hull = []
    
    for point in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) != 2:
            hull.pop()
        hull.append(point)
    
    return hull

# Example usage:
points = [(0, 0), (2, 2), (1, 1), (3, 3), (4, 4), (2, 3)]
hull = graham_scan(points)

# Plot the points and the convex hull
x, y = zip(*points)
hx, hy = zip(*hull)
plt.plot(x, y, 'bo', label="Points")
plt.plot(hx + (hx[0],), hy + (hy[0],), 'r-', label="Convex Hull")
plt.legend()
plt.show()

#2. Jarvis's March (Gift Wrapping)
#This algorithm works by starting at the leftmost point and wrapping around the points in a counterclockwise direction. It’s like "gift-wrapping" the points around the hull.

Python Code:

def jarvis_march(points):
    # Find the leftmost point
    leftmost = min(points, key=lambda x: x[0])
    hull = []
    p = leftmost

    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            if orientation(p, q, r) == 2:
                q = r
        p = q
        if p == leftmost:
            break
    
    return hull

# Example usage:
hull = jarvis_march(points)

# Plot the points and the convex hull
hx, hy = zip(*hull)
plt.plot(x, y, 'bo', label="Points")
plt.plot(hx + (hx[0],), hy + (hy[0],), 'r-', label="Convex Hull")
plt.legend()
plt.show()

#3. QuickHull Algorithm
#QuickHull is similar to QuickSort in terms of its divide-and-conquer approach. It divides the set of points by finding the farthest points from a line, and recursively computes the convex hull for the divided parts.

Python Code:

def quickhull(points):
    def orientation(p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def distance(p, q, r):
        return abs((r[1] - p[1]) * (q[0] - p[0]) - (r[0] - p[0]) * (q[1] - p[1]))

    def find_hull(points, p, q):
        if not points:
            return []
        farthest_point = max(points, key=lambda r: distance(p, q, r))
        points.remove(farthest_point)
        left_of_line1 = [r for r in points if orientation(p, farthest_point, r) > 0]
        left_of_line2 = [r for r in points if orientation(farthest_point, q, r) > 0]
        return find_hull(left_of_line1, p, farthest_point) + [farthest_point] + find_hull(left_of_line2, farthest_point, q)

    points = list(set(points))
    leftmost = min(points, key=lambda x: x[0])
    rightmost = max(points, key=lambda x: x[0])
    points.remove(leftmost)
    points.remove(rightmost)

    upper_hull = find_hull(points[:], leftmost, rightmost)
    lower_hull = find_hull(points[:], rightmost, leftmost)

    return [leftmost] + upper_hull + [rightmost] + lower_hull

# Example usage:
hull = quickhull(points)

# Plot the points and the convex hull
hx, hy = zip(*hull)
plt.plot(x, y, 'bo', label="Points")
plt.plot(hx + (hx[0],), hy + (hy[0],), 'r-', label="Convex Hull")
plt.legend()
plt.show()

#4. Divide and Conquer Algorithm
#This algorithm works by recursively dividing the points into halves, computing the convex hulls for each half, and merging the hulls.

#Summary of Complexity:
# 1 - Graham's Scan: O(n log n)
# 2 - Jarvis’s March (Gift Wrapping): O(nh) (where h is the number of points in the convex hull)
# 3 - QuickHull: O(n log n) on average, but can be O(n²) in the worst case.
# 4 - Divide and Conquer: O(n log n)

#Conclusion:
#Graham's Scan and Divide and Conquer are the most efficient algorithms for computing the convex hull in terms of time complexity (O(n log n)).
#Jarvis's March is simpler but can be slower, especially when the number of points in the convex hull (h) is large.
#QuickHull performs well in practice but may degrade in some cases to O(n²).
