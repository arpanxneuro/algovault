# Sum of Digits Using Recursion

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Adobe, TCS

---

## 📝 Problem Statement

Given a non-negative integer N, write a recursive function to calculate the sum of its digits. The function should return the sum of all digits in the number.

---

## 📥 Input

- `N`: A non-negative integer (0 ≤ N ≤ 10^9)

---

## 📤 Output

Return the sum of all digits in N.

## ✔️ Constraints

- 0 ≤ N ≤ 1,000,000,000
- You must use recursion to solve this problem
- The function should return an integer

---

## ✅ Example

**Input**: 1234  
**Output**: 10  
**Explanation**: 1 + 2 + 3 + 4 = 10

**Input**: 999  
**Output**: 27  
**Explanation**: 9 + 9 + 9 = 27

---

## 🧪 Test Cases

| # | Input (N) | Output |
|---|-----------|--------|
| 1 | 0 | 0 |
| 2 | 9 | 9 |
| 3 | 123 | 6 |
| 4 | 1000000000 | 1 |
| 5 | 99999 | 45 |

---

## 🛠️ Approach

### Recursive Approach
1. **Base Case**: If N is a single-digit number, return N itself.
2. **Recursive Case**:
   - Get the last digit using modulo 10: `N % 10`
   - Make a recursive call with the remaining number: `N // 10`
   - Add the last digit to the result of the recursive call

### Key Insight
- The problem can be broken down into smaller subproblems:
  - Sum of digits of N = (last digit of N) + (sum of digits of N without the last digit)
- The recursion continues until we reach a single-digit number (base case)
- The space complexity is O(log n) due to the recursion stack, where n is the number of digits

### Time and Space Complexity
- **Time Complexity**: O(log n) - We process each digit exactly once
- **Space Complexity**: O(log n) - Due to the recursion call stack

---

## 📝 Note
- The solution handles the edge case where N = 0
- For very large numbers (up to 10^9), the recursive approach is efficient
- The number of recursive calls equals the number of digits in N, which is log₁₀N
- This is a classic example of tail recursion, where the recursive call is the last operation