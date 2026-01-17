# Nth Node from End of Linked List

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: linked‑list, two‑pointers, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list and an integer `n`, return the value of the **nth node from the end** of the list. If `n` is greater than the number of nodes in the list, return `-1`.

---

## 📥 Input

- `head`: the head node of the linked list (may be `null` / `None` if the list is empty).
- `n`: 1‑based integer: the position from the end (i.e. `n = 1` → last node).

---

## 📤 Output

- Return an integer: the data value of the nth node from the end if it exists; otherwise `-1`.

---

## ✅ Examples

**Example 1**  
Input: head = [1 → 2 → 3 → 4 → 5], n = 2
Output: 4
Explanation: The 2nd node from the end is 4.
**Example 2**  
Input: head = [1 → 2 → 3 → 4], n = 4
Output: 1
Explanation: 4th node from end is the head (value 1).
**Example 3**  
Input: head = [7], n = 1
Output: 7
**Example 4**  
Input: head = [1 → 2 → 3], n = 5
Output: -1
Explanation: n is greater than list length.

---

## 🛠️ Approach (Two‑Pointer / Tortoise‑Hare)

Use a two-pointer technique (fast & slow) to find the nth node from end in one pass.

- Initialize `fast = head`, `slow = head`.
- Advance `fast` by `n` steps. If during this phase `fast == null`, return `-1` (list has fewer than `n` nodes).
- Then, advance both `slow` and `fast` together until `fast` reaches the last node.
- At that moment, `slow` will point to the nth node from the end. Return `slow.data`.

**Time Complexity:** O(L) where L = list length  
**Space Complexity:** O(1) — just pointers

This satisfies the expected one‑pass O(n) solution.

---

## 📌 Edge Cases & Notes

- If the list is empty (`head = null`) → return `-1`.
- If `n` equals the list length → returns the head's value.
- If `n >` list length → return `-1`.
- Works for both small and large lists.
