# permutation in string

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: string, sliding window, hashing

---

## 📝 Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains **any permutation** of `s1` as a **contiguous substring**, or `false` otherwise.  
A permutation is defined as a rearrangement of characters. The problem reduces to checking if _some substring of `s2` has the same character frequency profile as `s1`_.

---

## 📥 Input

- `s1`: string
- `s2`: string

---

## 📤 Output

- `true` | `false`: boolean indicating if any permutation of `s1` exists as a substring in `s2`.

## ✔️ Constraints

- `1 <= s1.length, s2.length <= 104`
- `s1` and `s2` consist of lowercase English letters only

---

## ✅ Example

**Input**:
s1 = "ab"
s2 = "eidbaooo"
**Output**:
true
**Explanation**:
`s2` contains `"ba"` which is a permutation of `"ab"`.

---

## 🧪 Test Cases

| #   | Input                      | Output |
| --- | -------------------------- | ------ |
| 1   | s1 = "ab", s2 = "eidbaooo" | true   |
| 2   | s1 = "ab", s2 = "eidboaoo" | false  |

---

## 🛠️ Approach

Use a **sliding window** of size equal to `s1.length()` over `s2`. Maintain **character frequency arrays** for both `s1` and the current window in `s2`. Update the window counts incrementally and compare against the frequency of `s1` at each step. If the counts match at any position, a valid permutation exists.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)  
  (Assuming fixed alphabet size of 26)
