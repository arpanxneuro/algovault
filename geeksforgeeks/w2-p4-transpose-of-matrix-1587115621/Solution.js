class Solution {
    transpose(mat) {
        let n = mat.length;
        for(let i=0; i<n; i++) {
            for(let j=i+1; j<n; j++) {
                [mat[i][j], mat[j][i]] = [mat[j][i], mat[i][j]];
            }
        }
        
        return mat
    }
}