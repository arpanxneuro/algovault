# Longest Common Prefix

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: string, array, trie

---

## 📝 Problem Statement

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`. ([LeetCode #14 Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/))

---

## 📥 Input Format

- `strs`: An array of strings.
  - `1 <= strs.length <= 200` :contentReference[oaicite:1]{index=1}
  - Each string `strs[i]` satisfies `0 <= strs[i].length <= 200`. :contentReference[oaicite:2]{index=2}
  - Strings consist only of lowercase English letters. :contentReference[oaicite:3]{index=3}

---

## 📤 Output Format

- Return a string — the longest common prefix of all strings in `strs`.
- If there is no common prefix, return an empty string `""`.

## ✔️ Constraints

- Number of strings: `1 <= strs.length <= 200` :contentReference[oaicite:4]{index=4}
- Each string length: `0 <= strs[i].length <= 200` :contentReference[oaicite:5]{index=5}
- Characters: only lowercase English letters (a–z). :contentReference[oaicite:6]{index=6}

---

## 🧪 Sample Cases

**Example 1**  
**Input:** `["flower", "flow", "flight"]`  
**Output:** `"fl"`  
**Explanation:** All strings start with `"fl"`. :contentReference[oaicite:7]{index=7}

**Example 2**  
**Input:** `["dog", "racecar", "car"]`  
**Output:** `""`  
**Explanation:** There is no common prefix among all strings. :contentReference[oaicite:8]{index=8}

**Example 3**  
**Input:** `["interspecies", "interstellar", "interstate"]`  
**Output:** `"inters"`  
**Explanation:** The first six characters `"inters"` are common to all strings. :contentReference[oaicite:9]{index=9}

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
- If any string is shorter than `i + 1`, or the characters differ — stop scanning and return the prefix up to position `i`. :contentReference[oaicite:10]{index=10}
- If you finish scanning all characters of the reference string without mismatches — return the entire reference string.
