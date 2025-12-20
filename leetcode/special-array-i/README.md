# Special Array I

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, simulation

---

## 📝 Problem Statement

An array is considered **special** if every pair of its adjacent elements has opposite parity (one even and one odd). Given an array `nums`, return `true` if the array is special, otherwise return `false`.

---

## 📥 Input

- `nums`: An array of integers (1 ≤ nums.length ≤ 100)
  - Each element nums[i] is an integer (0 ≤ nums[i] ≤ 100)

---

## 📤 Output

- Returns `true` if the array is special, `false` otherwise

## ✔️ Constraints

- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 100

---

## ✅ Example

**Input:**  
[1]
**Output:**  
true
**Input:**  
[2, 1, 4]
**Output:**  
true
**Input:**  
[4, 3, 1, 6]
**Output:**  
false

---

## 🧪 Test Cases

| #   | Input       | Output  |
| --- | ----------- | ------- |
| 1   | `[1]`       | `true`  |
| 2   | `[2,1,4]`   | `true`  |
| 3   | `[4,3,1,6]` | `false` |
| 4   | `[1,2,3,4]` | `true`  |

---

## 🛠️ Approach

1. Iterate through the array starting from index 1.
2. For each adjacent pair `(nums[i-1], nums[i])`, check parity using modulo (`% 2`).
3. If any adjacent pair has the same parity (both even or both odd), return `false` immediately.
4. If all pairs pass, return `true`.

---

### Time and Space Complexity

- **Time Complexity:** O(n) — single pass through the array
- **Space Complexity:** O(1) — only a constant amount of extra space is used

---

## 🔗 Related Problems

- [Special Array II](https://leetcode.com/problems/special-array-ii/)
- [Array With Elements Not Equal to Average of Neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/)
- [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/)
