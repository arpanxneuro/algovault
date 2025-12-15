class Solution:
    def countZeroes(self, A, N):
        count = 0
        flat = [i for row in A for i in row]
        for i in flat:
            if i == 0:
                count +=1
        
        return count