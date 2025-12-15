# Insert at End of Array

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: array, insertion, list

---

## 📝 Problem Statement

Given a partially-filled array `arr[]` and an integer value `val`, insert the value at the end of the array and return the updated array. Also return the new size of the array after insertion.

---

## 📥 Input

- `arr[]`: An array of integers (not completely filled)  
- `n`: Current number of elements in the array  
- `capacity`: Maximum capacity of the array  
- `val`: Integer value to be inserted at the end  

---

## 📤 Output

- Return the updated array with `val` inserted at the end  
- Return the new size of the array after insertion  

## ✔️ Constraints

- 1 ≤ n ≤ 10^5  
- 0 ≤ arr[i] ≤ 10^6  
- 1 ≤ capacity ≤ 10^6  
- 0 ≤ val ≤ 10^6  
- It is guaranteed that the array has at least one empty slot  

---

## ✅ Example

**Example 1**  
**Input:**  
arr = [1, 2, 3, 4, 5]
n = 5
capacity = 10
val = 90
**Output:**  
6 # New size of array
[1, 2, 3, 4, 5, 90] # Array after insertion
**Explanation:**  
The value 90 is inserted at the end of the array, increasing its size by 1.  

**Example 2**  
**Input:**  
arr = [10, 20, 30]
n = 3
capacity = 5
val = 40
**Output:**  
4
[10, 20, 30, 40]


---

## 🛠️ Approach

To solve this problem:

1. Check if there’s space in the array (`n < capacity`).  
2. Insert `val` at index `n` (0-based indexing).  
3. Increment the size `n` by 1.  
4. Return the new size (and updated array).  

### Time and Space Complexity

- **Time Complexity:** O(n) — in worst-case if rebuilding or copying array manually.  
- **Space Complexity:** O(1) — insertion at end without extra data structures.  
