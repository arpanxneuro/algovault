# Reverse an Array of Integers

> **Difficulty**: easy  
> **Platform**: HackerRank  
> **Tags**: array, data‑structure

---

## 📝 Problem Statement

Given an integer array, reverse the order of elements and output the reversed array. This is the exact task for the "Arrays - DS" challenge on HackerRank.

---

## 📥 Input

- First line: integer `N` — the number of elements in the array.
- Second line: `N` space-separated integers `arr[0], arr[1], …, arr[N–1]`.

---

## 📤 Output

Print the elements of the reversed array in a single line, space-separated.

---

## ✔️ Constraints

- \(1 \le N \le 10^3\)
- Elements values within valid integer range (as per contest constraints)

---

## ✅ Example

**Input**  
5
1 2 3 4 5
**Output**  
5 4 3 2 1

---

## 🛠️ Approach

Use a two‑pointer technique to reverse the array **in place**:

1. Initialize two pointers: `left = 0`, `right = N - 1`.
2. While `left < right`, swap `arr[left]` and `arr[right]`, then increment `left`, decrement `right`.

This achieves reversal in **O(N)** time with **O(1)** extra space.

---

## ⏱️ Complexity

- **Time Complexity:** O(N) — each element is swapped at most once.
- **Space Complexity:** O(1) — only constant extra space (pointers) is used.
