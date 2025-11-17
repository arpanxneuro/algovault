# Count Number of Substrings with Exactly K Distinct Characters

> **Difficulty**: Medium  
> **Companies**: Amazon, Google, Microsoft, Adobe

---

## 📝 Problem Statement

Given a string `S` of lowercase alphabets and an integer `K`, find the count of all possible substrings (not necessarily distinct) that have exactly `K` distinct characters.

---

## 📥 Input

- `S`: A string consisting of lowercase English letters (1 ≤ |S| ≤ 10^4)
- `K`: An integer representing the exact number of distinct characters required (1 ≤ K ≤ 26)

---

## 📤 Output

Return an integer representing the count of all substrings with exactly `K` distinct characters.

## ✔️ Constraints

- The string contains only lowercase English letters
- 1 ≤ |S| ≤ 10^4
- 1 ≤ K ≤ 26

---

## ✅ Example

**Input**: S = "aba", K = 2  
**Output**: 3  
**Explanation**: 
Substrings with exactly 2 distinct characters:
1. "ab" (indices 0-1)
2. "ba" (indices 1-2)
3. "aba" (indices 0-2)

**Input**: S = "aabab", K = 3  
**Output**: 0

---

## 🧪 Test Cases

| # | Input (S, K) | Output | Explanation |
|---|--------------|--------|-------------|
| 1 | "abc", 2 | 2 | "ab", "bc" |
| 2 | "aa", 1 | 3 | "a", "a", "aa" |
| 3 | "aab", 3 | 0 | No substring with 3 distinct chars |
| 4 | "aabbcc", 2 | 8 | Multiple valid substrings |
| 5 | "abcabcabc", 3 | 19 | Multiple overlapping substrings |

---

## 🛠️ Approach

### Sliding Window with Hash Map
1. **Problem Breakdown**:
   - We need to find substrings with exactly K distinct characters
   - This can be transformed into finding substrings with at most K distinct characters minus substrings with at most K-1 distinct characters

2. **Algorithm**:
   - Implement a helper function `atMostKDistinct(S, K)` that counts substrings with at most K distinct characters
   - The result is `atMostKDistinct(S, K) - atMostKDistinct(S, K-1)`
   - Use sliding window technique with a hash map to track character frequencies

3. **Optimization**:
   - Use a frequency array instead of hash map for better performance
   - Maintain a count of distinct characters in the current window

### Time and Space Complexity
- **Time Complexity**: O(N) - Each character is processed at most twice (once for each sliding window pass)
- **Space Complexity**: O(1) - Fixed size frequency array (size 26)

---

## 📝 Note
- The problem can be extended to handle case-sensitive characters or larger character sets
- The solution can be modified to return the actual substrings instead of just the count
- For very large strings, the solution remains efficient due to O(N) time complexity
- Edge cases to consider:
  - Empty string (though constraints say |S| ≥ 1)
  - K = 1 (single character substrings)
  - K = 26 (all possible distinct characters)
  - String with all identical characters