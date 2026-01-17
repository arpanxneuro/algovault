# Search in Linked List

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: linked‑list, search, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list (which may be empty) and an integer `x`, determine whether `x` exists in the list. If it does, return the index (0‑based) of its first occurrence; otherwise return `-1`.

This is a standard linear search over a linked list.

---

## 📥 Input

- `head`: the head node of the singly linked list (can be `null` / `None` if the list is empty)
- `x`: integer value to search for in the linked list

---

## 📤 Output

- Return an integer: the 0‑based index of the first node whose value equals `x`; or `-1` if no such node is found.

---

## ✔️ Constraints / Edge Cases

- The list can be empty.
- Node values (and `x`) can be any integer (positive, negative, zero) depending on problem variant.
- If the value appears multiple times, return the first occurrence (smallest index).

---

## ✅ Examples

**Example 1**  
Input: head = [3, 1, 4, 2], x = 4
Output: 2
Explanation: The first occurrence of value 4 is at index 2 (0‑based).
**Example 2**  
Input: head = [10, 20, 30], x = 5
Output: -1
Explanation: 5 is not present in the list.
**Example 3**  
Input: head = [], x = 1
Output: -1
Explanation: Empty list → no elements.
**Example 4**  
Input: head = [7,7,7], x = 7
Output: 0
Explanation: First node matches → index 0.

---

## 🛠️ Approach

Use a linear traversal (iterative): start at `head` with an index counter (initially 0). Traverse node by node: for each node, compare its value to `x`. If equal — return current index. If end of list is reached (`null` / `None`) — return `-1`. This requires **O(n)** time and **O(1)** extra space (just pointers and counter).

---

## ⏱️ Complexity

- **Time Complexity:** O(n) — traverse each node at most once.
- **Space Complexity:** O(1) — constant extra space.
