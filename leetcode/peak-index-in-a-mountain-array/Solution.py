class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        st, end = 1, len(arr) - 2
        while st <= end:
            mid = st + (end - st) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid - 1] < arr[mid]:
                st = mid + 1
            else:
                end = mid - 1

        return -1
