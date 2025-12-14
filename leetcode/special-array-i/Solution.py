class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        for i in range(1, len(nums)):
            if ((nums[i]%2)==(nums[i-1])%2): return False
        return True