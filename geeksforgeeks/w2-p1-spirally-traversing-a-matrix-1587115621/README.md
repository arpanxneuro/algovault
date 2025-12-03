# Spirally Traversing a Matrix

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: array, matrix, implementation

---

## 📝 Problem Statement

Given a matrix `mat[][]` of size `n × m`, return a list of all matrix elements traversed in **clockwise spiral order** — starting from the top‑left corner, moving right across the top row, then downward along the rightmost column, then left across the bottom row, then upward along the leftmost column, and continue layer by layer until all elements are visited. :contentReference[oaicite:2]{index=2}

---

## 📥 Input

- Integers `n`, `m` indicating number of rows and columns respectively.
- A 2D integer matrix `mat` of dimension `n × m`.

---

## 📤 Output

- A one‑dimensional list (or array) of integers representing the elements of `mat`, in the order they are visited during the spiral traversal.

---

## ✅ Example

**Input:**  
n = 3, m = 3
mat = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

**Output:**  
[1, 2, 3, 6, 9, 8, 7, 4, 5]

---

## 🛠️ Approach

One efficient and standard in‑place approach uses boundary‑tracking variables (`top`, `bottom`, `left`, `right`) and iteratively peels off the outer layers of the matrix until all elements are processed:

- Initialize `top = 0`, `bottom = n - 1`, `left = 0`, `right = m - 1`.
- While `top ≤ bottom` and `left ≤ right`:
  1. Traverse from `mat[top][left]` to `mat[top][right]` (left → right) → increment `top`.
  2. Traverse from `mat[top][right]` to `mat[bottom][right]` (top → bottom) → decrement `right`.
  3. If `top ≤ bottom`, traverse from `mat[bottom][right]` to `mat[bottom][left]` (right → left) → decrement `bottom`.
  4. If `left ≤ right`, traverse from `mat[bottom][left]` to `mat[top][left]` (bottom → top) → increment `left`.
- Continue until all elements are visited. :contentReference[oaicite:3]{index=3}

**Time Complexity:** O(n × m) — each element visited exactly once. :contentReference[oaicite:4]{index=4}  
**Space Complexity:** O(1) (ignoring output list) — only a few pointers/indices used. :contentReference[oaicite:5]{index=5}

---

## 📌 Notes

- Works for rectangular matrices (n ≠ m), not just square ones.
- Works for matrices containing any integers (positive, negative, zero).
- Preserves original matrix — only traverses without modifying contents.
