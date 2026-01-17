# Check If an Array is Sorted

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: array, loop, conditions

---

## 📝 Problem Statement

Given an integer array `arr[]`, determine whether the array is sorted in non-decreasing (ascending) order. Return `true` if it is sorted (i.e. every element is ≤ the next), otherwise return `false`.

---

## 📥 Input

- `arr[]`: an array of integers of size `n`

---

## 📤 Output

- Return a boolean value:
  - `true` if the array is sorted in non-decreasing order.
  - `false` otherwise.

---

## ✅ Examples

**Example 1**  
arr = [10, 20, 30, 40, 50]
**Output:**  
true

**Example 2**  
arr = [90, 80, 100, 70, 40, 30]
**Output:**  
false

---

## 🛠️ Approach

Use a single-pass linear scan (O(n) time, O(1) space):

- Iterate through the array from index 1 to n-1.
- For each index `i`, check if `arr[i-1] > arr[i]`.
  - If yes — return `false`.
- If the loop completes without finding such a violation — return `true`.

### Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## 📌 Notes

- Works for any integer array (positive, negative, zero).
- Handles arrays with equal consecutive elements (non-decreasing, not strictly increasing).
