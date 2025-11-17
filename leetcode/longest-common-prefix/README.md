# Longest Common Prefix

**Platform:** [LeetCode](https://leetcode.com/problems/longest-common-prefix/)  
**Category:** String / Array  
**Difficulty:** Easy  
**Problem Statement:** Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

---

## 📘 Problem Overview
Given an array of strings `strs`, find the longest common prefix shared by all strings in the array. The longest common prefix is the longest string that appears at the beginning of all strings in the array.

### Key Points:
- A prefix is a substring that appears at the start of a string
- The solution should handle edge cases like empty strings and single-string arrays
- All strings consist of lowercase English letters
- The solution should be case-sensitive

---

## 📥 Input Format
- `strs`: An array of strings (1 ≤ strs.length ≤ 200)
  - Each string has length between 0 and 200
  - Strings consist of lowercase English letters only

## 📤 Output Format
- A string representing the longest common prefix
- Returns an empty string `""` if no common prefix exists

## 🔍 Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`["flower", "flow", "flight"]`  
**Output:** `"fl"`  
**Explanation:**  
All strings start with `"fl"`

### Example 2
**Input:**  
`["dog", "racecar", "car"]`  
**Output:** `""`  
**Explanation:**  
No common prefix exists among the input strings

### Example 3
**Input:**  
`["interspecies", "interstellar", "interstate"]`  
**Output:** `"inters"`  
**Explanation:**  
The longest common prefix is `"inters"`

### Example 4
**Input:**  
`["a"]`  
**Output:** `"a"`  
**Explanation:**  
Single string in the array

### Example 5
**Input:**  
`[""]`  
**Output:** `""`  
**Explanation:**  
Empty string in the array

---

## 🧠 Approach
1. **Horizontal Scanning**: Compare the first string with all other strings character by character
2. **Prefix Reduction**: For each string, reduce the prefix until it matches the beginning of the current string
3. **Early Termination**: If the prefix becomes empty at any point, return immediately
4. **Edge Cases**: Handle empty array, single string, and empty strings appropriately

### Solution Code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(S)` where S is the sum of all characters in all strings  
  - In the worst case, we compare all characters of all strings
  - Best case: O(minLen) where minLen is the length of the shortest string
  
- **Space Complexity**: `O(1)`  
  - We only use constant extra space for the prefix variable

---

## 📝 Notes
- The solution uses Python's built-in `startswith()` method for clean string comparison
- The algorithm is efficient with early termination when no common prefix is found
- Handles edge cases like empty input array or empty strings gracefully
- The solution is optimal with O(S) time complexity where S is the total number of characters

## 🔗 Related Problems
- [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [Implement strStr()](https://leetcode.com/problems/implement-strstr/)

## 📚 Additional Resources
- [GeeksforGeeks: Longest Common Prefix](https://www.geeksforgeeks.org/longest-common-prefix-using-word-by-word-matching/)
- [LeetCode Article: Longest Common Prefix](https://leetcode.com/articles/longest-common-prefix/)

This ensures predictable **O(S)** performance, where S = total number of characters across all strings.
