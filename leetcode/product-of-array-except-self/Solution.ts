function productExceptSelf(nums: number[]): number[] {
    const n: number = nums.length;
    let ans: number[] = new Array(n).fill(1);
    let suffix: number = 1;
    for (let i = 1; i < n; i++) {
        ans[i] = ans[i - 1] * nums[i - 1];
    }
    for (let i = n - 2; i >= 0; i--) {
        suffix *= nums[i + 1];
        ans[i] *= suffix;
    }
    return ans;
};