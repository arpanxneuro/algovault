# Rotate a Matrix by 90 Degrees

Rotate a square matrix `mat` of size `n × n` by **90° in the anti-clockwise direction** without using extra space.

---

## 📝 Problem Statement

Given a matrix `mat`, modify it in-place so that the elements are rotated 90 degrees anti-clockwise. The operation should be done without allocating another matrix of the same size.

---

## 📥 Input

- First line: integer `n` denoting the size of the matrix.
- Next `n` lines: each contains `n` integers describing a row of `mat`.

---

## 📤 Output

- Print the rotated matrix in row-major order or return it from the helper function, depending on the execution environment. For textual explanations, the rows are usually flattened into a single line separated by spaces.

---

## ✔️ Constraints

- `1 ≤ n ≤ 500`
- `-10^3 ≤ mat[i][j] ≤ 10^3`

---

## ✅ Example

**Input**

```
3
1 2 3
4 5 6
7 8 9
```

**Output**

```
3 6 9
2 5 8
1 4 7
```

---

## 🧪 Test Cases

| # | Input | Output |
|---|---|---|
| 1 | `3\n1 2 3\n4 5 6\n7 8 9` | `3 6 9\n2 5 8\n1 4 7` |
| 2 | `2\n1 2\n3 4` | `2 4\n1 3` |

---

## ⏱️ Complexity

- **Time:** `O(n^2)` – every cell is visited once.
- **Space:** `O(1)` – rotation is done in-place.
