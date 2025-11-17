# GCD of Two Numbers (Recursive)

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Adobe, Goldman Sachs

---

## 📝 Problem Statement

Write a recursive function to find the Greatest Common Divisor (GCD) of two non-negative integers. The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

---

## 📥 Input

- `A`: First non-negative integer (0 ≤ A ≤ 10^9)
- `B`: Second non-negative integer (0 ≤ B ≤ 10^9)

---

## 📤 Output

Return the GCD of A and B.

## ✔️ Constraints

- At least one of A or B must be non-zero
- The solution must use recursion
- The function should handle large inputs efficiently

---

## ✅ Example

**Input**: A = 24, B = 36  
**Output**: 12  
**Explanation**: The divisors of 24 are 1,2,3,4,6,8,12,24 and of 36 are 1,2,3,4,6,9,12,18,36. The greatest common divisor is 12.

**Input**: A = 35, B = 10  
**Output**: 5

---

## 🧪 Test Cases

| # | Input (A, B) | Output | Explanation |
|---|--------------|--------|-------------|
| 1 | 0, 5 | 5 | GCD(0,5) = 5 |
| 2 | 13, 13 | 13 | GCD of same numbers |
| 3 | 24, 36 | 12 | GCD using Euclidean algorithm |
| 4 | 1000000000, 1 | 1 | Large number with 1 |
| 5 | 0, 0 | 0 | Special case (mathematically undefined, but return 0) |

---

## 🛠️ Approach

### Euclidean Algorithm (Recursive)
1. **Base Case**: If B = 0, return A
2. **Recursive Case**: Return GCD(B, A mod B)

### Key Insight
- The Euclidean algorithm is based on the principle that the GCD of two numbers also divides their difference
- The algorithm reduces the problem size in each recursive call
- The time complexity is O(log(min(A,B))) which is very efficient

### Time and Space Complexity
- **Time Complexity**: O(log(min(A,B))) - The number of recursive calls is proportional to the number of digits in the smaller number
- **Space Complexity**: O(log(min(A,B))) - Due to the recursion stack

---

## 📝 Note
- The solution handles the case where one of the numbers is 0
- For A = B = 0, the result is 0 (though mathematically undefined)
- The iterative implementation would be more space-efficient (O(1) space)
- This is an example of tail recursion, which some compilers can optimize
- The algorithm works for negative numbers by taking absolute values