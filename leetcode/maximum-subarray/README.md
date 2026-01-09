# maximum subarray

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, divide and conquer, dynamic programming

---

## 📝 Problem Statement

Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum**, and return its sum. A subarray is defined as a continuous segment of the array. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

An integer array `nums` of length between `1` and `10^5` where each element satisfies `-10^4 <= nums[i] <= 10^4`. :contentReference[oaicite:1]{index=1}

---

## 📤 Output

Return the **maximum sum** of any contiguous subarray of `nums`.

## ✔️ Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- Subarray must contain at least one number. :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:
`nums = [-2,1,-3,4,-1,2,1,-5,4]`

**Output**:
`6`

**Explanation**:  
The contiguous subarray `[4,-1,2,1]` has the largest sum, which is `6`. :contentReference[oaicite:3]{index=3}

---

**Input**:
`nums = [1]`

**Output**:
`1`

---

**Input**:
`nums = [5,4,-1,7,8]`

**Output**:
`23`

---

## 🧪 Test Cases

| #   | Input                     | Output |
| --- | ------------------------- | ------ |
| 1   | `[-2,1,-3,4,-1,2,1,-5,4]` | 6      |
| 2   | `[1]`                     | 1      |
| 3   | `[5,4,-1,7,8]`            | 23     |
| 4   | `[-1,-2,-3,-1]`           | -1     |

---

## 🛠️ Approach

A highly effective solution uses **Kadane’s Algorithm** (a dynamic programming/greedy technique):

1. Initialize two variables:
   - `currentSum`: maximum sum of a subarray ending at the current index
   - `maxSum`: global maximum sum found so far
2. For each element `num` in `nums`:
   - `currentSum = max(num, currentSum + num)`
   - `maxSum = max(maxSum, currentSum)`
3. Return `maxSum` at the end of the traversal. :contentReference[oaicite:4]{index=4}

This approach runs in **O(n)** time with **O(1)** extra space. :contentReference[oaicite:5]{index=5}

### Time and Space Complexity

- **Time Complexity**: O(n) — single pass through the array
- **Space Complexity**: O(1) — only constant extra space
