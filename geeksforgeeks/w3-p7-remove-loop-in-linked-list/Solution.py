'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head
        isCycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                isCycle = True
                break
        if not isCycle:
            return None
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        ptr = slow
        while ptr.next != slow:
            ptr = ptr.next
        ptr.next = None   # break the loop

        return head