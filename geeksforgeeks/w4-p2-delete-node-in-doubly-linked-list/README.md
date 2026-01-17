# Delete Node in Doubly Linked List

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: doubly‑linked‑list, deletion, data‑structure

---

## 📝 Problem Statement

Given the head of a doubly linked list and a key value `x`, delete **all occurrences** of nodes whose `data == x`, and return the head of the modified list. If the list is empty or no node with value `x` exists, return the original head. The list is sorted in ascending order. ([GfG – Delete a node in a Doubly Linked List](https://www.geeksforgeeks.org/delete-a-node-in-a-doubly-linked-list/))

---

## 📥 Input

- `head`: reference to the head node of the doubly linked list (or `null` / `None` if empty).
- `x`: integer value to delete from the list.
- The list may contain zero or more nodes; node values are arbitrary integers; duplicates are allowed.

---

## 📤 Output

- Return the head of the updated doubly linked list after all deletions.

---

## 🧪 Example Cases

| Input List                 | x                       | Output List       |
| -------------------------- | ----------------------- | ----------------- |
| `1 ⇄ 2 ⇄ 3 ⇄ 4`, x = 2     | Delete node with data 2 | `1 ⇄ 3 ⇄ 4`       |
| `1 ⇄ 1 ⇄ 1`, x = 1         | Delete all nodes        | `[]` (empty list) |
| `2 ⇄ 5 ⇄ 7 ⇄ 9`, x = 10    | No matching nodes       | `2 ⇄ 5 ⇄ 7 ⇄ 9`   |
| `1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5`, x = 1 | Delete head node(s)     | `2 ⇄ 3 ⇄ 4 ⇄ 5`   |
| `1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5`, x = 5 | Delete tail node        | `1 ⇄ 2 ⇄ 3 ⇄ 4`   |

---

## 🛠️ Approach

Traverse the doubly linked list. Whenever you find a node with `data == x`, delete that node:

- If it's the head node: update head to `head.next`.
- If node has a `.next`, set `node.next.prev = node.prev`.
- If node has a `.prev`, set `node.prev.next = node.next`.
- Properly adjust `head` if head was deleted.

Repeat until end of list — thus removing **all** occurrences. Use constant auxiliary space.
