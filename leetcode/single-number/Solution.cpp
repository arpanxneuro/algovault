class Solution
{
public:
    int singleNumber(vector<int> &nums)
    {
        int ans = 0;
        for (int x : nums)
        {
            ans = ans ^ x;
        }

        return ans;
    }
};