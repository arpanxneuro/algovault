# Insert in Middle of Linked List

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: linked‑list, insertion, two‑pointers, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list (which may be empty) and an integer `val`, insert a new node with value `val` in the middle of the list.

- If the list has `n` nodes, and `n` is even — insert after the `n/2`‑th node.
- If `n` is odd — insert after the `(n+1)/2`‑th node.

Return the head of the modified linked list.

---

## 📥 Input

- `head` — head node of the singly linked list (can be `null` / `None` if list is empty)
- `val` — integer value to insert into a new node

---

## 📤 Output

- Return the head of the updated linked list after insertion.

---

## ✅ Examples

**Example 1**  
Input: head = [1, 2, 4, 5], val = 3
Output: [1, 2, 3, 4, 5]
**Example 2**  
Input: head = [5, 10, 4, 32, 16], val = 41
Output: [5, 10, 4, 41, 32, 16]

If the list is empty:  
Input: head = [], val = 7
Output: [7]

---

## 🛠️ Approach

Two standard methods — both O(n) time, O(1) space.

### Method 1: Two‑pass (length + insert)

1. Traverse the list to compute `len`, the number of nodes.
2. Compute insertion index `mid = len/2` (if even), else `mid = (len + 1)/2`.
3. Traverse again to the `mid`‑th node, then insert the new node after it.

### Method 2: Single‑pass (Tortoise & Hare)

- Use two pointers — `slow` and `fast`. Initialize `slow = head`, `fast = head->next`.
- Move `slow` one step at a time; `fast` two steps at a time.
- When `fast` reaches end (or `fast->next` is null), `slow` will point to the node **after** which insertion should happen.
- Insert the new node after `slow`.

Both approaches give **Time Complexity:** O(n), **Space Complexity:** O(1).

---

## 📌 Edge Cases & Notes

- If the list is empty — the new node becomes the head.
- Works for both even and odd‑length lists, per rule above.
- Handles negative/positive values for `val` as typical.
