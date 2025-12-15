class Solution:
    def frequencyCount(self, arr):
        freq = {}
        for n in arr:
            if 1<=n<=len(arr):
                freq[n] = freq.get(n, 0) + 1
        res = [freq.get(i, 0) for i in range(1, len(arr)+1)]
        
        return res