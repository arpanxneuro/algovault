# kadane's algorithm

> **Difficulty**: medium  
> **Platform**: N/A  
> **Tags**: array, dynamic programming, greedy

---

## 📝 Problem Statement

You are given an integer array `arr[]`. You need to find the **maximum sum of a contiguous subarray** (containing at least one element) in the array. A subarray is defined as a **continuous part** of the array, and you must return the largest possible sum of such a subarray. This problem is commonly solved with **Kadane’s Algorithm** in linear time. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

- An integer array `arr[]` of size `n`, where  
  `1 ≤ arr.size() ≤ 10^5`  
  `-10^4 ≤ arr[i] ≤ 10^4` :contentReference[oaicite:1]{index=1}

---

## 📤 Output

Return the **maximum sum** achievable from any **contiguous subarray** of `arr[]`.

## ✔️ Constraints

- Array length up to 100,000
- Elements may be negative or positive
- Must find the subarray sum efficiently (expected O(n) time) :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:
`arr[] = [2, 3, -8, 7, -1, 2, 3]`

**Output**:
`11`

**Explanation**:
The subarray `[7, -1, 2, 3]` has the largest sum of `11`. :contentReference[oaicite:3]{index=3}

---

**Input**:
`arr[] = [-2, -4]`

**Output**:
`-2`

**Explanation**:
All values are negative, so the maximum subarray sum is the single element `-2`. :contentReference[oaicite:4]{index=4}

---

**Input**:
`arr[] = [5, 4, 1, 7, 8]`

**Output**:
`25`

**Explanation**:
The entire array gives the largest sum `25`. :contentReference[oaicite:5]{index=5}

---

## 🧪 Test Cases

| #   | Input                   | Output                            |
| --- | ----------------------- | --------------------------------- |
| 1   | [2, 3, -8, 7, -1, 2, 3] | 11                                |
| 2   | [-2, -4]                | -2                                |
| 3   | [5, 4, 1, 7, 8]         | 25                                |
| 4   | [-1, 0, -2]             | 0 or -1 (depending on definition) |

---

## 🛠️ Approach

Use **Kadane’s Algorithm** — an optimal linear-time solution:

1. Initialize two variables:
   - `currentSum`: running sum ending at current position
   - `maxSum`: global maximum found so far
2. For each element `x` in the array:
   - Update `currentSum = max(x, currentSum + x)`
   - Update `maxSum = max(maxSum, currentSum)`
3. Return `maxSum`, which holds the maximum contiguous subarray sum. :contentReference[oaicite:6]{index=6}

### Time and Space Complexity

- **Time Complexity**: O(n) — single pass through the array
- **Space Complexity**: O(1) — constant extra memory
