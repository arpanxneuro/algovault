#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        rev = ""
        for i in range(len(s)-1, -1, -1):
            rev += s[i]
        
        return rev