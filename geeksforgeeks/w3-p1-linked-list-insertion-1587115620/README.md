# Linked List Insertion

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: linked-list, insertion, singly‑linked‑list, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list (which may be empty), a position `pos` (0-based), and a value `val`, insert a new node with value `val` into the list at the given position. Position `0` refers to inserting at the head. Return the head of the modified list.

---

## 📥 Input

- `head`: the head node of the singly linked list (can be `null` / `None` when list is empty).
- `pos`: integer satisfying `0 ≤ pos ≤ length_of_list` — indicates index (0-based) where the new node should be inserted.
- `val`: integer value to store in the new node.

---

## 📤 Output

- Return the head of the updated linked list after insertion.

---

## ✔️ Constraints

- Position `pos` is valid: `0 ≤ pos ≤ length of existing list`.
- The list may initially be empty.
- Coefficient / value constraints depend on problem variant (e.g., can be negative or positive ints).

---

## ✅ Examples

**Example 1**
Input:
head = [1, 2, 3]
pos = 1
val = 9

Output:
[1, 9, 2, 3]

**Example 2**  
Input:
head = []
pos = 0
val = 5

Output:
[5]

**Example 3**  
Input:
head = [10, 20]
pos = 0
val = 5

Output:
[5, 10, 20]

---

## 🛠️ Approach

Iterative insertion — O(n) time, O(1) extra space. Basic idea:

- If `pos == 0`, create new node and link its `next` to current `head`; return new node as new head.
- Else, traverse the list until reaching the node at index `pos - 1`.
- Adjust pointers: let `newNode.next = current.next`, and `current.next = newNode`.  
  Return the (possibly unchanged) head.

---

## ⏱️ Complexity

- **Time Complexity:** O(n) — in worst case, must traverse up to list length.
- **Space Complexity:** O(1) — only constant extra space for the new node and pointer manipulation.
