class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteNode(self, head, x):
        if head is None:
            return None
        if x == 1:
            return head.next
        curr = head
        count = 1
        while curr and count < x-1:
            curr = curr.next
            count += 1
        if curr and curr.next:
            curr.next = curr.next.next
        
        return head