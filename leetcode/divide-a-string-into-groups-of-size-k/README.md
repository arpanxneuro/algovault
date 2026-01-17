# Divide a String Into Groups of Size k

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: string, simulation

---

## 📝 Problem Statement

You are given a lowercase string `s`, an integer `k`, and a character `fill`. Partition the string into groups (substrings) of size `k` as follows:

- The first group consists of the first `k` characters of `s`.
- The second group consists of the next `k` characters.
- And so on.
- For the final group: if the remaining characters are fewer than `k`, append the `fill` character repeatedly until the group reaches size `k`.

Return an array of strings representing all groups after partitioning. ([LeetCode #2138 Divide a String Into Groups of Size k](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/))

---

## 📥 Input

- `s`: a non‑empty string of lowercase English letters.
- `k`: integer group size (1 ≤ k ≤ 100)
- `fill`: a lowercase English letter used for padding the final group if needed

---

## 📤 Output

- An array of strings: each string is a group of length exactly `k`, in the order they were formed.

## ✔️ Constraints

- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters.
- `1 <= k <= 100`
- `fill` is a lowercase English letter.

---

## ✅ Example Cases

### Example 1

**Input:**  
s = "abcdefghi", k = 3, fill = "x"
**Output:**  
["abc", "def", "ghi"]
**Explanation:**  
The string divides evenly into groups of size 3 — no padding required.

### Example 2

**Input:**  
s = "abcdefghij", k = 3, fill = "x"
**Output:**  
["abc", "def", "ghi", "jxx"]
**Explanation:**  
Last group contains only “j”, so it is padded with two ‘x’ to reach size 3.

---

## 🛠️ Approach

- Traverse the string in steps of size `k`.
- For each step, extract the substring of next `k` characters (or whatever remains).
- If the last chunk is shorter than `k`, pad it with the `fill` character until its length becomes `k`.
- Append each group (padded when necessary) to the result array.
