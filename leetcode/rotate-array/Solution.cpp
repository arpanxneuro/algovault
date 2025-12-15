class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (n <= 1) return;   // nothing to do for 0/1 element
        k = k % n;
        if (k == 0) return;   // no rotation needed

        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    void reverse(vector<int>& n, int start, int end) {
        while (start < end) {
            int temp = n[start];
            n[start] = n[end];
            n[end] = temp;
            start++;
            end--;
        }
    }
};
