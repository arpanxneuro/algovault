# majority element

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, hashing, two-pointers, Boyer-Moore

---

## 📝 Problem Statement

Given an array `nums` of size `n`, return the **majority element** — the element that appears more than ⌊ n / 2 ⌋ times. You may assume that a majority element always exists in the array.

---

## 📥 Input

An integer array `nums` of size `n`, containing both positive and negative values.

---

## 📤 Output

The **majority element** in the array — the element occurring more than half the time.

## ✔️ Constraints

- `n == nums.length`
- `1 <= n <= 5 × 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- The input guarantees that a majority element always exists.

---

## ✅ Example

**Input**:
`nums = [3,2,3]`
**Output**:
`3`

---

## 🧪 Test Cases

| #   | Input           | Output |
| --- | --------------- | ------ |
| 1   | [3,2,3]         | 3      |
| 2   | [2,2,1,1,1,2,2] | 2      |
| 3   | [5,5,5,1,1]     | 5      |
| 4   | [1]             | 1      |

---

## 🛠️ Approach

### Boyer-Moore Voting Algorithm (Optimal Linear Time, Constant Space)

The **Boyer-Moore Voting Algorithm** maintains a candidate and a count:

1. Initialize `candidate` and `count = 0`.
2. Traverse the array:
   - If `count == 0`, set `candidate = nums[i]` and increment `count`.
   - If `nums[i] == candidate`, increment `count`; otherwise decrement `count`.
3. The `candidate` at the end of this process represents the majority element.

This approach achieves **O(n)** time and **O(1)** extra space.

### Alternative Approaches (Less Optimal)

- **Hash map frequency counting** (O(n) time, O(n) space).
- **Sorting and returning `nums[n // 2]`** (O(n log n) time).

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (for Boyer-Moore)
