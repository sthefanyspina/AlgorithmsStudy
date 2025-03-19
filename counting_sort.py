#Counting Sort is a non-comparative sorting algorithm that works by counting the occurrences of each unique element in the input array. This method is particularly efficient when the range of input values is small relative to the number of elements in the array.

#Here's a step-by-step explanation of how Counting Sort works:
# 1 - Input: You are given an array of integers.
# 2 - Find the Range: First, find the maximum value (max_val) in the array to determine the range of values.
# 3 - Count Frequencies: Create a frequency array (or count array), where each index represents a number in the input array. The value at each index indicates how many times that number appears in the input.
# 4 - Accumulate Counts: Modify the count array so that each index holds the cumulative sum of the previous counts. This allows for the correct positioning of each element in the sorted output.
# 5 - Place Elements: Finally, construct the sorted output array by placing each element in its correct position according to the accumulated counts.

#Steps:
# 1 - Create a count array that stores the count of each element in the input array.
# 2 - Modify the count array to store the cumulative count.
# 3 - Build the sorted array by placing elements according to the cumulative count.

#Python Code Example:

def counting_sort(arr):
    # Step 1: Find the maximum value in the array to determine the range
    max_val = max(arr)
    min_val = min(arr)
    
    # Step 2: Initialize the count array with zeros
    count_range = max_val - min_val + 1
    count = [0] * count_range
    output = [0] * len(arr)
    
    # Step 3: Count occurrences of each element in the input array
    for num in arr:
        count[num - min_val] += 1
    
    # Step 4: Modify the count array to store the cumulative count
    for i in range(1, count_range):
        count[i] += count[i - 1]
    
    # Step 5: Build the sorted output array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted Array:", sorted_arr)

#Explanation of the Code:
#Step 1: We find the maximum and minimum values in the input array arr to determine the range of numbers.
#Step 2: We create a count array where each index corresponds to the difference between the element value and the minimum value, storing the frequency of each element.
#Step 3: We fill the count array with the frequency of each element.
#Step 4: We convert the count array into a cumulative count array.
#Step 5: We place the elements into the output array based on the cumulative counts.

#Time Complexity:
#Best, Average, and Worst Case: O(n + k), where n is the number of elements in the array, and k is the range of the input (i.e., the difference between the maximum and minimum values).
#O(n) for counting the occurrences and placing the elements.
#O(k) for filling and processing the count array.

#Space Complexity:
#O(n + k), where n is the size of the input array, and k is the range of input values (difference between the maximum and minimum values).
