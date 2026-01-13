# single element in a sorted array

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, binary-search

---

## 📝 Problem Statement

You are given a sorted array consisting only of integers where every element appears exactly twice, except for one element which appears exactly once. Return the **single element** that appears only once. Your solution must run in **O(log n)** time and **O(1)** space. ([LeetCodee](https://leetcodee.com/problems/single-element-in-a-sorted-array/?utm_source=chatgpt.com)) :contentReference[oaicite:0]{index=0}

---

## 📥 Input

An integer array `nums` containing pairs of identical elements and exactly one unique element. :contentReference[oaicite:1]{index=1}

---

## 📤 Output

Return the **single element** in the array that does not have a matching duplicate. :contentReference[oaicite:2]{index=2}

## ✔️ Constraints

- `1 <= nums.length <= 10⁵`
- `0 <= nums[i] <= 10⁵`
- Every element except one appears exactly twice.
- The array is sorted in ascending order. :contentReference[oaicite:3]{index=3}

---

## ✅ Example

**Input**:
nums = [1,1,2,3,3,4,4,8,8]

**Output**:
2

**Input**:
nums = [3,3,7,7,10,11,11]

**Output**:
10

---

## 🧪 Test Cases

| #   | Input               | Output |
| --- | ------------------- | ------ |
| 1   | [1,1,2,3,3,4,4,8,8] | 2      |
| 2   | [3,3,7,7,10,11,11]  | 10     |
| 3   | [0,0,1]             | 1      |
| 4   | [5,5,6,6,7,8,8]     | 7      |

---

## 🛠️ Approach

To achieve **O(log n)** runtime with **O(1)** space, apply a **binary search pattern** that exploits the sorted property and pairing structure:

1. Initialize `left = 0` and `right = nums.length - 1`.
2. While `left < right`:
   - Compute `mid = left + (right - left) // 2`.
   - If `mid` is odd, decrement it by 1 to ensure it lands on the first element of a potential pair.
   - If `nums[mid] == nums[mid + 1]`, the unique element must be to the right — set `left = mid + 2`.
   - Otherwise the unique element is at or to the left — set `right = mid`.
3. When the loop ends, `nums[left]` is the unique element. :contentReference[oaicite:4]{index=4}

### Time and Space Complexity

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
