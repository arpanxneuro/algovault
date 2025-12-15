class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
		
#Function to insert a node in the middle of the linked list.
class Solution:
    def insertInMiddle(self, head, x):
        new_node = Node(x)
        if head is None:
            return new_node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_node.next = slow.next
        slow.next = new_node
        
        return head