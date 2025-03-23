#The Dutch National Flag Algorithm is an efficient sorting algorithm used to sort an array of three distinct values (often 0, 1, and 2). It was proposed by Edsger Dijkstra, and the main idea is to classify the elements into three categories and sort them in a single pass using a three-way partitioning technique.

#Problem Definition:
# 1 - Given an array with elements from the set {0, 1, 2}, the task is to sort the array such that:
# 1.1 - All 0s are moved to the beginning of the array,
# 1.2 - All 1s come in the middle, and
# 1.3 - All 2s are placed at the end of the array.

#How it works:
# 1 - The algorithm maintains three pointers:
# 1.1 - low: The boundary for the 0s.
# 1.2 - mid: The boundary for the 1s.
# 1.3 - high: The boundary for the 2s.
# 2 - We iterate through the array with the mid pointer, and based on the value at arr[mid], we perform different operations:
# 2.1 - If arr[mid] == 0, we swap it with arr[low] and move both low and mid pointers forward.
# 2.2 - If arr[mid] == 1, we simply move the mid pointer forward.
# 2.3 - If arr[mid] == 2, we swap it with arr[high] and move the high pointer backward.
#This way, we categorize elements into three sections (0s, 1s, and 2s) in a single pass through the array.

#Dutch National Flag Algorithm in Python:

def dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[low] and arr[mid] and move both pointers
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # If it's 1, just move the mid pointer
            mid += 1
        else:  # arr[mid] == 2
            # Swap arr[mid] and arr[high] and move high pointer
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage
arr = [0, 1, 2, 1, 0, 2, 1, 0, 2]
print("Before Sorting:", arr)
sorted_arr = dutch_national_flag(arr)
print("After Sorting:", sorted_arr)

#Explanation of the Code:
# 1 - Initialization: We start by initializing three pointers:
# 1.1 - low starts at the beginning of the array (index 0),
# 1.2 - mid starts at the beginning of the array (index 0),
# 1.3 - high starts at the end of the array (index len(arr) - 1).
# 2 - Main Loop: We continue to process the array until mid is greater than high.
# 2.1 - If arr[mid] == 0: Swap the elements at low and mid, then increment both low and mid.
# 2.2 - If arr[mid] == 1: Simply increment mid to move to the next element.
# 2.3 - If arr[mid] == 2: Swap the elements at mid and high, then decrement high. We do not increment mid in this case because we haven't processed the new element at arr[mid] after the swap.

#Time Complexity:
#Time Complexity: O(n), where n is the length of the array. The algorithm only makes a single pass through the array.
#Space Complexity: O(1), since we are sorting the array in place without using any extra space (other than a few pointers).

#Example Execution:
#For the input array [0, 1, 2, 1, 0, 2, 1, 0, 2], the algorithm will perform the following steps:
# 1 - Initial array: [0, 1, 2, 1, 0, 2, 1, 0, 2]
# 2 - Swap 0 and arr[low] → [0, 1, 2, 1, 0, 2, 1, 0, 2] (no change).
# 2.1 - low = 1, mid = 1, high = 8
# 3 - Swap 1 and arr[mid] → [0, 1, 2, 1, 0, 2, 1, 0, 2].
# 3.1 - mid = 2.
# 4 - Swap 2 and arr[high] → [0, 1, 2, 0, 0, 2, 1, 1, 2].
# 4.1 - high = 7.
# 5 - Continue processing until array is sorted.
#Final sorted array: [0, 0, 0, 1, 1, 1, 2, 2, 2].

#Advantages:
# 1 - Efficient: The algorithm runs in linear time, O(n), and does not require extra space beyond a few variables.
# 2 - In-place: No additional memory is needed, as the sorting is done in place.
