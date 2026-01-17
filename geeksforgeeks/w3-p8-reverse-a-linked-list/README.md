# Reverse a Linked List

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: linked‑list, reversal, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list, reverse the list — i.e., reverse the direction of `next` pointers so that the last node becomes the head, and return the new head of the reversed list. ([geeksforgeeks.org](https://www.geeksforgeeks.org/dsa/reverse-a-linked-list/))

---

## 📥 Input

- `head`: the head node of a singly linked list (may be `null` / `None` if the list is empty).

---

## 📤 Output

- Return the head of the reversed linked list.

---

## ✅ Example

**Input**  
[1, 2, 3, 4](represents 1 → 2 → 3 → 4 → null)

**Output**  
[4, 3, 2, 1]Which corresponds to 4 → 3 → 2 → 1 → null.

---

## 🛠️ Approach

One efficient in‑place method (iterative), with O(n) time and O(1) extra space:

- Maintain three pointers:
  - `prev = null`
  - `curr = head`
  - `next = null`
- Iterate while `curr` is not null:
  1. `next = curr.next` (store next node)
  2. `curr.next = prev` (reverse pointer)
  3. `prev = curr`
  4. `curr = next`
- At end, `prev` is new head of reversed list — return `prev`.

Alternative approaches: recursion or using stack — but iterative is most efficient (constant extra space) as shown on GfG.

---

## ⏱️ Complexity

- **Time Complexity:** O(n), where n is number of nodes — each node visited exactly once.
- **Space Complexity:** O(1) (iterative approach) — uses only constant extra pointers.

---

## 📌 Edge Cases & Notes

- Empty list (`head = null`) → return `null`.
- Single‑node list → return same node (now head).
- Works for any integer values stored in nodes.
- The reversed list should terminate at `null`, not cause loops — original next pointers are reversed carefully.
