# Pairwise Swap Elements of a Linked List

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Adobe, Intuit

---

## 📝 Problem Statement

Given a singly linked list, write a function to swap elements pairwise by swapping data. For example, if the linked list is `1->2->3->4` then the function should change it to `2->1->4->3`.

---

## 📥 Input

- `head`: The head node of the linked list (can be `None` for empty list).

---

## 📤 Output

Return the head of the modified linked list after swapping elements pairwise.

## ✔️ Constraints

- `0 ≤ number of nodes ≤ 10^5`
- `-10^5 ≤ Node.val ≤ 10^5`

---

## ✅ Example

**Input**: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8`  
**Output**: `2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 8 -> 7`

**Input**: `1 -> 2 -> 3 -> 4 -> 5`  
**Output**: `2 -> 1 -> 4 -> 3 -> 5`

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | `[1, 2, 3, 4]` | `[2, 1, 4, 3]` |
| 2 | `[1, 2, 3, 4, 5]` | `[2, 1, 4, 3, 5]` |
| 3 | `[]` | `[]` |
| 4 | `[1]` | `[1]` |
| 5 | `[1, 2]` | `[2, 1]` |

---

## 🛠️ Approach

### Iterative Approach
1. Start from the head of the linked list.
2. Traverse the list by jumping two nodes at a time.
3. For each pair of nodes, swap their data.
4. If the list has odd number of nodes, the last node remains as it is.

### Recursive Approach
1. If the list is empty or has only one node, return the head.
2. Store the next node of the current head.
3. Recursively call the function for the node after the next node.
4. Swap the data of the current node and the next node.
5. Return the new head (which was the second node).

### Key Insight
- We only need to swap the data of the nodes, not the actual node objects.
- The time complexity is O(n) as we traverse the list once.
- The space complexity is O(1) for iterative approach and O(n) for recursive approach due to the call stack.

---

## ⏱️ Complexity

- **Time:** `O(n)`
  - We traverse the linked list once.
- **Space:** `O(1)` (iterative) or `O(n)` (recursive)

---

## 📝 Note
- The solution handles all edge cases including empty list, single node list, and odd-length lists.
- The original structure of the linked list is preserved; only the data is swapped.
- For large lists, the iterative approach is preferred due to constant space usage.