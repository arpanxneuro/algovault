"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        if not head:
            return None
            
        if x==1:
            head = head.next
            if head:
                head.prev = None
            return head
            
        temp = head
        for _ in range(x-1):
            temp = temp.next
            if not temp:
                return head
        
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
            
        return head