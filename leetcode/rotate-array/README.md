# rotate array

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, in-place, rotation

---

## 📝 Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative. The rotation should be performed **in-place** with minimal extra space, and every element must end up in its correct rotated position such that the last `k` elements move to the front in order. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

An integer array `nums` and a non-negative integer `k`.

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5` :contentReference[oaicite:1]{index=1}

---

## 📤 Output

The same array `nums`, rotated to the right by `k` positions, modified **in place**.

## ✔️ Constraints

- The rotation must be performed in-place with O(1) extra space for the optimal solution.
- Multiple valid solution approaches exist. :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:
nums = [1,2,3,4,5,6,7], k = 3

**Output**:
[5,6,7,1,2,3,4]

**Explanation**:
After 3 right rotations, the last 3 elements (`5, 6, 7`) move to the front in order. :contentReference[oaicite:3]{index=3}

---

## 🧪 Test Cases

| #   | Input                        | Output         |
| --- | ---------------------------- | -------------- |
| 1   | nums = [1,2,3,4], k = 2      | [3,4,1,2]      |
| 2   | nums = [-1,-100,3,99], k = 2 | [3,99,-1,-100] |
| 3   | nums = [1], k = 0            | [1]            |
| 4   | nums = [1,2], k = 5          | [2,1]          |

---

## 🛠️ Approach

A highly optimized in-place solution uses a **three-step reversal technique**:

1. Normalize `k` by taking `k % n` to handle `k > n`.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the remaining `n − k` elements.

Each reversal reorders portions of the array such that the final sequence is rotated correctly. :contentReference[oaicite:4]{index=4}

### Time and Space Complexity

- **Time Complexity**: O(n), where `n = nums.length`
- **Space Complexity**: O(1) — only constant extra space is used

---

## 📌 Notes

- Rotating an array of length `n` by `k` steps is equivalent to rotating by `k % n` steps.
- The solution preserves element order without using auxiliary arrays. :contentReference[oaicite:5]{index=5}
