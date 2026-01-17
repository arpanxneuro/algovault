# Multiply Two Polynomials

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: polynomial, math, data‑structure

---

## 📝 Problem Statement

You are given two polynomials represented as arrays of coefficients:

- `A[i]` denotes the coefficient of \(x^i\) in the first polynomial.
- `B[i]` denotes the coefficient of \(x^i\) in the second polynomial.

Compute the product polynomial — i.e., return an array `C` such that each `C[i]` represents the coefficient of \(x^i\) in the product \(A(x) \times B(x)\). The resulting array will have length \(n + m - 1\), where `n` and `m` are lengths of `A` and `B`.

---

## 📥 Input

- `n`: number of coefficients (size) of first polynomial `A[]`
- `A[]`: array of `n` integers — coefficients of the first polynomial
- `m`: number of coefficients (size) of second polynomial `B[]`
- `B[]`: array of `m` integers — coefficients of the second polynomial

(_Note_: On GfG, often the driver passes these arrays directly to a helper function; explicit parsing may vary by language.)

---

## 📤 Output

Return (or print) an array of length `n + m - 1`, containing the coefficients of the product polynomial.

---

## ✅ Example

**Input**  
n = 3
A = [1, 2, 3] // represents 1 + 2x + 3x²
m = 2
B = [4, 5] // represents 4 + 5x
**Output**  
[4, 13, 22, 15] // represents 4 + 13x + 22x² + 15x³

**Explanation:**  
\[
(1 + 2x + 3x^2)\times(4 + 5x) = 4 + 13x + 22x^2 + 15x^3
\]

---

## 🛠️ Approach

Use the classic nested‑loop (convolution) method:

1. Initialize a result array `prod[]` of size `n + m - 1`, filled with zeros.
2. Loop over each coefficient `A[i]`, and for each loop over every coefficient `B[j]`:
   - Update `prod[i + j] += A[i] * B[j]`.
3. Return `prod[]`.

This runs in **O(n \* m)** time and requires **O(n + m)** space for the result (plus O(1) extra).

---

## 📌 Notes & Constraints

- Works even when polynomials have different degrees.
- Handles negative coefficients (if allowed).
- Output array length = `n + m - 1`.
- For large degrees, naive O(n·m) may be slow; advanced methods (e.g. FFT-based) can optimize.
