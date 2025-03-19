##Binary search is a highly efficient algorithm for finding an item from a sorted list (or array) by repeatedly dividing the search interval in half. If the value of the target is less than the value in the middle of the interval, the search continues in the left half, otherwise, it continues in the right half. This process is repeated until the value is found or the interval is empty.

##Steps of Binary Search:
## 1 - Start with the entire sorted array.
## 2 - Find the middle element.
## 3 - If the target element is equal to the middle element, return its index.
## 4 - If the target is smaller than the middle element, search in the left half.
## 5 - If the target is larger than the middle element, search in the right half.
## 6 - Repeat this process until the target is found or the search interval is empty (indicating the target is not in the array).

##Time Complexity:
##O(log n): This is because the search space is halved with each step, making it very efficient for large datasets.

##Example in Python:

def binary_search(arr, target):
    # Define the start and end of the search range
    low = 0
    high = len(arr) - 1

    # Loop until the search range is valid
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Target found, return index
        # If the target is smaller, search in the left half
        elif arr[mid] > target:
            high = mid - 1
        # If the target is larger, search in the right half
        else:
            low = mid + 1

    # Target not found
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")


##Explanation:
## 1 - low and high track the bounds of the search range.
## 2 - The mid index is recalculated in each loop iteration.
## 3 - The algorithm compares the middle element (arr[mid]) with the target:
## 3.1 - If they are equal, the function returns the index (mid).
## 3.2 - If the middle element is greater than the target, the algorithm searches the left half by setting high to mid - 1.
## 3.3 - If the middle element is less than the target, the algorithm searches the right half by setting low to mid + 1.
## 4 - If the target is not found by the time low exceeds high, the function returns -1 to indicate the target is not in the list.

##Example Output:
##Element 7 found at index 3

##When to Use Binary Search:
##Sorted Data: Binary search only works on sorted data. If the data is unsorted, you'll need to sort it first (which could take time, O(n log n), depending on the sorting algorithm).
##Efficient Searching: It is much faster than linear search for large datasets due to its logarithmic time complexity.
