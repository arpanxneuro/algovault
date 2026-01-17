# find the index of the first occurrence in a string

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: string, substring, sliding-window

---

## 📝 Problem Statement

Given two strings `needle` and `haystack`, return the index of the **first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`. If `needle` is empty, it is typically considered to occur at index `0`.

---

## 📥 Input

- A string `haystack`  
- A string `needle`

---

## 📤 Output

Return the **index of the first occurrence** of `needle` in `haystack`, or `-1` if no match exists.

## ✔️ Constraints

- `1 <= haystack.length, needle.length <= 10⁴`  
- `haystack` and `needle` consist only of lowercase English characters.

---

## ✅ Example

**Input**:
haystack = "sadbutsad", needle = "sad"

**Output**:
0

**Explanation**:
`sad` occurs at index 0 and 6; the first occurrence at index 0 is returned.

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | haystack = "sadbutsad", needle = "sad" | 0 |
| 2 | haystack = "leetcode", needle = "leeto" | -1 |
| 3 | haystack = "hello", needle = "ll" | 2 |
| 4 | haystack = "aaa", needle = "a" | 0 |

---

## 🛠️ Approach

A **sliding window** or **two-pointer substring matching** strategy compares a window of `haystack` (of length equal to `needle.length`) to the target `needle`. Slide the window from left to right; when the substring matches `needle`, return the current index. If no match is found, return `-1`.

### Time and Space Complexity
- **Time Complexity**: O(n × m), where `n = haystack.length` and `m = needle.length`  
- **Space Complexity**: O(1)

