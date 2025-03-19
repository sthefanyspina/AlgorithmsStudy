#Selection Sort is a simple sorting algorithm that works by repeatedly finding the minimum (or maximum, depending on the order) element from an unsorted portion of the list and swapping it with the first unsorted element.

#Algorithm Explanation:
# 1 - Start with the first element of the list.
# 2 - Find the smallest element in the remaining unsorted portion of the list.
# 3 - Swap this smallest element with the first unsorted element.
# 4 - Move the boundary of the unsorted portion one step forward.
# 5 - Repeat the process until the entire list is sorted.

#Selection Sort in Python:

def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements of the array
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

#Steps:
# 1 - Outer loop (for i in range(n)): This loop traverses through each element in the list, treating it as the starting point of the unsorted portion.
# 2 - Inner loop (for j in range(i+1, n)): This loop looks for the smallest element in the unsorted portion of the list.
# 3 - Find minimum: Compare each element to find the smallest.
# 4 - Swap: Once the smallest element is found, swap it with the element at the current index i.

#Example:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)

Output:
[11, 12, 22, 25, 64]

#Time Complexity:
#Best, Average, Worst Case: O(n^2) because there are two nested loops that iterate through the array. The inner loop runs n−i times for each outer loop iteration.

#Space Complexity:
#O(1): It’s an in-place sorting algorithm because it doesn't require any extra memory beyond the input array.
