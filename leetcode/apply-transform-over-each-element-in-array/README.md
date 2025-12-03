# Apply Transform Over Each Element in Array

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, functional‑programming, higher‑order‑function

---

## 📝 Problem Statement

Given an integer array `arr` and a mapping function `fn`, return a **new** array such that  
result[i] = fn(arr[i], i)
for every valid index `i`. Do **not** use the built‑in `Array.prototype.map` method. :contentReference[oaicite:4]{index=4}

---

## 📥 Input Format

- `arr`: integer array (its length `n` may be `0 ≤ n ≤ 1000`) :contentReference[oaicite:5]{index=5}
- `fn(value, index)`: a function that takes an integer and its index and returns an integer (or number)

---

## 📤 Output Format

- A new array of integers of the same length as `arr`, where each element is the result of applying the transform: `result[i] = fn(arr[i], i)`. The original array should remain unmodified.

---

## ✅ Examples

### Example 1

Input: arr = [1, 2, 3], fn = n => n + 1
Output: [2, 3, 4]

### Example 2

Input: arr = [1, 2, 3], fn = (n, i) => n + i
Output: [1, 3, 5]

### Example 3

Input: arr = [10, 20, 30], fn = () => 42
Output: [42, 42, 42]

---

## 🛠️ Approach

1. Initialize an empty result array `res = []`.
2. Iterate over indices `i = 0 … arr.length − 1`.
3. For each `i`, compute `transformed = fn(arr[i], i)` and push/assign it to `res[i]`.
4. After the loop, return `res`.

**Time Complexity:** O(n), where n = `arr.length`.  
**Space Complexity:** O(n) — for the new output array. :contentReference[oaicite:6]{index=6}

---

## 📌 Notes

- Works for empty arrays (returns empty array).
- Supports negative, zero or large integers (within allowed constraints).
- Ensures original array remains intact (doesn't mutate it).
