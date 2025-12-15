# reverse string

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: two pointers, string

---

## 📝 Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array **in-place** with **O(1)** extra memory. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

An array of characters `s`, where `1 <= s.length <= 10^5` and each `s[i]` is a printable ASCII character. :contentReference[oaicite:1]{index=1}

---

## 📤 Output

The same array `s` reversed in place.

## ✔️ Constraints

- Reverse the array without allocating additional space beyond constant extra memory.
- The solution must modify `s` directly. :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:
s = ["h","e","l","l","o"]
**Output**:
["o","l","l","e","h"]
**Explanation**:
The characters are swapped from ends inward using a two-pointer approach. :contentReference[oaicite:3]{index=3}

---

## 🧪 Test Cases

| #   | Input                     | Output                    |
| --- | ------------------------- | ------------------------- |
| 1   | ["h","e","l","l","o"]     | ["o","l","l","e","h"]     |
| 2   | ["H","a","n","n","a","h"] | ["h","a","n","n","a","H"] |
| 3   | ["a"]                     | ["a"]                     |
| 4   | ["x","y"]                 | ["y","x"]                 |

---

## 🛠️ Approach

Use a **two-pointer technique**:

1. Initialize a pointer `left` at index `0` and `right` at index `len(s) - 1`.
2. Swap the elements at `left` and `right`.
3. Move `left` forward and `right` backward.
4. Repeat until `left >= right`.

This ensures the array is reversed in place with constant extra memory. :contentReference[oaicite:4]{index=4}

### Time and Space Complexity

- **Time Complexity**: O(n) — one pass through the list
- **Space Complexity**: O(1) — constant extra space
