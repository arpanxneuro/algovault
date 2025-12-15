class Solution:
    def getSecondLargest(self, arr):
        if len(arr)<2:
            return None
        uni_val = set(arr)
        if len(uni_val)<2:
            return None
        sorted_el = sorted(uni_val, reverse=True)
        
        return sorted_el[1]