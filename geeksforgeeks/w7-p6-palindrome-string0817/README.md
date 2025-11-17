# Check if String is Palindrome (Recursive)

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Adobe, Bloomberg

---

## 📝 Problem Statement

Given a string S, write a recursive function to determine if it is a palindrome. A string is a palindrome if it reads the same backward as forward, ignoring cases and non-alphanumeric characters.

---

## 📥 Input

- `S`: A string (1 ≤ |S| ≤ 10^4), where |S| is the length of the string

---

## 📤 Output

Return `1` if the string is a palindrome, `0` otherwise.

## ✔️ Constraints

- The string may contain any ASCII characters
- The solution must be case-insensitive
- The solution must ignore non-alphanumeric characters
- You must use recursion to solve this problem

---

## ✅ Example

**Input**: "A man, a plan, a canal: Panama"  
**Output**: 1  
**Explanation**: "amanaplanacanalpanama" is a palindrome

**Input**: "race a car"  
**Output**: 0  
**Explanation**: "raceacar" is not a palindrome

---

## 🧪 Test Cases

| # | Input | Output | Explanation |
|---|-------|--------|-------------|
| 1 | "radar" | 1 | "radar" is a palindrome |
| 2 | "hello" | 0 | "hello" is not a palindrome |
| 3 | "A man, a plan, a canal: Panama" | 1 | Ignore non-alphanumeric and case |
| 4 | "a" | 1 | Single character is palindrome |
| 5 | "Able was I ere I saw Elba" | 1 | Case-insensitive palindrome |

---

## 🛠️ Approach

### Recursive Approach
1. **Base Cases**:
   - If the string has 0 or 1 character, it's a palindrome (return 1)
   - If the first and last characters don't match (case-insensitive), it's not a palindrome (return 0)
2. **Recursive Case**:
   - If the first and last characters match, recursively check the substring that excludes these characters

### Key Insight
- The problem reduces to checking if the first and last characters are the same, then moving inward
- Non-alphanumeric characters should be skipped during comparison
- The solution must be case-insensitive

### Time and Space Complexity
- **Time Complexity**: O(n) - Each character is processed exactly once
- **Space Complexity**: O(n) - Due to the recursion stack (worst case for a palindrome)

---

## 📝 Note
- The solution handles edge cases like empty strings and single-character strings
- Non-alphanumeric characters are ignored during the check
- The comparison is case-insensitive
- The iterative approach would be more space-efficient (O(1) space) but the problem requires recursion
- This is an example of two-pointer technique implemented recursively