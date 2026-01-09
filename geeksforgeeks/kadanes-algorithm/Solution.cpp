class Solution {
  public:
    int maxSubarraySum(vector<int> &arr) {
        // Code here
        int currSum=0, maxSum=INT_MIN;
        for(int i=0; i<arr.size(); i++) {
            currSum += arr[i];
            maxSum = max(currSum, maxSum);
            if(currSum<0) currSum=0;
        }
        
        return maxSum;
    }
};