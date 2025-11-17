# Power of Numbers (Recursive)

> **Difficulty**: Medium  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given a number N and a non-negative integer P, calculate N raised to the power P using recursion. Since the result can be very large, compute it modulo 10^9 + 7.

---

## 📥 Input

- `N`: An integer (1 ≤ N ≤ 10^6)
- `P`: A non-negative integer (0 ≤ P ≤ 10^6)

---

## 📤 Output

Return (N^P) % (10^9 + 7)

## ✔️ Constraints

- The solution must use recursion
- Must handle large numbers efficiently
- Result should be in modulo 10^9 + 7

---

## ✅ Example

**Input**: N = 2, P = 3  
**Output**: 8  
**Explanation**: 2^3 = 8

**Input**: N = 2, P = 5  
**Output**: 32

---

## 🧪 Test Cases

| # | Input (N, P) | Output | Explanation |
|---|--------------|--------|-------------|
| 1 | 2, 3 | 8 | 2^3 = 8 |
| 2 | 3, 4 | 81 | 3^4 = 81 |
| 3 | 5, 0 | 1 | Any number to power 0 is 1 |
| 4 | 100000, 100000 | 754573826 | Large numbers with modulo |
| 5 | 1, 100000 | 1 | 1 to any power is 1 |

---

## 🛠️ Approach

### Recursive Binary Exponentiation
1. **Base Cases**:
   - If P = 0, return 1
   - If P = 1, return N % MOD
2. **Recursive Cases**:
   - If P is even: result = (power(N, P/2) % MOD)² % MOD
   - If P is odd: result = (N % MOD * power(N, P-1) % MOD) % MOD

### Key Insight
- The problem can be solved in O(log P) time using binary exponentiation
- The modulo operation is applied at each step to prevent integer overflow
- The recursion depth is O(log P) due to halving the problem size

### Time and Space Complexity
- **Time Complexity**: O(log P) - The problem size is halved in each recursive call
- **Space Complexity**: O(log P) - Due to the recursion stack

---

## 📝 Note
- The solution handles edge cases like P = 0 and P = 1
- The modulo operation (10^9 + 7) is a large prime number commonly used in programming competitions
- The iterative approach would be more space-efficient (O(1) space)
- For negative exponents, the problem requires additional handling (not covered here)
- This is an example of divide and conquer approach with memoization