# Insert in Sorted Way in a Sorted Doubly Linked List

> **Difficulty**: medium  
> **Source**: GeeksforGeeks  
> **Tags**: doubly‑linked‑list, insertion, sorting, data‑structure

---

## 📝 Problem Statement

Given the head of a sorted doubly linked list (ascending / non‑decreasing order) and an integer value `x`, insert a new node with value `x` into the correct position in the list so that the list remains sorted. The list may contain duplicate values. ([GfG – Insert value in sorted way in a sorted doubly linked list](https://www.geeksforgeeks.org/insert-value-sorted-way-sorted-doubly-linked-list/)) :contentReference[oaicite:2]{index=2}

---

## 📥 Input Format

- `head`: reference to the head node of the sorted doubly linked list (can be `null` / `None` if the list is empty)
- `x`: integer value to insert

---

## 📤 Output Format

- Return the head of the modified doubly linked list after insertion

---

## 🧪 Example Cases

- **Input:** `head = 3 ⇄ 5 ⇄ 8 ⇄ 10 ⇄ 12`, `x = 9` → **Output:** `3 ⇄ 5 ⇄ 8 ⇄ 9 ⇄ 10 ⇄ 12` :contentReference[oaicite:3]{index=3}
- **Input:** `head = 1 ⇄ 4 ⇄ 10 ⇄ 11`, `x = 15` → **Output:** `1 ⇄ 4 ⇄ 10 ⇄ 11 ⇄ 15` :contentReference[oaicite:4]{index=4}
- **Input:** empty list (`head = None`), `x = 5` → **Output:** single-node list `5`

---

## 🛠️ Approach

1. Create a new node with value `x`.
2. If the list is empty, make the new node the head and return it.
3. Else if `x` is less than or equal to head’s data, insert the new node before head — set new node’s `next = head`, update head’s `prev`, and return new node as new head.
4. Otherwise traverse the list until either you reach the end or find a node `curr` such that `curr.data ≤ x ≤ curr.next.data`. Insert the new node after `curr` by adjusting `prev` and `next` pointers accordingly.
5. If you reach end without finding such spot (i.e. `x` greater than all existing values), insert at end.

This preserves sorted order and runs in O(n) time with O(1) extra space. :contentReference[oaicite:5]{index=5}
