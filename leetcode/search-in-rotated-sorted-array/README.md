# search in rotated sorted array

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, binary-search, rotated

---

## 📝 Problem Statement

There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`. For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the **index of `target`** if it is in `nums`, or **`-1`** if it is not in `nums`. You must write an algorithm with **O(log n)** runtime complexity.

---

## 📥 Input

- A rotated sorted integer array `nums`
- An integer `target` to find within the array

---

## 📤 Output

Return the **index** of `target` in `nums`, or **`-1`** if `target` is not present.

## ✔️ Constraints

- `1 <= nums.length <= 5000`
- `-10⁴ <= nums[i] <= 10⁴`
- All values of `nums` are unique
- `nums` is an ascending array that is possibly rotated
- `-10⁴ <= target <= 10⁴`

---

## ✅ Example

**Input**:
nums = [4,5,6,7,0,1,2], target = 0

**Output**:
4

**Input**:
nums = [4,5,6,7,0,1,2], target = 3

**Output**:
-1

**Input**:
nums = [1], target = 0

**Output**:
-1

---

## 🧪 Test Cases

| #   | Input                              | Output |
| --- | ---------------------------------- | ------ |
| 1   | nums = [4,5,6,7,0,1,2], target = 0 | 4      |
| 2   | nums = [4,5,6,7,0,1,2], target = 3 | -1     |
| 3   | nums = [1], target = 0             | -1     |
| 4   | nums = [5,1,3], target = 3         | 2      |

---

## 🛠️ Approach

Use a **modified binary search** to achieve **O(log n)** time complexity. At every iteration, compute `mid` and determine which side of the array is sorted. If the left side is sorted and the target lies within it, adjust `right`; otherwise adjust `left`. If the right side is sorted and the target lies within it, adjust `left`; otherwise adjust `right`. Continue until the target is found or the search range is exhausted.

### Time and Space Complexity

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
