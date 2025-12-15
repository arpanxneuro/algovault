class Solution:
    def spirallyTraverse(self, mat):
        res = []
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            # Top row
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top += 1
            # Right column
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1
            # Bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1
            # Left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1

        return res
