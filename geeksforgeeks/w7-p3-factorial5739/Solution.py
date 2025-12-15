class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        if n==1 or n==0:
            return n
        return n*self.factorial(n-1)