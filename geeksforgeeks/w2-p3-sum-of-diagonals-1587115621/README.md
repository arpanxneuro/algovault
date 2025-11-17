# Sum of Diagonals

Compute the sum of the **principal diagonal** elements of a square matrix `M` of size `N × N`.

---

## 📝 Problem Statement

Given `N` and an `N × N` matrix `M`, calculate the sum of all elements `M[i][i]` where the row and column indices are equal. You only need to consider the main diagonal (top-left to bottom-right).

---

## 📥 Input

- First line: integer `T` representing the number of test cases (optional based on platform wrapper).
- For each test case:
  - Integer `N` – the dimension of the matrix.
  - `N` lines follow, each containing `N` integers describing the matrix row.

---

## 📤 Output

- For each test case, output the sum of the principal diagonal elements.

---

## ✔️ Constraints

- `1 ≤ N ≤ 500`
- `-10^3 ≤ M[i][j] ≤ 10^3`

---

## ✅ Example

**Input**

```
1
3
1 2 3
4 5 6
7 8 9
```

**Output**

```
15
```

**Explanation:** The diagonal elements are `1, 5, 9`. Their sum is `15`.

---

## 🧪 Test Cases

| # | Input | Output |
|---|---|---|
| 1 | `3\n1 2 3\n4 5 6\n7 8 9` | `15` |
| 2 | `2\n5 7\n3 4` | `9` |

---

## ⏱️ Complexity

- **Time:** `O(N)` – only `N` diagonal entries are summed.
- **Space:** `O(1)` – constant auxiliary space.
