# remove duplicates from sorted array

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, two pointers

---

## 📝 Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates _in-place_ such that each unique element appears only once and the relative order of the elements is preserved. After modifying the array, return _k_, the number of unique elements. The first _k_ elements of `nums` should contain the unique values. It does not matter what is left beyond index `k-1`. You must achieve this with _O(1)_ extra memory.

---

## 📥 Input

A sorted integer array `nums` of length between `1` and `3 * 10^4`, where each element is in the range `[-100, 100]`. Every duplicate element appears consecutively due to the array being sorted.

---

## 📤 Output

Returns an integer _k_, the number of unique elements after removing duplicates in place. The first _k_ positions of `nums` must hold the unique values.

## ✔️ Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- The array `nums` is sorted in non-decreasing order.
- Modify the array in place with constant extra memory.

---

## ✅ Example

**Input**:

```
nums = [1,1,2]
```

**Output**:

```
2, nums = [1,2,_]
```

**Explanation**:  
Return `k = 2`. The first two elements of `nums` are now the unique elements `1` and `2`. The values after index `k-1` can be ignored.

---

**Input**:
`nums = [0,0,1,1,1,2,2,3,3,4]`

**Output**:
`5, nums = [0,1,2,3,4,,,,,_]`

**Explanation**:  
Return `k = 5`. The unique values in sorted order are `0,1,2,3,4`.

---

## 🧪 Test Cases

| #   | Input                 | Output |
| --- | --------------------- | ------ |
| 1   | [1,1,2]               | 2      |
| 2   | [0,0,1,1,1,2,2,3,3,4] | 5      |
| 3   | [2,2,2]               | 1      |
| 4   | [1,2,3,4]             | 4      |

---

## 🛠️ Approach

Use a **two-pointer technique**:

1. Initialize a slow pointer `i` at index `0`.
2. Iterate a fast pointer `j` from index `1` to end.
3. Whenever `nums[j] != nums[i]`, increment `i` and set `nums[i] = nums[j]`.
4. At the end, `i + 1` is the count of unique elements.

This works because the array is sorted, so all duplicates are grouped, and overwriting them in place with new values ensures the unique elements accumulate at the front.

### Time and Space Complexity

- **Time Complexity**: O(n) — traverse the array once
- **Space Complexity**: O(1) — constant extra memory
