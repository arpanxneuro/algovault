# remove all occurrences of a substring

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: string, stack, simulation

---

## 📝 Problem Statement

Given two strings `s` and `part`, repeatedly remove the **leftmost occurrence** of the substring `part` from `s` until `s` no longer contains `part`.  
Return the final string after all such removals are completed.

A substring is defined as a contiguous sequence of characters within a string.

---

## 📥 Input

- A string `s`
- A string `part`

---

## 📤 Output

- A string representing `s` after removing all occurrences of `part`

## ✔️ Constraints

- `1 <= s.length <= 1000`
- `1 <= part.length <= 1000`
- `s` and `part` consist of lowercase English letters only

---

## ✅ Example

**Input**:
`s = "daabcbaabcbc", part = "abc"`
**Output**:
`dab`
**Explanation**:

```
- Remove `"abc"` starting at index 2 → `dabaabcbc`
- Remove `"abc"` starting at index 4 → `dababc`
- Remove `"abc"` starting at index 3 → `dab`
- No further occurrences exist
```

---

## 🧪 Test Cases

| #   | Input                            | Output |
| --- | -------------------------------- | ------ |
| 1   | s = "daabcbaabcbc", part = "abc" | dab    |
| 2   | s = "axxxxyyyyb", part = "xy"    | ab     |

---

## 🛠️ Approach

A scalable approach involves simulating string construction using a stack (or dynamic string buffer).  
As characters are processed sequentially, they are appended to the buffer. Whenever the suffix of the buffer matches `part`, it is immediately removed. This ensures leftmost removal while maintaining optimal performance under the given constraints.

This strategy avoids repeated full-string scans and aligns with linear-time string processing principles.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
