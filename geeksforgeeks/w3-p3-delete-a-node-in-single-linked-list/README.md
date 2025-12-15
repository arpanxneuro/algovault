# Delete a Node in Single Linked List

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: linked‑list, deletion, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list (which may be empty), and a 0‑based position `pos`, delete the node at that position. If the position is invalid (out of bounds), the list remains unchanged. Return the head of the modified linked list.

---

## 📥 Input

- `head` — the head node of the singly linked list (may be `null` / `None` if list is empty)
- `pos` — integer indicating the 0‑based position of the node to delete

---

## 📤 Output

- Return the head of the updated list after deletion (or unchanged head if position invalid)

---

## ✔️ Constraints

- Let the list have `n` nodes initially, then `0 ≤ pos < n` for valid deletion.
- For empty list (`n = 0`) or invalid `pos`, simply return the original `head`.
- Node values can be any integer (positive, negative, zero) depending on problem specification.

---

## ✅ Examples

**Example 1**  
Input: head = [1, 2, 3, 4], pos = 2
Output: [1, 2, 4]
Explanation: Node at index 2 (0‑based) — value 3 — is removed.
**Example 2**  
Input: head = [10, 20, 30, 40], pos = 0
Output: [20, 30, 40]
Explanation: Delete the head node.
**Example 3**  
Input: head = [7], pos = 0
Output: []
Explanation: Single‑node list becomes empty.
**Example 4**  
Input: head = [5,10,15,20], pos = 4
Output: [5,10,15,20]
Explanation: Position out‑of‑bounds — no deletion.

---

## 🛠️ Approach

Standard iterative deletion in a singly linked list — O(n) time, O(1) space. :contentReference[oaicite:2]{index=2}

1. If `head` is `null`, return `null`.
2. If `pos == 0`, adjust head to `head.next`, delete old head (if manual memory management), and return new head.
3. Else, traverse list to reach node just **before** the target — i.e. iterate `pos - 1` steps (while tracking current node).
4. If `next` of that node exists, update its `next` pointer to skip the node to delete: `prev.next = prev.next.next`.
5. Return head.

Edge cases: empty list, deletion at head, last‑node deletion, invalid position (≥ length).

---

## ⏱️ Complexity

- **Time Complexity:** O(n) — traversal up to `pos` (worst-case full list).
- **Space Complexity:** O(1) — only a few pointer variables used.
