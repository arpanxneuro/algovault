# Second Largest

> **Difficulty**: Basic  
> **Accuracy**:   
> **Submissions**:   
> **Points**: 

---

## 📝 Problem Statement

Given an array of positive integers `arr[]`, return the **second largest distinct element** in the array. If such an element doesn't exist (i.e., all elements are equal), return `-1`.

> The second largest element **must not be equal** to the largest.

---

---

## 📥 Input

- **Array size**: `2 ≤ arr.size() ≤ 10⁵`
- **Array values**: `1 ≤ arr[i] ≤ 10⁵`

---

---

## 📤 Output

Return or print the resulting array or required value.

---

## ✅ Examples

| Input                  | Output | Explanation                                          |
|------------------------|--------|------------------------------------------------------|
| `[12, 35, 1, 10, 34, 1]` | `34`   | `35` is the largest, `34` is the second largest      |
| `[10, 5, 10]`           | `5`    | `10` is the largest, `5` is second largest           |
| `[10, 10, 10]`          | `-1`   | All elements are equal — no second largest           |

---

---

## 🧪 Test Cases

| Input | Value | Output |
|---|---|---|
| `5
1 2 3 4 5` | `90` | `1 2 3 4 5 90` |

**Time Complexity:** O(n)

**Space Complexity:** O(1)
