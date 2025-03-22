#Merge Sort is a divide-and-conquer sorting algorithm that divides the array into two halves, recursively sorts each half, and then merges the sorted halves together. It's a very efficient algorithm, with a time complexity of 𝑂(𝑛log𝑛).

#Here's how Merge Sort works:
# 1 - Divide: Split the array into two halves until each subarray has only one element.
# 2 - Conquer: Recursively sort each subarray.
# 3 - Combine: Merge the sorted subarrays back together to form a single sorted array.

#Python implementation:

def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide: Find the middle point and split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine: Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    # Merge two sorted arrays into a single sorted array
    sorted_arr = []
    i = j = 0
    
    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # If there are remaining elements in either half, append them
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

#How It Works:
#merge_sort(arr): This function takes an unsorted array arr and:
#If the array has 1 or 0 elements, it returns the array (since it's already sorted).
#Otherwise, it splits the array into two halves (left_half and right_half).
#It then recursively sorts each half by calling merge_sort() on them.
#merge(left, right): This function merges two sorted subarrays (left and right) into a single sorted array:
#It compares the first elements of both subarrays and adds the smaller one to sorted_arr.
#It continues comparing and adding elements until all elements from both subarrays are placed in sorted_arr.

#Example Usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)

Output:
[3, 9, 10, 27, 38, 43, 82]

#Time Complexity:
#Best case: O(nlogn)
#Average case: O(nlogn)
#Worst case: O(nlogn)
