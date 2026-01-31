class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int srow = 0, erow = m - 1, scol = 0, ecol = n - 1;
        vector<int> ans;
        int total = m * n;

        while (ans.size() < total) {
            // top
            for (int j = scol; j <= ecol && ans.size() < total; j++)
                ans.push_back(matrix[srow][j]);
            srow++;
            // right
            for (int i = srow; i <= erow && ans.size() < total; i++)
                ans.push_back(matrix[i][ecol]);
            ecol--;
            // bottom
            for (int j = ecol; j >= scol && ans.size() < total; j--)
                ans.push_back(matrix[erow][j]);
            erow--;
            // left
            for (int i = erow; i >= srow && ans.size() < total; i--)
                ans.push_back(matrix[i][scol]);
            scol++;
        }

        return ans;
    }
};
