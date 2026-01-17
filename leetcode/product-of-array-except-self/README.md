# product of array except self

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, prefix-suffix, product

---

## 📝 Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must **not use the division operation** and the algorithm must run in **O(n)** time. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

---

## 📥 Input

- An integer array `nums`
- `2 <= nums.length <= 10⁵`
- `-30 <= nums[i] <= 30`

---

## 📤 Output

Return an array `answer` of the same length where `answer[i]` is the product of all elements in `nums` except `nums[i]`.

## ✔️ Constraints

- You cannot use division.
- You must achieve **O(n)** time complexity.
- The product of any prefix or suffix will fit in a 32-bit integer.

---

## ✅ Example

**Input**:
nums = [1,2,3,4]

**Output**:
[24,12,8,6]

---

## 🧪 Test Cases

| #   | Input         | Output      |
| --- | ------------- | ----------- |
| 1   | [1,2,3,4]     | [24,12,8,6] |
| 2   | [-1,1,0,-3,3] | [0,0,9,0,0] |
| 3   | [1,0,2,3]     | [0,6,0,0]   |
| 4   | [2,5]         | [5,2]       |

---

## 🛠️ Approach

To meet the **O(n)** requirement without using division, use a **prefix-suffix product technique**. Compute products of elements to the left and right of each index and multiply them:

1. First pass (left-to-right): compute left cumulative product for each index and store in the result array.
2. Second pass (right-to-left): maintain a running suffix product and multiply it into the result array.
3. This achieves the final product for each index without division.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (excluding the output array)
