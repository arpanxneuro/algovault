class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        srow, erow, scol, ecol = 0, m - 1, 0, n - 1
        ans = []
        total = m * n

        while len(ans) < total:
            # top
            for j in range(scol, ecol+1):
                if len(ans) == total: break
                ans.append(matrix[srow][j])
            srow+=1

            # right
            for i in range(srow, erow+1):
                if len(ans) == total: break
                ans.append(matrix[i][ecol])
            ecol-=1

            # bottom
            for j in range(ecol, scol-1, -1):
                if len(ans) == total: break
                ans.append(matrix[erow][j])
            erow -= 1

            # left
            for i in range(erow, srow-1, -1):
                if len(ans) == total: break
                ans.append(matrix[i][scol])
            scol += 1

        return ans