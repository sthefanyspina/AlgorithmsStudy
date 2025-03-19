##Step-by-Step Approach:
## 1 -Initialize three pointers: prev, current, and next.
## 2 - Iterate through the list:
## 2.1 - Store the next node (next = current.next).
## 2.2 - Reverse the current node's next pointer (current.next = prev).
## 2.3 - Move the prev and current pointers one step forward.
## 3 - Repeat until the list is reversed.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Function to print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev and current one step forward
            current = next_node
        self.head = prev  # Set the head to the new first node

# Example usage:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Original List:")
llist.print_list()

llist.reverse()

print("Reversed List:")
llist.print_list()

##Explanation:
##The append function adds nodes to the linked list.
##The print_list function prints the linked list.
##The reverse function reverses the linked list by adjusting the next pointers.
