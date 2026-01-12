# search insert position

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, binary-search

---

## 📝 Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with **O(log n)** runtime complexity. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

- A sorted array `nums` of distinct integers  
- An integer `target` value :contentReference[oaicite:1]{index=1}

---

## 📤 Output

Return the **index** of the first occurrence of `target` if found; otherwise, return the index where it would be inserted in order. :contentReference[oaicite:2]{index=2}

## ✔️ Constraints

- `1 <= nums.length <= 10^4`  
- `-10^4 <= nums[i] <= 10^4`  
- `nums` contains distinct values sorted in ascending order  
- `-10^4 <= target <= 10^4` :contentReference[oaicite:3]{index=3}

---

## ✅ Example

**Input**:
nums = [1,3,5,6], target = 5

**Output**:
2

**Input**:
nums = [1,3,5,6], target = 2

**Output**:
1

**Input**:
nums = [1,3,5,6], target = 7

**Output**:
4

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | nums = [1,3,5,6], target = 5 | 2 |
| 2 | nums = [1,3,5,6], target = 2 | 1 |
| 3 | nums = [1,3,5,6], target = 7 | 4 |
| 4 | nums = [1,3,5,6], target = 0 | 0 |

---

## 🛠️ Approach

To achieve **O(log n)** runtime, use **binary search** on the sorted array. Maintain pointers `left` and `right` for the search range. Compute the midpoint; if the value at `mid` equals the target, return `mid`. If it’s less than the target, search the right half; if greater, search the left half. When the loop finishes without finding the target, the `left` pointer indicates the correct insertion position. :contentReference[oaicite:4]{index=4}

### Time and Space Complexity
- **Time Complexity**: O(log n)  
- **Space Complexity**: O(1)

