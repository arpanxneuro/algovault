# Second Largest

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: array, loop, condition, searching, dsa

---

## 📝 Problem Statement

Given an array of positive integers `arr[]`, return the **second largest distinct element** in the array. If such an element doesn't exist (i.e., all elements are equal), return `-1`.

The second largest element **must not be equal** to the largest.

---

## 📥 Input

- `arr[]`: An array of positive integers
- `n`: Number of elements in the array (2 ≤ n ≤ 10⁵)

---

## 📤 Output

- Return or print the second largest distinct integer in the array.
- If no such distinct second largest exists, return `-1`.

## ✔️ Constraints

- 2 ≤ n ≤ 10⁵
- 1 ≤ arr[i] ≤ 10⁵

---

## ✅ Examples

| Input                    | Output | Explanation                                       |
| ------------------------ | ------ | ------------------------------------------------- |
| `[12, 35, 1, 10, 34, 1]` | `34`   | Largest is `35`, next distinct largest is `34`    |
| `[10, 5, 10]`            | `5`    | Largest is `10`, second distinct largest is `5`   |
| `[10, 10, 10]`           | `-1`   | All elements are equal — no second largest exists |

---

## 🛠️ Approach

Traverse the array once while tracking two variables: `largest` and `secondLargest`.

- Initialize both to a sentinel (e.g. `-1` or minimal value).
- For each element `x`:
  - If `x > largest`, update `secondLargest = largest`, then `largest = x`.
  - Else if `x < largest` and `x > secondLargest`, update `secondLargest = x`.  
    After scanning, `secondLargest` holds the required value (or `-1` when not found).

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

## 📌 Notes

- The algorithm handles duplicates correctly by ensuring the second largest is **strictly less** than the largest.
- Works for large arrays (up to 10⁵ elements), in a single pass.
