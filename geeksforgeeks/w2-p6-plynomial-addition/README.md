# Polynomial Addition

Add two polynomials represented by arrays of coefficients (lowest power to highest). Return the resulting polynomial after adding matching powers.

---

## 📝 Problem Statement

Given two arrays `A` and `B`, where `A[i]` and `B[i]` denote the coefficient of `x^i`, compute another array `C` such that `C[i] = A[i] + B[i]`. If one polynomial has fewer terms, treat the missing coefficients as zero.

---

## 📥 Input

- `n`: number of coefficients in the first polynomial.
- `n` integers: coefficients of the first polynomial.
- `m`: number of coefficients in the second polynomial.
- `m` integers: coefficients of the second polynomial.

The driver code on GeeksforGeeks passes these arrays directly to the helper function, so manual input parsing is usually unnecessary.

---

## 📤 Output

Return an array (or print a list) of coefficients representing the sum polynomial. The length should be `max(n, m)`.

---

## ✔️ Constraints

- `1 ≤ n, m ≤ 10^3`
- `-10^4 ≤ coefficient ≤ 10^4`

---

## ✅ Example

**Input**

```
n = 3
A = [1, 2, 3]   // 1 + 2x + 3x^2
m = 2
B = [4, 5]      // 4 + 5x
```

**Output**

```
[5, 7, 3]
```

**Explanation:** `C(x) = (1 + 4) + (2 + 5)x + 3x^2 = 5 + 7x + 3x^2`.

---

## 🧪 Test Cases

| # | A | B | Output |
|---|---|---|---|
| 1 | `[1, 0, 3]` | `[2, 5, 1]` | `[3, 5, 4]` |
| 2 | `[5, -2]` | `[3]` | `[8, -2]` |

---

## ⏱️ Complexity

- **Time:** `O(max(n, m))`
- **Space:** `O(max(n, m))` for the result array (or `O(1)` extra if reusing one array)
