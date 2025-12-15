class Solution:
    def isPalindrome(self, s):
        # Compare the string with its reverse
        return s == s[::-1]
