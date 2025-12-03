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

## 📥 Input Format

- `s`: a non‑empty string of lowercase English letters. :contentReference[oaicite:0]{index=0}
- `k`: integer group size (1 ≤ k ≤ 100) :contentReference[oaicite:1]{index=1}
- `fill`: a lowercase English letter used for padding the final group if needed :contentReference[oaicite:2]{index=2}

---

## 📤 Output Format

- An array of strings: each string is a group of length exactly `k`, in the order they were formed.

## ✔️ Constraints

- `1 <= s.length <= 100` :contentReference[oaicite:3]{index=3}
- `s` consists only of lowercase English letters. :contentReference[oaicite:4]{index=4}
- `1 <= k <= 100` :contentReference[oaicite:5]{index=5}
- `fill` is a lowercase English letter. :contentReference[oaicite:6]{index=6}

---

## ✅ Example Cases

### Example 1

**Input:**  
s = "abcdefghi", k = 3, fill = "x"
**Output:**  
["abc", "def", "ghi"]
**Explanation:**  
The string divides evenly into groups of size 3 — no padding required. :contentReference[oaicite:7]{index=7}

### Example 2

**Input:**  
s = "abcdefghij", k = 3, fill = "x"
**Output:**  
["abc", "def", "ghi", "jxx"]
**Explanation:**  
Last group contains only “j”, so it is padded with two ‘x’ to reach size 3. :contentReference[oaicite:8]{index=8}

---

## 🛠️ Approach

- Traverse the string in steps of size `k`.
- For each step, extract the substring of next `k` characters (or whatever remains).
- If the last chunk is shorter than `k`, pad it with the `fill` character until its length becomes `k`. :contentReference[oaicite:9]{index=9}
- Append each group (padded when necessary) to the result array.
