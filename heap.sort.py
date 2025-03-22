#Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It works by first converting the list into a max-heap, where the largest element is at the root, and then repeatedly swapping the root (the largest element) with the last element in the heap and reducing the heap size. After each swap, it "heapifies" the reduced heap to restore the max-heap property. The algorithm sorts the list in-place, meaning it doesn't require any additional storage other than the input list.

#Steps of Heap Sort:
# 1 - Build a max-heap from the unsorted input list. A max-heap is a binary tree where each parent node is greater than or equal to its children.
# 2 - Extract the root (largest element) from the heap and swap it with the last element of the heap.
# 3 - Reduce the heap size by excluding the last element (since it's now sorted).
# 4 - Heapify the reduced heap to maintain the max-heap property.
# 5 - Repeat steps 2 to 4 until the heap size is reduced to 1.

#Python Implementation of Heap Sort:

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current root to end
        heapify(arr, i, 0)  # Heapify the root element

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)

#Explanation:
# 1 - heapify(): This function ensures that a subtree with root at index i satisfies the max-heap property. It compares the root with its left and right children and swaps if necessary.
# 2 - heap_sort(): First, it builds the max-heap by calling heapify() for all internal nodes (starting from the last non-leaf node). Then it extracts the root (the largest element) and reduces the heap size by one, repeatedly calling heapify() to restore the heap property.

#Time Complexity:
#Building the heap takes O(n).
#Extracting the root and heapifying takes O(logn) for each element, and there are O(nlogn).

#Space Complexity:
#Heap Sort is done in-place, so the space complexity is O(1).

#Example:
#For the input array [12, 11, 13, 5, 6, 7], the sorted array output will be:
#Sorted array is: [5, 6, 7, 11, 12, 13]
