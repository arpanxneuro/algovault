# Multiply Two Polynomials

Multiply two polynomials represented as coefficient arrays (from constant term upward) and return the resulting polynomial.

---

## 📝 Problem Statement

Given two arrays `A` and `B`, where `A[i]` is the coefficient of `x^i`, compute the product polynomial `C(x) = A(x) * B(x)`. The resulting array should have `n + m - 1` entries.

---

## 📥 Input

- `n`: number of coefficients for the first polynomial.
- `n` integers describing `A`.
- `m`: number of coefficients for the second polynomial.
- `m` integers describing `B`.

Driver code on GeeksforGeeks typically passes these arrays directly, so parsing may already be handled.

---

## 📤 Output

Return or print an array of length `n + m - 1` containing coefficients of the product polynomial.

---

## ✔️ Constraints

- `1 ≤ n, m ≤ 200`
- `-10^3 ≤ coefficient ≤ 10^3`

---

## ✅ Example

**Input**

```
n = 3
A = [1, 2, 3]
m = 2
B = [4, 5]
```

**Output**

```
[4, 13, 22, 15]
```

**Explanation:** `(1 + 2x + 3x^2) * (4 + 5x) = 4 + 13x + 22x^2 + 15x^3`.

---

## 🧪 Test Cases

| # | A | B | Output |
|---|---|---|---|
| 1 | `[2, 0, 3]` | `[1, 1]` | `[2, 2, 3, 3]` |
| 2 | `[5]` | `[3, -2]` | `[15, -10]` |

---

## ⏱️ Complexity

- **Time:** `O(n * m)` – naive convolution.
- **Space:** `O(n + m)` – result array.
