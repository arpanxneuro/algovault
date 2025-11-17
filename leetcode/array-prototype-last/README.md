# Array Prototype Last

**Platform:** [LeetCode](https://leetcode.com/problems/array-prototype-last/)  
**Category:** Functional Programming / JavaScript  
**Difficulty:** Easy  
**Problem Statement:** Augment the JavaScript `Array` prototype with a `last()` method that returns the final element of an array. If the array is empty, the method must return `-1`. Inputs originate from `JSON.parse`, guaranteeing valid array instances.

---

## 📘 Problem Overview
This problem verifies understanding of prototype extensions. The solution should work for arrays containing any data type, must not modify existing built-ins beyond the added method, and must protect against empty arrays.

---

## 📥 Input Format
- `nums`: JSON-parsed array with length `n` (0 ≤ n ≤ 1000). Elements can be numbers, objects, or `null`.

## 📤 Output Format
- `nums.last()` should return the last element when `n > 0`.
- If `n == 0`, the method should return `-1`.

## 🔍 Constraints
- Arrays are valid JSON arrays parsed before invocation.
- No additional arguments are provided to the method.
- Should not rely on built-in helpers other than basic property access.

---

## 🧪 Sample Cases

### Example 1
**Input:** `nums = [null, {}, 3]`

**Output:** `3`

**Explanation:** `nums.last()` returns the final element, which is `3`.

### Example 2
**Input:** `nums = []`

**Output:** `-1`

**Explanation:** Empty arrays must return `-1` as a sentinel value.

---

## 🧠 Approach
1. Extend `Array.prototype` with a function named `last`.
2. Inside the method, check `this.length`.
3. Return `-1` if the array is empty; otherwise return `this[this.length - 1]`.

### Considerations
- Using `function` syntax ensures `this` binds to the array instance.
- The method should not mutate the array or accept parameters.

---

## 📊 Complexity Analysis
- **Time Complexity:** `O(1)` — constant-time access to the last index.
- **Space Complexity:** `O(1)` — no additional storage.

---

## 📝 Notes
- Works for arrays containing any JSON-supported type.
- Returning `-1` is mandated by the problem statement for empty arrays.
