# Largest Element in Array

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: array, loop, comparison, condition

---

## 📝 Problem Statement

Given an array `arr[]` of size `n`, find and return the largest element in the array.

---

## 📥 Input

- An integer `n`, the size of the array.  
- An array `arr[]` of `n` integers.  

---

## 📤 Output

- Return the largest element in the array `arr[]`.  

## ✔️ Constraints

- 1 ≤ n ≤ 10^6  
- 0 ≤ arr[i] ≤ 10^6  

---

## ✅ Example

**Input:**  
5
1 2 3 4 5

**Output:**  
5

**Explanation:** Among the array elements `[1, 2, 3, 4, 5]`, the largest element is `5`.  

---

## 🛠️ Approach

To solve this problem:  
1. Initialize a variable `max` (or `mx`) with the first element of the array.  
2. Traverse the array from the second element to the last. For each element, if it is greater than `max`, update `max`.  
3. After finishing traversal, `max` holds the largest element — return it.  

### Time and Space Complexity

- **Time Complexity:** O(n) — traverse all elements once.  
- **Space Complexity:** O(1) — only a constant extra variable is used.  
