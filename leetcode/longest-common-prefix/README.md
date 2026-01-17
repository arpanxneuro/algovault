# Longest Common Prefix

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: string, array, trie

---

## 📝 Problem Statement

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`. ([LeetCode #14 Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/))

---

## 📥 Input

- `strs`: An array of strings.
  - `1 <= strs.length <= 200`
  - Each string `strs[i]` satisfies `0 <= strs[i].length <= 200`.
  - Strings consist only of lowercase English letters.

---

## 📤 Output

- Return a string — the longest common prefix of all strings in `strs`.
- If there is no common prefix, return an empty string `""`.

## ✔️ Constraints

- Number of strings: `1 <= strs.length <= 200`
- Each string length: `0 <= strs[i].length <= 200`
- Characters: only lowercase English letters (a–z).

---

## 🧪 Sample Cases

**Example 1**  
**Input:** `["flower", "flow", "flight"]`  
**Output:** `"fl"`  
**Explanation:** All strings start with `"fl"`.

**Example 2**  
**Input:** `["dog", "racecar", "car"]`  
**Output:** `""`  
**Explanation:** There is no common prefix among all strings.

**Example 3**  
**Input:** `["interspecies", "interstellar", "interstate"]`  
**Output:** `"inters"`  
**Explanation:** The first six characters `"inters"` are common to all strings.

**Example 4**  
**Input:** `["a"]`  
**Output:** `"a"`  
**Explanation:** Single-string array — the string itself is the common prefix.

**Example 5**  
**Input:** `["", "abc"]`  
**Output:** `""`  
**Explanation:** One string is empty — the longest common prefix must be empty.

---

## 🛠️ Approach

A straightforward “vertical‑scanning” approach works well:

- Use the first string `strs[0]` as reference.
- For each character position `i` in the reference string, compare with the character at the same position in all other strings.
- If any string is shorter than `i + 1`, or the characters differ — stop scanning and return the prefix up to position `i`.
- If you finish scanning all characters of the reference string without mismatches — return the entire reference string.
