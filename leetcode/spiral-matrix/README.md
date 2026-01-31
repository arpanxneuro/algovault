# spiral matrix

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, matrix, simulation, traversal

---

## 📝 Problem Statement

Given an `m x n` matrix, return all the elements of the matrix **in spiral order**.  
The traversal starts at the top-left corner and proceeds clockwise, collecting each element exactly once. :contentReference[oaicite:1]{index=1}

---

## 📥 Input

```
matrix = [[1,2,3],[4,5,6],[7,8,9]]
```

---

## 📤 Output

```
[1,2,3,6,9,8,7,4,5]
```

## ✔️ Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100` :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:

```
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
```

**Output**:

```
[1,2,3,4,8,12,11,10,9,5,6,7]
```

**Explanation**:  
Elements are visited layer by layer, moving right across the top row, down the right column, left across the bottom row, and up the left column, repeating until all elements are visited. :contentReference[oaicite:3]{index=3}

---

## 🧪 Test Cases

| #   | Input                                | Output                         |
| --- | ------------------------------------ | ------------------------------ |
| 1   | `[[1,2,3],[4,5,6],[7,8,9]]`          | `[1,2,3,6,9,8,7,4,5]`          |
| 2   | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | `[1,2,3,4,8,12,11,10,9,5,6,7]` |
| 3   | `[[1]]`                              | `[1]`                          |

---

## 🛠️ Approach

To traverse in spiral order, maintain four boundaries:

- `top`, `bottom` (rows),
- `left`, `right` (columns).

1. Traverse from `left` to `right` on `top`, then increment `top`.
2. Traverse from `top` to `bottom` on `right`, then decrement `right`.
3. If there are remaining rows, traverse from `right` to `left` on `bottom`, then decrement `bottom`.
4. If there are remaining columns, traverse from `bottom` to `top` on `left`, then increment `left`.
5. Repeat until all elements are visited. :contentReference[oaicite:4]{index=4}

This approach visits every element exactly once.

### Time and Space Complexity

- **Time Complexity**: O(m × n) — each element is processed once.
- **Space Complexity**: O(m × n) — due to the output list.
