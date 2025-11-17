# Fibonacci Series Up to Nth Term

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Adobe, Oracle

---

## 📝 Problem Statement

Generate the first N terms of the Fibonacci sequence using recursion. The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

---

## 📥 Input

- `N`: A positive integer (1 ≤ N ≤ 50)

---

## 📤 Output

Return a list/array containing the first N terms of the Fibonacci sequence.

## ✔️ Constraints

- 1 ≤ N ≤ 50
- You must use recursion to solve this problem
- The function should return a list/array of integers

---

## ✅ Example

**Input**: 5  
**Output**: [0, 1, 1, 2, 3]

**Input**: 8  
**Output**: [0, 1, 1, 2, 3, 5, 8, 13]

---

## 🧪 Test Cases

| # | Input (N) | Output |
|---|-----------|--------|
| 1 | 1 | [0] |
| 2 | 2 | [0, 1] |
| 3 | 5 | [0, 1, 1, 2, 3] |
| 4 | 10 | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] |
| 5 | 15 | [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377] |

---

## 🛠️ Approach

### Recursive Approach with Memoization
1. **Base Cases**:
   - If N = 1, return [0]
   - If N = 2, return [0, 1]
2. **Recursive Case**:
   - Get the previous Fibonacci sequence up to N-1 terms
   - Calculate the next term as the sum of the last two terms
   - Append the new term to the sequence and return

### Key Insight
- The naive recursive approach has exponential time complexity (O(2^n)) due to repeated calculations
- Using memoization or storing previously computed terms reduces the time complexity to O(n)
- The space complexity is O(n) for both the result array and the recursion stack

### Time and Space Complexity
- **Time Complexity**: O(n) - With memoization, each term is computed exactly once
- **Space Complexity**: O(n) - For storing the result and recursion stack

---

## 📝 Note
- The solution handles the edge cases where N = 1 or N = 2
- For N > 50, the numbers become very large (F(50) = 12,586,269,025)
- The iterative approach would be more space-efficient (O(1) space) but the problem requires recursion
- This is a classic example of multiple recursion where each call makes two recursive calls