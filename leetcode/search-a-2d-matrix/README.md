# search a 2d matrix

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: binary-search, matrix

---

## 📝 Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.  
Your solution **must run in O(log(m \* n)) time complexity**. :contentReference[oaicite:1]{index=1}

---

## 📥 Input

```
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
```

---

## 📤 Output

```
true
```

## ✔️ Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4` :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:

```
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
```

**Output**:

```
false
```

**Explanation**:

The `target` 13 does not exist in the matrix. The matrix can be considered as a sorted list of `m * n` elements, which enables efficient binary search. :contentReference[oaicite:3]{index=3}

---

## 🧪 Test Cases

| #   | Input                                                           | Output  |
| --- | --------------------------------------------------------------- | ------- |
| 1   | `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3`  | `true`  |
| 2   | `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13` | `false` |
| 3   | `matrix = [[1]], target = 1`                                    | `true`  |

---

## 🛠️ Approach

Treat the matrix as a virtually flattened sorted array of size `m * n`. Each possible index `idx` in `[0, m * n - 1]` maps to a matrix position via:

- `row = idx // n`
- `col = idx % n`

Perform a **binary search** over this conceptual flattened range:

1. Initialize `left = 0` and `right = m * n - 1`.
2. While `left <= right`, compute `mid = (left + right) // 2`.
3. Map `mid` to `(row, col)` and compare `matrix[row][col]` with `target`.
4. Adjust the search range accordingly until the element is found or the range is exhausted. :contentReference[oaicite:4]{index=4}

This ensures logarithmic time complexity over all elements. :contentReference[oaicite:5]{index=5}

### Time and Space Complexity

- **Time Complexity**: O(log(m \* n))
- **Space Complexity**: O(1)
