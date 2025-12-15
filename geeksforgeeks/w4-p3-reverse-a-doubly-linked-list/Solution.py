class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def reverse(self, head):
        if not head:
            return None

        curr = head
        prev = None
        
        while curr:
            # Swap next and prev pointers
            curr.prev, curr.next = curr.next, curr.prev
            # Move prev to current before going to next node
            prev = curr
            # Move to next node (curr.prev)
            curr = curr.prev
        
        # prev will be the new head after reversal
        return prev
