# Array Prototype Last

> **Platform:** LeetCode  
> **Difficulty:** easy  
> **Tags:** array, functional‑programming, higher‑order‑function

---

## 📝 Problem Statement

Extend the built-in JavaScript array type so that any array instance has a method `last()`, which behaves as follows:

- If the array has one or more elements, `arr.last()` returns the final element of the array.
- If the array is empty, `arr.last()` returns `-1`.

You may assume arrays originate from a valid JSON parse, i.e. standard JavaScript arrays. :contentReference[oaicite:5]{index=5}

---

## 📥 Input & Usage

- Input is provided as a JavaScript array `nums`.
- The solution environment (on LeetCode) will call `nums.last()` directly — no need for manual I/O parsing.

---

## 📤 Output

- For a non-empty array: return the last element (`nums[nums.length - 1]`).
- For an empty array: return `-1`.

---

## ✅ Examples

**Example 1**  
Input: nums = [1, 2, 3]
Output: 3
Explanation: `nums.last()` returns the last element, 3. :contentReference[oaicite:6]{index=6}

**Example 2**
Input: nums = []
Output: -1Explanation: Array is empty → return `-1`. :contentReference[oaicite:7]{index=7}

**Example 3**  
Input: nums = [null, {}, 3]
Output: 3Explanation: Mixed content is allowed; last element is 3. :contentReference[oaicite:8]{index=8}
