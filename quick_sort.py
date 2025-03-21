#QuickSort is a divide-and-conquer algorithm that works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

#Here’s how the QuickSort algorithm works step-by-step:

#Steps:
# 1 - Pick a pivot: Choose an element from the array to be the pivot. The choice of pivot can be the first element, the last element, the middle element, or a random element.
# 2 - Partition the array: Rearrange the array so that elements smaller than the pivot come before it, and elements larger than the pivot come after it. The pivot element is then in its final position.
# 3 - Recursively apply the same process: Apply the above steps to the sub-arrays (elements before the pivot and elements after the pivot).

#Python Code Implementation:

def quicksort(arr):
    # Base case: if the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here we choose the last element as pivot)
    pivot = arr[-1]
    
    # Partition step: Create sub-arrays for elements less than and greater than the pivot
    left = [x for x in arr[:-1] if x <= pivot]  # elements <= pivot
    right = [x for x in arr[:-1] if x > pivot]  # elements > pivot
    
    # Recursively sort the sub-arrays and concatenate with the pivot
    return quicksort(left) + [pivot] + quicksort(right)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)

#Explanation of Code:
# 1 - Base Case: If the array has zero or one element, it's already sorted, so it is returned as is.
# 2 - Pivot Selection: We pick the last element as the pivot (arr[-1]).
# 3 - Partitioning:
# 3.1 - left: All elements less than or equal to the pivot.
# 3.2 - right: All elements greater than the pivot.
# 4 - Recursive Sorting: The quicksort function is called recursively on the left and right sub-arrays.
#Concatenation: The sorted left sub-array, pivot, and sorted right sub-array are combined and returned.

#Example:
#For the array [10, 7, 8, 9, 1, 5], the algorithm would proceed as follows:
# 1 - Select 5 as the pivot.
# 2 - Partition into left = [1] and right = [10, 7, 8, 9].
# 3 - Recursively sort left and right.
# 4 - Combine sorted sub-arrays and pivot: [1] + [5] + [7, 8, 9, 10].

#Time Complexity:
#Best case: O(n log n)
#Average case: O(n log n)
#Worst case: O(n^2) (occurs when the pivot is the smallest or largest element, resulting in unbalanced partitions)
