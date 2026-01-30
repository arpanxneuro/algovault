class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True]*(n+1)
        count = 0
        for i in range(2, n):
            j=i*2
            if isPrime[i]:
                count+=1
                while j<n:
                    isPrime[j] = False
                    j+=i

        return count