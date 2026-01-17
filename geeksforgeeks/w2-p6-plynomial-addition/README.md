# Polynomial Addition

> **Difficulty**: medium  
> **Platform**: GeeksforGeeks  
> **Tags**: polynomial, math, data‑structure

---

## 📝 Problem Statement

You are given two polynomials represented by arrays of coefficients:

- `A[i]` denotes coefficient of \(x^i\) in the first polynomial.
- `B[i]` denotes coefficient of \(x^i\) in the second polynomial.

Compute the sum polynomial — i.e., return an array `C` where for each power \(i\),  
C[i] = A[i] + B[i]
If one polynomial has fewer coefficients (i.e. lower maximum degree), treat missing coefficients as 0.

---

## 📥 Input

- `n` — number of coefficients in the first polynomial
- `A[]` — array of `n` integers (coefficients of polynomial A)
- `m` — number of coefficients in the second polynomial
- `B[]` — array of `m` integers (coefficients of polynomial B)

_Note: On GeeksforGeeks the driver may directly pass arrays — manual parsing may or may not be required depending on the language._

---

## 📤 Output

- Return (or print) an array of length `max(n, m)` — coefficients of the sum polynomial.

---

## ✅ Example

**Input:**  
n = 3
A = [1, 2, 3] // represents 1 + 2x + 3x^2
m = 2
B = [4, 5] // represents 4 + 5x

**Output:**  
[5, 7, 3] // represents 5 + 7x + 3x^2

**Explanation:**

- Constant term: 1 + 4 = 5
- x¹ term: 2 + 5 = 7
- x² term: 3 + 0 = 3

---

## 🛠️ Approach

1. Determine `size = max(n, m)` — the degree (plus one) of resultant polynomial.
2. Initialize result array `sum[]` of length `size`, initially copying coefficients from `A[]` (for indices < n).
3. For each index `i < m`, add `B[i]` to `sum[i]`.
4. Return `sum[]`.

This runs in **O(max(n, m))** time and uses **O(max(n, m))** space for output (or O(1) extra space if allowed to modify one input).

---

## 📌 Notes

- Works when polynomials have different degrees — missing higher-order coefficients are treated as zero.
- Output length equals the higher degree polynomial’s length.
- Negative coefficients allowed, if input has them.
