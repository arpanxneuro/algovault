class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        new_node = Node(x)
        
        # 1. if head is empty
        if head is None:
            head = new_node
            
        # 2. isert at first
        if x <= head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        
        # 3. insert at mid or end
        curr = head
        while curr.next and curr.next.data < x:
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        
        return head