class Solution:
    def isPalindrome(self, s):
        if s==s[::-1]:
            return True
        else:
            return False
