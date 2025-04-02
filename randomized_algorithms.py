#Randomized Algorithms are a class of algorithms that make use of random numbers or random choices to solve a problem. These algorithms use randomness to either:
# 1 - Make decisions during the computation process.
# 2 - Choose between different possibilities in a non-deterministic way.

#In Python, this randomness can be handled using the random module, which provides functions for generating random numbers and selecting random elements. Randomized algorithms can be especially useful when solving problems that are difficult or inefficient to solve with deterministic algorithms.

#Key Types of Randomized Algorithms:
# 1 - Las Vegas Algorithms: These always produce the correct result, but the runtime is a random variable. The algorithm might run longer or shorter depending on the random choices made during execution. The expectation is that the expected runtime is efficient.
# 2 - Monte Carlo Algorithms: These might give an incorrect result with a small probability, but they always run in a predictable time. The error can be reduced by running the algorithm multiple times or increasing the sample size.
# 3 - Randomized Data Structures: Some data structures can use randomness to improve performance, like hash tables with random hashing or randomized trees.

#Example 1: Randomized QuickSort (Las Vegas)
#One of the classic examples of a randomized algorithm is Randomized QuickSort, which randomly selects a pivot element to partition the array instead of choosing a fixed pivot.

import random

def randomized_quick_sort(arr):
    # Base case: If the array is empty or contains a single element, it's sorted
    if len(arr) <= 1:
        return arr
    
    # Randomly choose a pivot and swap it with the first element
    pivot_index = random.randint(0, len(arr) - 1)
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    
    # Partition the array into two parts: less than pivot and greater than pivot
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    # Recursively sort the partitions
    return randomized_quick_sort(less) + [pivot] + randomized_quick_sort(greater)

# Test the algorithm
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = randomized_quick_sort(arr)
print("Sorted array:", sorted_arr)

#Example 2: Monte Carlo Algorithm - Estimating Pi
#A common Monte Carlo approach is using random sampling to estimate values, like estimating the value of π.
#The idea is to randomly throw points onto a square and count how many fall inside a circle inscribed within that square. The ratio of points inside the circle to the total points can be used to estimate π.

import random

def estimate_pi(num_points):
    inside_circle = 0
    
    for _ in range(num_points):
        x = random.random()  # random x-coordinate between 0 and 1
        y = random.random()  # random y-coordinate between 0 and 1
        
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    # The ratio of points inside the circle to total points approximates π/4
    return (inside_circle / num_points) * 4

# Test the algorithm
pi_estimate = estimate_pi(1000000)
print("Estimated value of Pi:", pi_estimate)

#Example 3: Randomized Algorithms for Searching (Monte Carlo)
#Let's consider a simple Monte Carlo approach to searching for a target in an array, where we randomly pick elements and check if they match the target. It’s not guaranteed to find the target, but it might give a result quicker than a brute-force search for certain inputs.

import random

def monte_carlo_search(arr, target, num_trials):
    for _ in range(num_trials):
        index = random.randint(0, len(arr) - 1)
        if arr[index] == target:
            return True
    return False

# Test the algorithm
arr = [5, 2, 7, 1, 8, 3]
target = 7
result = monte_carlo_search(arr, target, 1000)
print("Found target:", result)

#Advantages of Randomized Algorithms:
# 1 - Simplicity: Many randomized algorithms are simple to implement.
# 2 - Efficiency: They can have better expected time complexity than deterministic algorithms for certain problems.
# 3 - Good Average-Case Performance: They often perform well on average, even if the worst-case performance is not optimal.

#Disadvantages of Randomized Algorithms:
# 1 - Uncertainty: The randomness introduces unpredictability in the algorithm’s performance, and sometimes it might not work as expected.
# 2 - Error Probability: For Monte Carlo algorithms, there’s a non-zero chance of getting incorrect results. For Las Vegas algorithms, you may have longer running times in some cases.
