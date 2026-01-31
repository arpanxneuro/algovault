# search a d matrix ii

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, matrix, binary search, two pointers, divide and conquer

---

## 📝 Problem Statement

Write an efficient algorithm that searches for a value `target` in an `m x n` integer `matrix`.  
This matrix has the following properties:

- Integers in each row are sorted in ascending order from left to right.
- Integers in each column are sorted in ascending order from top to bottom. :contentReference[oaicite:1]{index=1}

Return `true` if `target` is found in the matrix, and `false` otherwise. :contentReference[oaicite:2]{index=2}

---

## 📥 Input

```
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
```

---

## 📤 Output

```
true
```

## ✔️ Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `-10^9 <= matrix[i][j], target <= 10^9`
- The integers in each row and column are sorted as described above. :contentReference[oaicite:3]{index=3}

---

## ✅ Example

**Input**:

```
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
```

**Output**:

```
false
```

**Explanation**:  
The given `target` value does not exist in the sorted 2D matrix structure. :contentReference[oaicite:4]{index=4}

---

## 🧪 Test Cases

| #   | Input                  | Output         |
| --- | ---------------------- | -------------- |
| 1   | matrix with target 5   | `true`         |
| 2   | matrix with target 20  | `false`        |
| 3   | matrix with single row | `true`/`false` |

---

## 🛠️ Approach

To search efficiently given both row and column sorted properties:

1. Start at the **top-right** corner of the matrix (row = 0, col = n − 1).
2. At each step:
   - If the current value equals `target`, return `true`.
   - If the current value is greater than `target`, move left (`col–`).
   - If the current value is less than `target`, move down (`row++`).
3. Continue until you either find `target` or exit the matrix bounds. :contentReference[oaicite:5]{index=5}

This strategy eliminates either a row or a column at every step, yielding a linear time search relative to dimensions.

### Time and Space Complexity

- **Time Complexity**: O(m + n) — each step removes one row or one column.
- **Space Complexity**: O(1) — constant auxiliary memory.

---

## 🧾 Notes

- This problem differs from _Search a 2D Matrix I_ because the matrix is not flattened in a single globally sorted array — only rows and columns are locally sorted. :contentReference[oaicite:6]{index=6}
