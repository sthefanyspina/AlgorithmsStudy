##The Floyd Cycle Detection Algorithm, also known as Floyd's Tortoise and Hare algorithm, is used to detect cycles in a linked list or in a sequence of values. It uses two pointers moving at different speeds to determine whether there is a cycle and if so, where it begins.

##Key Concepts:
##Tortoise and Hare:
##The tortoise moves one step at a time.
##The hare moves two steps at a time.

##Cycle Detection:
##If the sequence (linked list) contains a cycle, the tortoise and hare will eventually meet at some point within the cycle. If they do meet, a cycle is present.
##If there is no cycle, the hare will eventually reach the end of the list.

##Steps to Detect a Cycle:
##1 - Initialization: Start with two pointers (tortoise and hare). The tortoise starts at the first node, and the hare starts at the first node as well.
##2 - Move the Pointers: In each iteration, move the tortoise by one step and the hare by two steps.
##3 - Cycle Detection: If at any point, the tortoise and hare meet (i.e., they point to the same node), a cycle exists.
##4 - No Cycle: If the hare reaches the end of the list (i.e., a None value), then no cycle exists.

##Here’s how you can implement Floyd's Cycle Detection Algorithm in Python:

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    tortoise = head
    hare = head

    while hare and hare.next:
        tortoise = tortoise.next         # Move tortoise 1 step
        hare = hare.next.next          # Move hare 2 steps

        # If tortoise and hare meet, there's a cycle
        if tortoise == hare:
            return True

    return False  # No cycle

# Example to test
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Creating a linked list with a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle here (node2 -> node3 -> node4 -> node2)

print(hasCycle(node1))  # Should return True

# Creating a linked list without a cycle
node1_no_cycle = ListNode(1)
node2_no_cycle = ListNode(2)
node3_no_cycle = ListNode(3)
node1_no_cycle.next = node2_no_cycle
node2_no_cycle.next = node3_no_cycle

print(hasCycle(node1_no_cycle))  # Should return False
