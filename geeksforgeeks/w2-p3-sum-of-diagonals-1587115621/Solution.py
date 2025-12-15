from typing import List

class Solution:
    def sumDiagonal(self, N : int , M : List[List[int]] ) -> int :
        diag_sum = 0
        for i in range(N):
            diag_sum += M[i][i]
        
        return diag_sum
                