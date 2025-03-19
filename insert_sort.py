##Insertion Sort is a simple and intuitive sorting algorithm. It builds the sorted array one element at a time by repeatedly picking the next element from the unsorted part of the list and inserting it into its correct position in the sorted part of the list.

##Here’s how Insertion Sort works:
## 1 - Start from the second element in the array (since the first element is already considered "sorted").
## 2 - Compare the current element with the element before it (starting from the second element).
## 3 - If the current element is smaller than the element before it, shift the element to the right.
## 4 - Repeat this process until the current element finds its correct position in the sorted part of the array.
## 5 - Continue this process for each element in the array.

##Python Code for Insertion Sort:
def insertion_sort(arr):
    # Iterate over each element in the array (starting from the second element)
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        current_element = arr[i]
        
        # Initialize the position to compare with the element before it
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than current_element
        # to one position ahead of their current position
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        
        # Insert the current element at its correct position
        arr[j + 1] = current_element
        
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
print("Original Array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted Array:", sorted_arr)

##How It Works:
## 1 - First Pass: The element 11 is compared with 12. Since 11 is smaller, it is placed before 12.
## 1.1 - Array after this pass: [11, 12, 13, 5, 6]
## 2 - Second Pass: The element 13 is compared with 12 (no change needed since 13 is already larger).
## 2.1 - Array after this pass: [11, 12, 13, 5, 6]
## 3 - Third Pass: The element 5 is compared with 13, 12, and 11 and is placed in the correct position.
## 3.1 - Array after this pass: [5, 11, 12, 13, 6]
## 4 - Fourth Pass: The element 6 is compared with 13, 12, and 11 and is placed in the correct position.
## 4.1 - Final sorted array: [5, 6, 11, 12, 13]

##Time Complexity:
##Best case: When the array is already sorted, the time complexity is O(n) because the algorithm only needs to pass through the array once.
##Worst case: When the array is in reverse order, the time complexity is O(n²) because for each element, we need to shift all the previous elements.
##Average case: The time complexity is also O(n²).
