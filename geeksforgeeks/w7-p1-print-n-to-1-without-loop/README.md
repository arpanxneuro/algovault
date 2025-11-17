# Print N to 1 Without Loop

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Adobe, Goldman Sachs

---

## 📝 Problem Statement

Write a program to print all natural numbers from N to 1 using recursion, without using any loops. The numbers should be printed in descending order, from N down to 1.

---

## 📥 Input

- `N`: A positive integer (1 ≤ N ≤ 10,000)

---

## 📤 Output

Print numbers from N to 1 in descending order, each on a new line.

## ✔️ Constraints

- 1 ≤ N ≤ 10,000
- You must use recursion (no loops allowed)
- The function should not return anything, just print the numbers

---

## ✅ Example

**Input**: 5

**Output**:
```
5
4
3
2
1
```

---


---

## 🧪 Test Cases

| # | Input (N) | Output |
|---|-----------|--------|
| 1 | 1 | `1` |
| 2 | 3 | `3 2 1` |
| 3 | 5 | `5 4 3 2 1` |
| 4 | 10 | `10 9 8 7 6 5 4 3 2 1` |
| 5 | 0 | `(No output, as N must be ≥ 1)` |

---

## 🛠️ Approach

### Recursive Approach
1. **Base Case**: If N is less than 1, return (stop the recursion).
2. **Recursive Case**:
   - Print the current number N.
   - Make a recursive call with N-1.

### Key Insight
- The function calls are stored in the call stack, which implicitly creates a LIFO (Last In, First Out) structure.
- The printing happens before the recursive call, ensuring the numbers are printed in descending order.
- The space complexity is O(n) due to the maximum depth of the recursion stack.

### Time and Space Complexity
- **Time Complexity**: O(n) - We make exactly n recursive calls.
- **Space Complexity**: O(n) - Due to the recursion call stack (implicit memory usage).

---

## 📝 Note
- The solution handles the edge case where N = 1.
- For very large values of N (close to 10,000), be aware of the recursion depth limit in some programming languages.
- This is a classic example of head recursion where the recursive call is not the last operation in the function.