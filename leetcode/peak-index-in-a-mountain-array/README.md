# peak index in a mountain array

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: array, binary-search, mountain

---

## 📝 Problem Statement

You are given an integer mountain array `arr` of length `n` where the values strictly increase up to a **peak element** and then strictly decrease. Return the **index of the peak element**. The algorithm must run in **O(log n)** time complexity.

---

## 📥 Input

- An integer array `arr` representing a mountain array (strictly increasing then strictly decreasing).

---

## 📤 Output

Return the **index** of the peak element — the element larger than its neighbors in the mountain array.

## ✔️ Constraints

- `3 <= arr.length <= 10⁵`
- `0 <= arr[i] <= 10⁶`
- `arr` is guaranteed to be a mountain array (strictly increasing then strictly decreasing).

---

## ✅ Example

**Input**:
arr = [0,1,0]

**Output**:
1
**Input**:
arr = [0,2,1,0]

**Output**:
1

---

## 🧪 Test Cases

| #   | Input      | Output |
| --- | ---------- | ------ |
| 1   | [0,1,0]    | 1      |
| 2   | [0,2,1,0]  | 1      |
| 3   | [0,10,5,2] | 1      |
| 4   | [3,4,5,1]  | 2      |

---

## 🛠️ Approach

To achieve **O(log n)** runtime, apply a **binary search** leveraging the mountain property:

1. Initialize `left = 0` and `right = arr.length - 1`.
2. While `left < right`:
   - Compute `mid = left + (right - left) // 2`.
   - If `arr[mid] < arr[mid + 1]`, the peak is to the right → set `left = mid + 1`.
   - Otherwise, the peak is at or to the left → set `right = mid`.
3. At termination `left == right` — this index is the peak.

### Time and Space Complexity

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
