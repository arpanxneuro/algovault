# Reverse an Array of Integers

> **Difficulty**: Easy  
> **Platform**: HackerRank  
> **Tags**: Array, Data Structure

---

## 📝 Problem Statement

Given an array of integers, reverse the order of elements in the array and print the reversed array.

---

## 📥 Input

- The first line contains an integer `N` (1 ≤ N ≤ 10^3), the number of elements in the array.
- The second line contains `N` space-separated integers `arr[i]` (1 ≤ arr[i] ≤ 10^4), where 0 ≤ i < N.

---

## 📤 Output

Print the elements of the reversed array as a single line of space-separated integers.

## ✔️ Constraints

- 1 ≤ N ≤ 10^3
- 1 ≤ arr[i] ≤ 10^4

---

## ✅ Example

**Input**:
5 1 2 3 4 5

**Output**:
5 4 3 2 1


**Explanation**: The array [1,2,3,4,5] when reversed becomes [5,4,3,2,1].

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | `5`<br>`1 2 3 4 5` | `5 4 3 2 1` |
| 2 | `3`<br>`10 20 30` | `30 20 10` |
| 3 | `1`<br>`100` | `100` |
| 4 | `6`<br>`1 4 3 2 5 6` | `6 5 2 3 4 1` |

---

## 🛠️ Approach

### Two-Pointer Technique
1. **Initialization**:
   - Use two pointers: `start` (beginning of array) and `end` (end of array)
   - Initialize `start` to 0 and `end` to N-1

2. **Swapping**:
   - While `start` is less than `end`:
     - Swap elements at positions `start` and `end`
     - Increment `start` and decrement `end`

3. **Termination**:
   - The loop terminates when `start` becomes greater than or equal to `end`
   - The array is now reversed in-place

### Time and Space Complexity
- **Time Complexity**: O(N) - We traverse half of the array
- **Space Complexity**: O(1) - Constant extra space is used (in-place reversal)

---

## 📝 Note
- The solution modifies the original array in-place
- For very large arrays, this approach is memory efficient
- The algorithm is stable and works for both even and odd array lengths
- Edge cases handled:
  - Single element array
  - Already reversed array
  - Array with duplicate elements

## 🔗 Related Problems
- [Rotate Array](https://leetcode.com/problems/rotate-array/)
- [Reverse String](https://leetcode.com/problems/reverse-string/)
- [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)