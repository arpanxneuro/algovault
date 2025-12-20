# Sorted Insert for Circular Linked List

> **Difficulty**: medium  
> **Source**: GeeksforGeeks  
> **Tags**: circular‑linked‑list, insertion, sorting, data‑structure

---

## 📝 Problem Statement

Given a node from a circular singly linked list sorted in ascending order and an integer value `x`, insert `x` into the list so that it remains sorted. The function should return a reference (any node) in the modified circular list. ([Sorted insert for circular linked list — GeeksforGeeks](https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/))

---

## 📥 Input Format

- `head`: reference to any node in the sorted circular linked list (or `null` / `None` if the list is empty).
- `x`: integer value to insert into the list.
- The list may be empty, or contain zero or more nodes; duplicates are allowed.

---

## 📤 Output Format

- Return a reference to any node in the updated circular linked list (often the newly inserted node or the head).

---

## 🧪 Example Cases

- **Input:** list: `1 → 2 → 4` (circular), `x = 2`  
  **Output:** `1 → 2 → 2 → 4` (circular) :contentReference[oaicite:2]{index=2}
- **Input:** list: `1 → 4 → 7 → 9` (circular), `x = 5`  
  **Output:** `1 → 4 → 5 → 7 → 9` (circular) :contentReference[oaicite:3]{index=3}
- **Input:** empty list, `x = 10`  
  **Output:** single-node circular list: `10 → (back to itself)` :contentReference[oaicite:4]{index=4}

---

## 🛠️ Approach

1. Create a new node with data `x`.
2. If the list is empty (`head` is `null`):
   - Make new node point to itself. Return it as the (only) node.
3. Otherwise, traverse the circular list to find correct insertion point:
   - If `x` should be inserted before head’s data (i.e. smallest), locate the last node (whose `next` points to head), insert new node before head, and return new node (as possible new head).
   - Else traverse until you find `curr` such that `curr.data ≤ x ≤ curr.next.data`, then insert between `curr` and `curr.next`.
   - If you traverse full circle without insertion (i.e. x > all existing values), insert after last node (before head).

This preserves sorted order and circular structure. :contentReference[oaicite:5]{index=5}
