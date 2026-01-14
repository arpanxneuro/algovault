class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        st, end = 0, n - 1
        while st <= end:
            mid = st + (end - st) // 2
            if n == 1:
                return nums[0]
            if mid == 0 and nums[0] != nums[1]:
                return nums[mid]
            if mid == n - 1 and nums[n - 1] != nums[n - 2]:
                return nums[mid]
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid - 1] == nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid - 1] == nums[mid]:
                    st = mid + 1
                else:
                    end = mid - 1
        return -1
