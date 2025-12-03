# Detect Loop in Linked List

> **Difficulty**: medium  
> **Platform**: GeeksforGeeks  
> **Tags**: linked‑list, two‑pointers, cycle‑detection, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list, determine whether the list contains a **cycle / loop** — i.e., whether there exists a node such that by continuously following `next` pointers you eventually revisit that node (instead of reaching `null`). Return `true` if there is a cycle, otherwise return `false`. :contentReference[oaicite:2]{index=2}

---

## 📥 Input

- `head`: the head node of the singly linked list (can be `null` / `None` if list is empty).

---

## 📤 Output

- Return a boolean:
  - `true` — if the linked list contains at least one cycle.
  - `false` — otherwise.

---

## ✅ Examples

**Example 1**  
Input: head = 1 → 3 → 4 → 3 (last node links back to node with value 3)
Output: true
**Example 2**  
Input: head = 1 → 8 → 3 → 4 → null
Output: false

---

## 🛠️ Approach (Floyd’s Cycle‑Finding / Two‑Pointer)

Use the two‑pointer (slow and fast) algorithm to detect a loop in O(n) time and O(1) extra space. :contentReference[oaicite:3]{index=3}

- Initialize both pointers — `slow = head`, `fast = head`.
- While `fast` and `fast.next` are valid:
  - Move `slow` one step (`slow = slow.next`)
  - Move `fast` two steps (`fast = fast.next.next`)
  - If at any point `slow == fast`, a cycle exists → return `true`.
- If you exit the loop (i.e. `fast` or `fast.next` becomes `null`), no cycle → return `false`.

This runs in **O(n)** time, **O(1)** space.

---

## 📌 Notes & Edge Cases

- Works even for empty list (`head = null`) → returns `false`.
- Handles single-node list with no cycle.
- Handles cases where the entire list loops back (cycle starting at head or elsewhere).
- Does **not** require extra memory (no hash sets), making it space-efficient.
- This algorithm is standard, commonly called Floyd’s Cycle‑Finding Algorithm (Hare & Tortoise). :contentReference[oaicite:4]{index=4}
