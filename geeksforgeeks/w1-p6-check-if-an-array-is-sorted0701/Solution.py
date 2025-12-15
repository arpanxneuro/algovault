class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(len(arr)):
            if i != len(arr)-1:
                if arr[i] > arr[i+1]:
                    return False
            else:
                if arr[i-1] > arr[i]:
                    return False
        return True