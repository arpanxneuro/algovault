# Frequency of Array Elements

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: array, hash, data structure

---

## 📝 Problem Statement

Given an array `arr[]` of non‑negative integers (or integers), return the frequency of each distinct element present in the array — i.e., how many times each element appears.

---

## 📥 Input

- `arr[]`: an integer array of size `n`.
- `n`: number of elements in the array.

---

## 📤 Output

- For each distinct element in `arr[]`, output (or return) a pair: **element → frequency**, representing how many times that element occurs in the array.

---

## ✅ Examples

**Example 1**  
**Input**: arr = [10, 20, 10, 5, 20]
**Output**: [[5, 1], [10, 2], [20, 2]]

Here 5 occurs once, 10 occurs 2 times, 20 occurs 2 times.

**Example 2**  
**Input**: arr = [4, 4, 4, 4]
**Output**: [[4, 4]]

All elements are the same — 4 occurs 4 times.

---

## 🛠️ Approach

A recommended efficient approach uses a hash‑map / dictionary to count frequencies in a single pass:

- Initialize an empty map `freqMap`.
- Iterate over each element `x` in `arr[]`: increment `freqMap[x]`.
- After the pass, iterate over entries in `freqMap` to build the result pairs (element, count).

This gives **Time Complexity** = O(n), and **Space Complexity** = O(n) (for the map) in the general case.

If the array elements are in a restricted range (e.g., 1 to n) — as per a variant of the problem — there exists an in‑place O(n)‑time, O(1)-extra‑space method using the array itself as a frequency map.

---

## 📌 Notes

- Works with duplicate elements.
- Works for arbitrary integer values (as long as map/dictionary supports them).
- The order of output pairs can be sorted (e.g. ascending by element) or left in arbitrary order depending on implementation.
