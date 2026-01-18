# single number

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, bit manipulation

---

## 📝 Problem Statement

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. The solution must run in linear time and use only constant extra space.

---

## 📥 Input

An integer array `nums` of length between `1` and `3 * 10^4`, where each element is between `-3 * 10^4` and `3 * 10^4`. Every element appears twice except for one.

---

## 📤 Output

Return the integer that appears only once in the array.

## ✔️ Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Every element in the array appears exactly twice except for one element.

---

## ✅ Example

**Input**:
`nums = [2,2,1]`

**Output**:
`1`

---

**Input**:
`nums = [4,1,2,1,2]`

**Output**:
`4`

---

**Input**:
`nums = [1]`

**Output**:
`1`

---

## 🧪 Test Cases

| #   | Input       | Output |
| --- | ----------- | ------ |
| 1   | [2,2,1]     | 1      |
| 2   | [4,1,2,1,2] | 4      |
| 3   | [1]         | 1      |
| 4   | [5,5,3,3,7] | 7      |

---

## 🛠️ Approach

Use the **bitwise XOR** operation, which has properties that cancel out duplicates:

1. Initialize a variable `result = 0`.
2. For each number `num` in `nums`, do `result ^= num`.
3. After processing all numbers, `result` will be the single number since duplicates XOR to zero.

### Time and Space Complexity

- **Time Complexity**: O(n) — each element is processed once
- **Space Complexity**: O(1) — only a single accumulator variable is used
