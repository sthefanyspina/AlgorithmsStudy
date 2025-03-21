#Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The algorithm gets its name because smaller elements "bubble" to the top of the list (beginning), while larger elements "sink" to the bottom (end).

#How Bubble Sort Works:
# 1 - Start from the beginning of the list.
# 2 - Compare adjacent elements (i.e., compare the first element with the second, the second with the third, and so on).
# 3 - If the first element is larger than the second element, swap them.
# 4 - Continue this process for the entire list, which will ensure that the largest element is "bubbled" to the end of the list.
# 5 - Repeat the process for the remaining unsorted part of the list (ignoring the already sorted part at the end).
# 6 - The process stops when no more swaps are needed, meaning the list is sorted.

Bubble Sort Example in Python:

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Set a flag to optimize and break early if no swaps were made
        swapped = False
        
        # Last i elements are already sorted, so no need to check them
        for j in range(0, n-i-1):
            # Compare the adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, the list is sorted
        if not swapped:
            break
    
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))

#Explanation:
# 1 - Outer loop (for i in range(n)): This loop controls the number of passes through the list.
# 2 - Inner loop (for j in range(0, n-i-1)): This loop performs comparisons between adjacent elements in the unsorted portion of the list. After each pass, the largest element "bubbles up" to the correct position at the end.
# 3 - Swapping condition (if arr[j] > arr[j+1]): If the current element is greater than the next one, they are swapped.
# 4 - Optimization with swapped flag: If no elements were swapped in a pass (i.e., the list is already sorted), the algorithm can terminate early, saving unnecessary passes.

#Time Complexity:
#Worst-case time complexity: O(n²) – occurs when the list is sorted in reverse order.
#Best-case time complexity: O(n) – occurs when the list is already sorted, and the algorithm can stop early.
#Average-case time complexity: O(n²).
