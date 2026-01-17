# Check if String is Palindrome

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: string, data‑structures, two‑pointer‑algorithms

---

## 📝 Problem Statement

Given a string `S`, write a function to determine if it is a palindrome. A string is a palindrome if it reads the same forward and backward. The comparison should be **case‑sensitive** and should consider **all characters** (i.e., do **not** ignore non‑alphanumeric characters, spaces or punctuation). ([GfG – Palindrome String Problem](https://www.geeksforgeeks.org/problems/palindrome-string0817/1))

---

## 📥 Input

- `S`: a string (1 ≤ |S| ≤ typically within practical string limits)

---

## 📤 Output

- Return `1` if the string `S` is a palindrome; otherwise return `0`.

---

## 🧪 Example Cases

| Input        | Output | Explanation                                |
| ------------ | ------ | ------------------------------------------ |
| `"radar"`    | `1`    | "radar" reads the same forwards/backwards. |
| `"hello"`    | `0`    | "hello" reversed is "olleh" — not same.    |
| `"abba"`     | `1`    | Symmetric string.                          |
| `""` (empty) | `1`    | Empty string is trivially palindrome.      |

---

## 🛠️ Approach

Use two-pointer (or recursion) technique:

- Initialize two indices: `left = 0`, `right = len(S) − 1`.
- While `left < right`:
  - Compare `S[left]` and `S[right]`; if they differ → return `0`.
  - Move `left++`, `right--`.
- If loop completes without mismatch → return `1`.

Recursively, one could check: if `S[0] != S[-1]` then not palindrome; else recurse on the substring `S[1:-1]`.

This method runs in **O(n)** time and uses **O(1)** extra space (or O(n) if recursion uses call stack).

---

## 📚 Notes & References

- Official problem (GfG “Palindrome String”) content.
- Two‑pointer method explanation from GfG editorial.
