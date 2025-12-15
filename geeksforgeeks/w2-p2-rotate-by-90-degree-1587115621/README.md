# Rotate a Matrix by 90 Degrees

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: matrix, rotation, in‑place

---

## 📝 Problem Statement

Given a square matrix `mat` of size `n × n`, rotate the matrix by **90° in the anti‑clockwise direction**, modifying the matrix **in-place** (without using extra space for another matrix). ([geeksforgeeks.org](https://www.geeksforgeeks.org/dsa/inplace-rotate-square-matrix-by-90-degrees/))

---

## 📥 Input

- An integer `n` denoting the size of the square matrix.
- A matrix `mat` of size `n × n`, where each of the next `n` lines contains `n` space-separated integers.

---

## 📤 Output

- The same matrix `mat`, now rotated 90° anti‑clockwise.
- If printing — output the rotated matrix row by row in row-major order; if returning — return the rotated matrix.

---

## ✅ Example

**Input**  
n = 3
mat = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

**Output**  
3 6 9
2 5 8
1 4 7

---

## 🛠️ Approach

One efficient in-place solution (O(n²) time, O(1) extra space) uses two main steps:

1. **Transpose the matrix** (swap `mat[i][j]` with `mat[j][i]` for all i < j).
2. **Reverse each column** (or equivalently **reverse rows then transpose**, depending on convention) — for an anti‑clockwise rotation, the usual method is: transpose, then reverse individual columns. :contentReference[oaicite:2]{index=2}

This transforms rows into columns and reorders elements appropriately to achieve the 90° anti‑clockwise rotation.

---

## 📌 Notes & Constraints

- Works for any integer matrix (positive, negative, zero).
- In-place algorithm — no auxiliary matrix needed.
- **Time Complexity:** O(n²) — each element is visited and swapped a constant number of times.
- **Space Complexity:** O(1) (excluding input storage) — only a few indices / temp variables used.
- Valid for any square matrix size `n ≥ 1`.
