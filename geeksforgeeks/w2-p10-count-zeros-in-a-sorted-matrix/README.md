# Count Zeros in a Sorted Matrix

Count the total number of zeros in an `n × m` binary matrix where each row is sorted (all 0s precede 1s).

---

## 📝 Problem Statement

Given a matrix `mat` of size `n × m` such that each row is sorted in non-decreasing order, determine how many entries are equal to zero. The typical solution uses a staircase traversal from the top-right corner to achieve linear time.

---

## 📥 Input

- `n` and `m`: number of rows and columns.
- Followed by `n` rows, each containing `m` binary values (`0` or `1`).

On GeeksforGeeks, the matrix is passed directly to the helper function.

---

## 📤 Output

Return an integer indicating how many cells contain zero.

---

## ✔️ Constraints

- `1 ≤ n, m ≤ 10^3`
- Matrix rows are individually sorted.

---

## ✅ Example

**Input**

```
3 4
0 0 1 1
0 0 0 1
0 1 1 1
```

**Output**

```
7
```

**Explanation:** There are seven zeros across the three rows.

---

## 🧪 Test Cases

| # | Matrix | Zero Count |
|---|---|---|
| 1 | `[[0,0,1],[0,1,1]]` | `3` |
| 2 | `[[0,0,0],[0,0,0]]` | `6` |

---

## ⏱️ Complexity

- **Time:** `O(n + m)` using top-right traversal (or `O(n·m)` for brute force).
- **Space:** `O(1)` extra.
