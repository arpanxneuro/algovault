class Solution:
    def largest(self, arr):
        if len(arr)==0:
            return -1
        max = arr[0]
        for i in range(1, len(arr)):
            if arr[i]>max:
                max = arr[i]
        
        return max