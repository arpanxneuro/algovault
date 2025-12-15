class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        if head is None:
            return new_node
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return head