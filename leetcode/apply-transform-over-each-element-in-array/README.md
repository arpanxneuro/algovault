# Apply Transform Over Each Element in Array

**Platform:** [LeetCode](https://leetcode.com/problems/apply-transform-over-each-element-in-array/)  
**Category:** Functional Programming / Arrays  
**Difficulty:** Easy  
**Problem Statement:** Implement a custom map function that applies a provided transform `fn` to every element `arr[i]` (optionally using the index) and returns a new array containing the transformed values.

---

## 📘 Problem Overview
This problem recreates `Array.prototype.map` without using the built-in helper. The provided callback can use both the value and index. The resulting array must preserve order and length while reflecting the mapping defined by `fn`.

---

## 📥 Input Format
- `arr`: integer array of length `n` (0 ≤ n ≤ 1000)
- `fn(value, index)`: transformation function returning an integer

## 📤 Output Format
- Return a new integer array `result` where `result[i] = fn(arr[i], i)` for all valid indices.

## 🔍 Constraints
- `0 ≤ arr.length ≤ 1000`
- `-10^9 ≤ arr[i] ≤ 10^9`
- `fn` must return an integer
- Must not use `Array.prototype.map`

---

## 🧪 Sample Cases

### Example 1
**Input:** `arr = [1, 2, 3]`, `fn = n => n + 1`  
**Output:** `[2, 3, 4]`  
**Explanation:** Every element is incremented by 1.

### Example 2
**Input:** `arr = [1, 2, 3]`, `fn = (n, i) => n + i`  
**Output:** `[1, 3, 5]`  
**Explanation:** Each element is increased by its index.

### Example 3
**Input:** `arr = [10, 20, 30]`, `fn = () => 42`  
**Output:** `[42, 42, 42]`  
**Explanation:** Constant-returning functions are valid.

---

## 🧠 Approach
1. Create a new array `result` with the same length as `arr`.
2. Iterate over `arr` once.
3. For each index `i`, evaluate `fn(arr[i], i)` and store it in `result[i]`.
4. Return `result` after the loop.

### Key Insights
- The callback may use the index to make position-aware transformations.
- Avoiding `.map()` ensures compatibility even when the built-in helper is restricted.

---

## 📊 Complexity Analysis
- **Time Complexity:** `O(n)` — Single pass over `arr`.
- **Space Complexity:** `O(n)` — Output array of length `n`.

---

## 📝 Notes
- Supports empty arrays by returning `[]`.
- Works with large integers and negative values.
