# Sorted Insert for Circular Linked List

> **Difficulty**: medium  
> **Source**: GeeksforGeeks  
> **Tags**: circular‑linked‑list, insertion, sorting, data‑structure

---

## 📝 Problem Statement

Given a node from a circular singly linked list sorted in ascending (non‑decreasing) order, and an integer value `x`, insert a new node with value `x` into the list so that it remains a sorted circular linked list. Return a reference to any node in the modified list (often the inserted node or head). ([GfG – Sorted insert for circular linked list](https://www.geeksforgeeks.org/sorted-insert-for-circular-linked-list/))

---

## 📥 Input Format

- `head`: reference to any node in the sorted circular linked list (or `null`/`None` if list is empty).
- `x`: integer value to insert.
- The list may have zero or more nodes; node values can be in any integer range; duplicates allowed.

---

## 📤 Output Format

- A reference to a node in the updated circular linked list, after inserting the new value and maintaining sorted order and circular linkage.

---

## 🧪 Example Cases

| Initial list               | x   | Resulting list (one possible rotation)                    |
| -------------------------- | --- | --------------------------------------------------------- |
| `1 → 2 → 4` (circular)     | 2   | `1 → 2 → 2 → 4` :contentReference[oaicite:2]{index=2}     |
| `1 → 4 → 7 → 9` (circular) | 5   | `1 → 4 → 5 → 7 → 9` :contentReference[oaicite:3]{index=3} |
| empty list                 | 10  | `10` (single node circular list)                          |

---

## 🛠️ Approach

1. Create a new node with value `x`.
2. If the list is empty (`head == None`), make the new node point to itself and return it.
3. Otherwise, traverse the circular list to find the correct insertion point as follows:
   - If `x` should come before or equal to the current head’s data, locate the tail (node whose next points to head), insert the new node before head, and return the new node as (possible) new head.
   - Else, traverse until you find a node `curr` such that `curr.data ≤ x ≤ curr.next.data`, then insert the new node between `curr` and `curr.next`.
   - If traversal completes (i.e. `x` is larger than all existing nodes), insert the new node after the current last node and before head — preserving circular order.
4. Return the reference.

This ensures sorted order and circular linkage are preserved. :contentReference[oaicite:4]{index=4}
