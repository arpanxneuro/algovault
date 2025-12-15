class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addTwoLists(self, head1, head2):
        # Step 1: Reverse both lists
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        dummy = Node(0)
        curr = dummy
        carry = 0

        # Step 2: Add lists
        while head1 or head2 or carry:
            val1 = head1.data if head1 else 0
            val2 = head2.data if head2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            curr.next = Node(total % 10)
            curr = curr.next

            if head1: head1 = head1.next
            if head2: head2 = head2.next

        # Step 3: Reverse result back
        return self.reverse(dummy.next)
