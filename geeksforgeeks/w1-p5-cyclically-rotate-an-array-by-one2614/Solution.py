#User function Template for python3

class Solution:
    def rotate(self, arr):
        count = 1
        for i in range(count):
            arr.insert(0, arr.pop())
        return arr