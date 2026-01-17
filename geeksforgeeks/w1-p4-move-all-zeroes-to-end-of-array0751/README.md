# Move All Zeroes to End of Array

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: array, list, loop, condition

---

## 📝 Problem Statement

You are given an array `arr[]` of integers. Your task is to **move all the zeroes to the end of the array**, while maintaining the **relative order of the non-zero elements**. The modification must be done **in-place** (i.e. without using extra array space).

---

## 📥 Input

- `arr[]`: An array of integers (may include zeros)
- `n`: Number of elements in the array

---

## 📤 Output

- The array after reordering — all non-zero elements appear in original relative order, followed by all zeros.

## ✔️ Constraints

- Array size and element constraints depend on problem/platform limits.

---

## ✅ Examples

| Input                            | Output                                                           |
| -------------------------------- | ---------------------------------------------------------------- |
| `arr = [1, 2, 0, 4, 3, 0, 5, 0]` | `[1, 2, 4, 3, 5, 0, 0, 0]` |
| `arr = [10, 20, 30]`             | `[10, 20, 30]`             |
| `arr = [0, 0]`                   | `[0, 0]`                   |

---

## 🛠️ Approach

One efficient in-place approach:

- Maintain a pointer `count = 0` to track the position to place the next non-zero element.
- Traverse the array from start to end: whenever you encounter a non-zero element `arr[i]`, assign it to `arr[count]`, then increment `count`.
- After processing all elements, from index `count` to end of the array, set the remaining positions to `0`.

### Complexity

- **Time Complexity**: O(n) — single pass to shift non-zero elements + one pass to fill zeros.
- **Space Complexity**: O(1) — in-place algorithm without extra array.

---

## 📌 Notes

- The algorithm preserves the relative order of non-zero elements.
- Works for arrays containing no zeros, all zeros, or mixture of zeros and non-zeros.
