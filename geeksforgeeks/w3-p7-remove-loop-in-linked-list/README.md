# Remove Loop in Linked List

> **Difficulty**: medium  
> **Platform**: GeeksforGeeks  
> **Tags**: linked‑list, two‑pointers, cycle‑detection, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list that may contain a cycle (loop), remove the loop — i.e. ensure that the list becomes linear by breaking the cycle. After removal, the list should traverse from head to tail ending with `null`. ([geeksforgeeks.org](https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/?utm_source=chatgpt.com))

If there is no loop, the list should remain unchanged.

---

## 📥 Input

- `head`: the head node of a singly linked list (may be `null` / `None`)
- The list may or may not contain a loop; if it does, it's guaranteed to have at most one cycle

---

## 📤 Output

- The function should modify the linked list in-place to remove the loop if present.
- After removal (or if no loop), the list should be linear — no node’s `next` should point back to an earlier node.
- Typically, the function returns `void` (or `null`) — but the modified list (head) should represent the corrected chain with no cycles.

---

## ✅ Examples

**Example 1 — loop present**  
Input: head = 1 → 3 → 4
(last node’s next points back to node with value 3)
After removal: 1 → 3 → 4 → null
**Example 2 — no loop**  
Input: head = 1 → 8 → 3 → 4 → null
Output: list remains unchanged

---

## 🛠️ Approach (Floyd’s Cycle Detection + Loop Removal)

Efficient in‑place algorithm — O(n) time, O(1) extra space.

1. Use two pointers — `slow` and `fast`, both starting at `head`.
2. Advance `slow` by one, `fast` by two steps at a time.
3. If at any step `slow == fast`, a cycle is detected.
4. To find the start of the loop: reset one pointer to head; then move both one step at a time until their `next` pointers are equal. That identifies the node before loop start.
5. Set that node’s `next` to `null`, breaking the loop.

This preserves all nodes and retains the list order (except the loop is removed).

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## 📌 Edge Cases & Notes

- If the list is empty (`head = null`) or has a single node — handle gracefully.
- Works when loop begins at head, or anywhere in the list.
- After removal, any traversal of the list should end at `null`, not cycle infinitely.
- This method does **not** use extra data structures (no hash-set), so it's space-efficient.
