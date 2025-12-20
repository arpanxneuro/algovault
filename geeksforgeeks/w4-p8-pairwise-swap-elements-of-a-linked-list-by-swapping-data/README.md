# Pairwise Swap Elements of a Linked List (by Swapping Data)

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: linked-list, data‑structures  

---

## 📝 Problem Statement

Given a singly linked list, swap the data of its nodes in pairs: i.e. swap the 1st and 2nd nodes, then the 3rd and 4th, and so on. If the list has an odd number of nodes, the last node remains unchanged. For example, `1 → 2 → 3 → 4` becomes `2 → 1 → 4 → 3` after the swap. ([GfG – Pairwise Swap Elements of a given Linked List](https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list/))  

---

## 📥 Input Format

- `head`: reference to the head node of the singly linked list.  
- The list may be empty (`head = None`) or contain up to \(10^5\) nodes.  
- Node values may be any integer (e.g. \(-10^5\) ≤ val ≤ \(10^5\)).  

---

## 📤 Output Format

- Return the head of the modified linked list after performing the pairwise data swaps.  

---

## 🧪 Example Cases

- **Input:** `1 → 2 → 3 → 4 → 5 → 6 → None`  
  **Output:** `2 → 1 → 4 → 3 → 6 → 5 → None`  

- **Input:** `1 → 2 → 3 → 4 → 5 → None`  
  **Output:** `2 → 1 → 4 → 3 → 5 → None`  

- **Input:** `[]` (empty list) → Output: `[]`  

---

## 🛠️ Approach  

Use a simple iterative (or recursive) traversal:  

- Traverse the list two nodes at a time.  
- For each adjacent pair \(`node`, `node.next`\), swap their `data` fields.  
- Move forward by two nodes and repeat until end of list.  

This ensures O(n) time and O(1) extra space (aside from the list itself).  