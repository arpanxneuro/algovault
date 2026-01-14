class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0, count = 0;

        for (int val : nums) {
            if (count == 0) {
                candidate = val;
            }
            count += (val == candidate) ? 1 : -1;
        }

        return candidate;
    }
};
