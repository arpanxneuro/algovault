class Solution:
    def series(self, n):
        MOD = 10**9 + 7
        a, b = 0, 1
        result = [a]

        for i in range(n):
            result.append(b)
            a, b = b, (a + b) % MOD  # use modulo to keep numbers small

        return result
