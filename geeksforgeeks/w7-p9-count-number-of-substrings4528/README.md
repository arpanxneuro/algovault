# Count Number of Substrings with Exactly K Distinct Characters

> **Difficulty**: Medium  
> **Source**: GeeksforGeeks  
> **Tags**: sliding-window, two-pointers-algorithm, strings, dynamic programming, algorithms

---

## 📝 Problem Statement

Given a string `S` of lowercase letters and an integer `K`, count all substrings (not necessarily distinct) of `S` that contain exactly `K` distinct characters. Substrings with identical content but different positions are counted separately. ([GeeksforGeeks – Count substrings with k distinct characters](https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/))

---

## 📥 Input

- `S`: a lowercase English‑letter string, `1 ≤ |S| ≤ 10^4`.
- `K`: an integer, `1 ≤ K ≤ 26`.

---

## 📤 Output

- Return an integer — the number of substrings of `S` that have exactly `K` distinct characters.

---

## 🧪 Examples

**Example 1**  
Input: S = "aba", K = 2
Output: 3
Explanation: substrings are "ab", "ba", "aba"

**Example 2**  
Input: S = "abc", K = 2
Output: 2
Explanation: substrings are "ab", "bc"

**Example 3**  
Input: S = "aa", K = 1
Output: 3
Explanation: substrings are "a", "a", "aa"

---

## 🛠️ Approach

Use a sliding‑window + “at most K distinct” trick:

1. Define a helper function `atMostKDistinct(s, k)` that counts the number of substrings with _at most_ `k` distinct characters — using two‑pointer / sliding window + a fixed-size frequency array (size 26).
2. The answer is:  
   countExactlyK = atMostKDistinct(S, K) – atMostKDistinct(S, K − 1)
3. In `atMostKDistinct`, maintain a window `[i..j]`, expand `j`, update freq & distinct count; when distinct > k, move `i` forward until valid; accumulate valid substrings ending at `j`.
