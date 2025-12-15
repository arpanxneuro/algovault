# Reverse a String

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: string, loop

---

## 📝 Problem Statement

Given a string `s`, your task is to **reverse the string** — i.e., rearrange the characters such that the first character becomes last, the second becomes second-last, and so on. ([geeksforgeeks.org](https://www.geeksforgeeks.org/reverse-a-string/))

---

## 📥 Input

- A single string `s` of length `n`.

---

## 📤 Output

- A string that represents the **reverse** of the input string.

---

## ✅ Examples

**Example 1**  
**Input**: s = "GeeksforGeeks"
**Output**: "skeeGrofskeeG"

**Example 2**  
**Input**: s = "abdcfe"
**Output**: "efcdba"

---

## 🛠️ Approach

A simple in-place approach (two-pointer) — or building a new string in reverse — works in O(n) time:

- Set two indices: `left = 0`, `right = n − 1`.
- While `left < right`, swap `s[left]` and `s[right]`, then `left++`, `right--`.
- Return the modified string.

This approach runs in **O(n)** time and uses **O(1)** extra space (ignoring language-specific string immutability). 

---

## 📌 Notes

- Works for strings containing any characters — alphabets, digits, symbols.
- Efficient even for very long strings, linear runtime.
