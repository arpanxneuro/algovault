class Solution:
    def searchRow(self, mat: List[List[int]], t: int, row: int) -> bool:
        n = len(mat[0])
        st, end = 0, n - 1
        while st <= end:
            mid = st + (end - st) // 2
            if t == mat[row][mid]:
                return True
            elif t > mat[row][mid]:
                st = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        stRw, endRw = 0, m - 1
        while stRw <= endRw:
            mid = stRw + (endRw - stRw) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][n - 1]:
                return self.searchRow(matrix, target, mid)
            elif target > matrix[mid][n - 1]:
                stRw = mid + 1
            else:
                endRw = mid - 1
        return False
