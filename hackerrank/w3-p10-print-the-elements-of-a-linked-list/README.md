# Print the Elements of a Linked List

> **Difficulty**: easy  
> **Platform**: HackerRank  
> **Tags**: linked‑list, traversal, data‑structure

---

## 📝 Problem Statement

Given the head of a singly linked list, traverse the list and **print the data of each node, one per line**. If the head pointer is `NULL` (i.e. the list is empty), print nothing. This is the core requirement of the Print the Elements of a Linked List challenge on HackerRank. :contentReference[oaicite:2]{index=2}

---

## 📥 Input

- First line: integer `n`, the number of elements in the linked list. :contentReference[oaicite:3]{index=3}
- Next `n` lines: each line contains an integer — the data value for a node in the linked list. :contentReference[oaicite:4]{index=4}

> **Note:** When solving on HackerRank, you should **not** manually read input in the function — the driver code handles input parsing and passes the head of the constructed list to your function. :contentReference[oaicite:5]{index=5}

---

## 📤 Output

Print the data of each node in the linked list, one per line, in the order they appear in the list. If the list is empty, output nothing. :contentReference[oaicite:6]{index=6}

---

## 🛠️ Approach

### Iterative Traversal

- Initialize `current = head`.
- While `current != null`:
  - Print `current.data`.
  - Move `current = current.next`.

This runs in **O(n)** time (n = number of nodes) and uses **O(1)** extra space. This is a standard method for printing a singly linked list — widely discussed in linked‑list tutorials. :contentReference[oaicite:7]{index=7}

### (Optional) Recursive Traversal

Alternatively, you could implement a recursive function that prints node data, then recurses on `next`. This yields the same output order, but uses O(n) stack space — not ideal for very long lists. :contentReference[oaicite:8]{index=8}

---

## ✅ Example

**Input**  
3
16
13
7

**Output**  
16
13
7

**Explanation:** The linked list is `16 → 13 → 7 → NULL`. Printing each node’s data in order results in three lines: 16, 13, 7.

---

## 📊 Complexity

- **Time Complexity:** O(n), where n is number of nodes.
- **Space Complexity:** O(1) — only a few pointers/variables are used for traversal (ignoring call stack if recursive).
