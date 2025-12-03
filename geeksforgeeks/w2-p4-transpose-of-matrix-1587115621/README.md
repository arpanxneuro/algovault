# Transpose of Matrix

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: matrix, data structure, transpose

---

## 📝 Problem Statement

Given a matrix `mat[][]` of size `n × n` (square matrix), compute its **transpose** — i.e., produce a matrix where rows are converted to columns and columns to rows. For a square matrix, transpose can be done **in‑place** by swapping `mat[i][j]` with `mat[j][i]`. :contentReference[oaicite:2]{index=2}

---

## 📥 Input

- Integer `n`: dimension of the square matrix
- Next `n` lines: each line contains `n` integers — the `i`‑th row of the matrix

---

## 📤 Output

- The transposed matrix (of same dimension `n × n`) — either returned by a function or printed row by row depending on problem setup

---

## ✅ Example

**Input**  
n = 2
mat = [
[1, 2],
[9, -2]
]

**Output**  
[
[1, 9],
[2, -2]
]

**Explanation**: Elements at position (i, j) are moved to (j, i), converting rows into columns. :contentReference[oaicite:3]{index=3}

---

## 🛠️ Approach

For square matrix of size `n`:

- Loop with two indices `i` from `0` to `n-1`, and `j` from `i+1` to `n-1`
- Swap `mat[i][j]` and `mat[j][i]` — this mirrors elements over the main diagonal (top‑left to bottom‑right) :contentReference[oaicite:4]{index=4}
- After these swaps, `mat` becomes its transpose — rows ↔ columns swapped, in-place, no extra matrix required

**Time Complexity:** O(n²)  
**Space Complexity:** O(1) (in-place) :contentReference[oaicite:5]{index=5}

---

## 📌 Notes

- This in-place transpose works only when the matrix is square — for non‑square (rectangular) matrices, a separate resultant matrix must be created. :contentReference[oaicite:6]{index=6}
- Works for any integer entries (positive, negative, zero).
- Efficient for large matrices within memory constraints thanks to in-place operation.
