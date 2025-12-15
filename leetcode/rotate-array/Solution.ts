function rotate(nums: number[], k: number): void {
  const n = nums.length;
  if (n <= 1) return;
  k = k % n;
  if (k === 0) return;

  function reverse(arr: number[], start: number, end: number) {
    while (start < end) {
      const temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
      start++;
      end--;
    }
  }

  reverse(nums, 0, n - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, n - 1);
}
