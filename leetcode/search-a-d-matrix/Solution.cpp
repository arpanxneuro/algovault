class Solution
{
public:
    bool searchInRw(vector<vector<int>> &mat, int t, int row)
    {
        int n = mat[0].size();
        int st = 0, end = n - 1;
        while (st <= end)
        {
            int mid = st + (end - st) / 2;
            if (t == mat[row][mid])
                return true;
            else if (t > mat[row][mid])
                st = mid + 1;
            else
                end = mid - 1;
        }
        return false;
    }

    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        if (matrix.empty() || matrix[0].empty())
            return false;

        int m = matrix.size(), n = matrix[0].size();
        int stRw = 0, endRw = m - 1;

        while (stRw <= endRw)
        {
            int mid = stRw + (endRw - stRw) / 2;

            if (target >= matrix[mid][0] && target <= matrix[mid][n - 1])
            {
                return searchInRw(matrix, target, mid);
            }
            else if (target > matrix[mid][n - 1])
            {
                stRw = mid + 1;
            }
            else
            {
                endRw = mid - 1;
            }
        }
        return false;
    }
};
