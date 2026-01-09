# remove element

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, two-pointers, in-place

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`. To get accepted, you need to do the following:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`.
- The remaining elements of `nums` are not important.
- Return `k`. :contentReference[oaicite:1]{index=1}

---

## 📥 Input

- An integer array `nums`
- An integer `val` to remove

---

## 📤 Output

- An integer `k` representing the count of elements not equal to `val`, with the first `k` positions of `nums` holding those elements. :contentReference[oaicite:2]{index=2}

## ✔️ Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100` :contentReference[oaicite:3]{index=3}

---

## ✅ Example

**Input**:
nums = [3,2,2,3], val = 3

**Output**:
2, nums = [2,2,_,_]

**Explanation**:
Your function should return `k = 2`, with the first two elements of `nums` being 2. It does not matter what you leave beyond the returned `k`. :contentReference[oaicite:4]{index=4}

---

## 🧪 Test Cases

| #   | Input                             | Output |
| --- | --------------------------------- | ------ |
| 1   | nums = [3,2,2,3], val = 3         | 2      |
| 2   | nums = [0,1,2,2,3,0,4,2], val = 2 | 5      |
| 3   | nums = [], val = 1                | 0      |
| 4   | nums = [1,1,1], val = 1           | 0      |

---

## 🛠️ Approach

Use a **two-pointer technique**: maintain a pointer `k` for where the next non-`val` element should go. Iterate through `nums`, and when the current element is not equal to `val`, assign it to `nums[k]` and increment `k`. In the end, `k` represents the number of valid elements. :contentReference[oaicite:5]{index=5}

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
