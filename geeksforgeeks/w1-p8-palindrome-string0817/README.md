# Palindrome String

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: string, dsa

---

## 📝 Problem Statement

Given a string `str`, determine whether it is a **palindrome** — i.e., the string reads the same forward and backward. Return `true` (or `1` depending on implementation) if it is a palindrome; otherwise return `false` (`0`). :contentReference[oaicite:2]{index=2}

---

## 📥 Input

- A string `str` of length \( n \)

---

## 📤 Output

- A boolean (or integer) indicating whether the string is a palindrome.
  - `true` / `1` — if `str` is a palindrome
  - `false` / `0` — otherwise

---

## ✅ Examples

**Example 1**  
**Input**: str = "abba"
**Output**: true (or 1)

**Example 2**  
**Input**: str = "abc"
**Output**: false (or 0)

([geeksforgeeks.org](https://www.geeksforgeeks.org/palindrome-string/)) :contentReference[oaicite:3]{index=3}

---

## 🛠️ Approach

Use the two‑pointer method (or compare reversed string) — O(n) time, O(1) extra space:

- Maintain two indices: `left = 0`, `right = n − 1`.
- While `left < right`, compare `str[left]` and `str[right]`.
  - If they differ → not a palindrome → return `false` or `0`.
  - Else, increment `left`, decrement `right`.
- If loop completes without mismatch → return `true` / `1`.  
  :contentReference[oaicite:4]{index=4}

**Time Complexity:** O(n) — single pass through half the string. :contentReference[oaicite:5]{index=5}  
**Space Complexity:** O(1) — only a few pointers/indices used. :contentReference[oaicite:6]{index=6}

---

## 📌 Notes

- Works for strings of any length ≥ 1.
- Handles even and odd length strings gracefully.
