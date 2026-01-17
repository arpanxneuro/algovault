# Two Sum

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, hash-table, two-pointers

---

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return _indices_ of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

---

## 📥 Input

- `nums`: An array of integers (2 ≤ nums.length ≤ 10⁴)
  - Each element nums[i] is an integer (-10⁹ ≤ nums[i] ≤ 10⁹)
- `target`: An integer (-10⁹ ≤ target ≤ 10⁹)

---

## 📤 Output

- Return an array `[i, j]` where `nums[i] + nums[j] == target`
- The order of the indices does not matter
- The solution is guaranteed to exist and be unique

## ✔️ Constraints

- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- Only one valid answer exists

---

## ✅ Example

**Input:**

```nums = [2, 7, 11, 15]
target = 9
```

**Output:**  
`[0, 1]`
**Explanation:**  
`nums[0] + nums[1] = 2 + 7 = 9`

**Input:**

```nums = [3, 2, 4]
target = 6
```

**Output:**  
`[1, 2]`
**Input:**

```nums = [3, 3]
target = 6
```

**Output:**  
`[0, 1]`
**Input:**

```nums = [-1, -2, -3, -4, -5]
target = -8
```

**Output:**  
`[2, 4]`

---

## 🧪 Test Cases

| #   | Input                  | Output  |
| --- | ---------------------- | ------- |
| 1   | `[2,7,11,15], 9`       | `[0,1]` |
| 2   | `[3,2,4], 6`           | `[1,2]` |
| 3   | `[3,3], 6`             | `[0,1]` |
| 4   | `[-1,-2,-3,-4,-5], -8` | `[2,4]` |

---

## 🛠️ Approach

- Use a hash table to store numbers and their indices.
- Traverse the array: for each element `num`, check if `target - num` exists in the hash table.
- If it exists, return the indices `[hash[target-num], currentIndex]`.
- Otherwise, store `num` with its index in the hash table.

---

### Time and Space Complexity

- **Time Complexity:** O(n) — single pass through the array, constant-time hash table lookups
- **Space Complexity:** O(n) — hash table stores at most n elements
