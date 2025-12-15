# Node definition
class Node:
    def __init__(self, coef, power):
        self.coef = coef
        self.power = power
        self.next = None

class Solution:
    def multiply(self, A, B):
        n, m = len(A), len(B)
        res = [0] * (n + m - 1)  # result length
        
        for i in range(n):
            for j in range(m):
                res[i + j] += A[i] * B[j]
        
        return res
