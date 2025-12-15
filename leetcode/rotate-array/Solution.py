class Solution:
    def reverse(self, n: List[int], start: int, end: int):
        while start < end:
            n[start], n[end] = n[end], n[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n <= 1:
            return
        k = k % n
        if k == 0:
            return

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
