class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        myArr = []
        n = len(s)
        remainder = n % k
        if remainder != 0:
            padCount = k - remainder
            s += fill * padCount
        for i in range(0, len(s), k):
            myArr.append(s[i : i + k])
        return myArr
