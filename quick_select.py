##Quickselect is an efficient algorithm for finding the k-th smallest (or largest) element in an unordered list. It is related to the Quicksort algorithm and operates by partially sorting the array to locate the desired element, making it faster than fully sorting the array when only the k-th element is needed.

##How Quickselect Works:
## 1 - Partitioning:
## 1.1 - Select a pivot element from the array.
## 1.2 - Rearrange the array so that all elements less than the pivot come before it, and all elements greater than the pivot come after it. This step places the pivot in its correct position if the array were sorted.

##Selection:
## 1 -Determine the position of the pivot in the array.
## 2 - If the pivot's position matches the desired k-th index, return the pivot as the result.
## 3 - If the pivot's position is greater than k, recursively apply Quickselect to the left subarray (elements less than the pivot).
## 4 - If the pivot's position is less than k, recursively apply Quickselect to the right subarray (elements greater than the pivot), adjusting k accordingly.
## This process continues until the k-th smallest element is found.

##Python Implementation:

import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)
    return None

# Example usage:
arr = [7, 10, 4, 3, 20, 15]
k = 3  # Find the 3rd smallest element
result = quickselect(arr, 0, len(arr) - 1, k - 1)  # k-1 for zero-based index
print(f"The {k}rd smallest element is: {result}")

##Output:
##The 3rd smallest element is: 7

##Explanation:
##In the array [7, 10, 4, 3, 20, 15], the 3rd smallest element is 7.
##We adjust k by subtracting 1 because Python uses zero-based indexing.

##Time Complexity:
##Average Case: O(n), where n is the number of elements in the array.
##Worst Case: O(n²), which occurs when the pivot selection is consistently poor (e.g., always picking the smallest or largest element as the pivot).
