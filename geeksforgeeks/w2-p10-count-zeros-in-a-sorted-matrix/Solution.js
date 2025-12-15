class Solution {
  countZeros(A, N) {
    let count = 0;
    const flat = A.flat();
    for (const val of flat) {
      if (val == 0) {
        count++;
      }
    }

    return count;
  }
}
