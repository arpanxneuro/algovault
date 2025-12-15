class Solution:
    def reverseexponentiation(self, n):
        rev = int(str(n)[::-1])
        return n ** rev