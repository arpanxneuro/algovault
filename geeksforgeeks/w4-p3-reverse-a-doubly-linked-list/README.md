# Reverse a Doubly Linked List

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: doubly‑linked‑list, reversal, data‑structure

---

## 📝 Problem Statement

Given the head of a doubly linked list, reverse the list in‑place so that the first node becomes the last, the second becomes the second last, and so on. Return the new head of the reversed list. ([GfG – Reverse a Doubly Linked List](https://www.geeksforgeeks.org/reverse-a-doubly-linked-list/))

---

## 📥 Input Format

- `head`: reference to the head node of a doubly linked list (or `null` / `None` if the list is empty).
- Number of nodes can be 0 up to ~10⁴, node values are arbitrary integers.

---

## 📤 Output Format

- Return the head of the reversed doubly linked list.

---

## 🧪 Example Cases

- **Input:** `1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5`  
  **Output:** `5 ⇄ 4 ⇄ 3 ⇄ 2 ⇄ 1`

- **Input:** Empty list → Output: empty list

- **Input:** Single-node list `[x]` → Output: `[x]`

---

## 🛠️ Approach

Traverse the list, and for each node, swap its `next` and `prev` pointers. Then move to what was previously the next node (i.e. current’s new `prev`, since pointers were swapped). At end, update head to the last processed node, which becomes the new head. This takes one full pass.
