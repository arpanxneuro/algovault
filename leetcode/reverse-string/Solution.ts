/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
  let start = 0,
    end = s.length - 1;
  while (start < end) {
    let temp = s[start];
    s[start] = s[end];
    s[end] = temp;
    start++;
    end--;
  }
}
