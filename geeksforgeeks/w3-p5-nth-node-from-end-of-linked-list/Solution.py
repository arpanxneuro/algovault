'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count = count+1
        if k>count:
            return -1
        else:
            for x in range(count-k):
                head = head.next
            return head.data