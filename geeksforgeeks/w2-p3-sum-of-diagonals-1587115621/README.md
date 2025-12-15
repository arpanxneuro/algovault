# Sum of Diagonals

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: matrix, diagonal, math

---

## 📝 Problem Statement

Given a square matrix `M` of size `N × N`, compute the sum of all elements on its **principal (main) diagonal** (i.e. elements where row index = column index). Optionally, one can also consider the secondary diagonal — elements where row index + column index = N − 1. For this version, we focus on the **principal diagonal** sum.

---

## 📥 Input

- An integer `N` denoting the size of the square matrix.
- Followed by `N` lines each containing `N` space‑separated integers — the rows of the matrix.

If multiple test cases: first line may contain `T`, number of test cases (depends on problem wrapper).

---

## 📤 Output

- For each test case: output the sum of the principal diagonal elements of the matrix.

---

## ✅ Example

**Input**
1 # number of test cases (optional)
3 # N
1 2 3
4 5 6
7 8 9

**Output**  
15

**Explanation**: Principal diagonal elements are `1, 5, 9`. Their sum = `15`.

---

## 🛠️ Approach

Traverse the matrix row by row. Maintain a running sum `diagSum`. For each row `i` (0‑based or 1‑based as per implementation), add `M[i][i]` to `diagSum`. After processing all rows, output `diagSum`.

**Time Complexity:** O(N) — only one pass over diagonal entries.  
**Space Complexity:** O(1) — constant extra space.

This is the standard method to compute the “trace” of a square matrix. :contentReference[oaicite:2]{index=2}
