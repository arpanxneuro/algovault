# Insert into Sorted Circular Linked List

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: circular‑linked‑list, data‑structure, linked‑list

---

## 📝 Problem Statement

Given a sorted circular singly linked list (ascending order), and a value `x`, insert a node with value `x` into the list so that the list remains sorted. The function should return a reference (head or a node) in the modified circular list. ([GfG – Sorted insert for circular linked list](https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/))

---

## 📥 Input Format

- `head`: reference to any node in the circular linked list (or `None` / `NULL` if list is empty).
- `x`: integer value to insert.
- The list may contain duplicates and node values can be negative, positive or zero.

---

## 📤 Output Format

- Return a reference to a node in the updated circular linked list (typically the inserted node or head). The list remains circular and sorted after insertion.

---

## 🧪 Example Cases

- **Input:** Circular list `1 → 2 → 4 → (back to 1)`, `x = 2`  
  **Output:** Sorted circular list becomes `1 → 2 → 2 → 4 → ...`

- **Input:** Circular list `1 → 4 → 7 → 9 → (back to 1)`, `x = 5`  
  **Output:** `1 → 4 → 5 → 7 → 9 → ...`

- **Input:** Empty list (`head = None`), `x = 10`  
  **Output:** A circular list with single node `10` pointing to itself.

---

## 🛠️ Approach

1. Create a new node with the given value `x`.
2. If list is empty (`head == None`):
   - Point new node’s `next` to itself, return new node.
3. Else: traverse the list to find correct position:
   - If `x` should be inserted before head (i.e. `x <= head.data`), find the last node (whose `next` points to head), insert new node before head, and return new node as new head.
   - Else, find the appropriate spot where `curr.data < x <= curr.next.data`. Insert new node there.
   - If reached end without insertion, insert at end before head (i.e. for x largest).
4. Return reference to resulting list (head or new node). :contentReference[oaicite:2]{index=2}
