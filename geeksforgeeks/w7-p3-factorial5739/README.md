# Factorial Using Recursion

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Adobe, Goldman Sachs

---

## 📝 Problem Statement

Write a recursive function to calculate the factorial of a non-negative integer N. The factorial of N (denoted as N!) is the product of all positive integers less than or equal to N.

**Note**: 0! is defined as 1.

---

## 📥 Input

- `N`: A non-negative integer (0 ≤ N ≤ 20)

---

## 📤 Output

Return the factorial of N.

## ✔️ Constraints

- 0 ≤ N ≤ 20 (to prevent integer overflow in 64-bit signed integers)
- You must use recursion to solve this problem
- The function should return a 64-bit integer

---

## ✅ Example

**Input**: 5  
**Output**: 120  
**Explanation**: 5! = 5 × 4 × 3 × 2 × 1 = 120

**Input**: 0  
**Output**: 1  
**Explanation**: By definition, 0! = 1

---

## 🧪 Test Cases

| # | Input (N) | Output (N!) |
|---|-----------|-------------|
| 1 | 0 | 1 |
| 2 | 1 | 1 |
| 3 | 5 | 120 |
| 4 | 10 | 3628800 |
| 5 | 20 | 2432902008176640000 |

---

## 🛠️ Approach

### Recursive Approach
1. **Base Case**: 
   - If N = 0 or N = 1, return 1
2. **Recursive Case**:
   - Return N * factorial(N-1)

### Key Insight
- The problem can be broken down into smaller subproblems:
  - N! = N × (N-1)!
- The recursion continues until it reaches the base case (N = 0 or 1)
- The space complexity is O(n) due to the recursion stack depth

### Time and Space Complexity
- **Time Complexity**: O(n) - We make exactly n recursive calls
- **Space Complexity**: O(n) - Due to the recursion call stack

---

## 📝 Note
- The solution handles the edge case where N = 0
- For N > 20, the result may exceed the maximum value of a 64-bit signed integer (2^63 - 1)
- This is a classic example of linear recursion where each call makes exactly one recursive call
- The iterative approach would have O(1) space complexity but the problem specifically requires recursion