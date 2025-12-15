class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        # transpose
        for i in range(n):
            for j in range(i+1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        # rev cols
        for i in range(n):
            top, bottom = 0, n-1
            while top < bottom:
                mat[top][i], mat[bottom][i] = mat[bottom][i], mat[top][i]
                top += 1
                bottom -= 1
                
        return mat