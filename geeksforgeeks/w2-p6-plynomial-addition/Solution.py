# Node definition
class Node:
    def __init__(self, coef, power):
        self.coef = coef
        self.power = power
        self.next = None

class Solution:
    def add_polynomial(self, head1, head2):
        dummy = Node(0, 0)
        tail = dummy

        p1, p2 = head1, head2
        while p1 and p2:
            if p1.power == p2.power:
                coef_sum = p1.coef + p2.coef
                if coef_sum != 0:
                    tail.next = Node(coef_sum, p1.power)
                    tail = tail.next
                p1, p2 = p1.next, p2.next

            elif p1.power > p2.power:
                tail.next = Node(p1.coef, p1.power)
                tail = tail.next
                p1 = p1.next

            else:  # p2.power > p1.power
                tail.next = Node(p2.coef, p2.power)
                tail = tail.next
                p2 = p2.next

        while p1:
            tail.next = Node(p1.coef, p1.power)
            tail = tail.next
            p1 = p1.next

        while p2:
            tail.next = Node(p2.coef, p2.power)
            tail = tail.next
            p2 = p2.next

        return dummy.next
