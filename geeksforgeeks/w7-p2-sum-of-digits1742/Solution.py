class Solution:
    def sumOfDigits(self, n):
        if n == 0:
            return 0
        
        return (n % 10) + self.sumOfDigits(n // 10)
