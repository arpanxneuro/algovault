class Solution:
    def isFreqSame(self, f1, f2):
        for i in range(26):
            if f1[i] != f2[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        freq = [0]*26
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
        for i in range(n2):
            winIdx, idx = 0, i
            winFreq = [0]*26
            while winIdx < n1 and idx < n2:
                winFreq[ord(s2[idx]) - ord('a')] += 1
                winIdx += 1
                idx += 1
            if  self.isFreqSame(freq, winFreq):
                return True
        return False