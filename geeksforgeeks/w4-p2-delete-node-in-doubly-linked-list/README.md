# Delete Node in Doubly Linked List

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given a reference to the head of a doubly linked list and a key, delete all occurrences of the given key from the linked list. The list is maintained in sorted order.

---

## 📥 Input

- `head`: The head node of a sorted doubly linked list (can be `None` for empty list).
- `x`: The value to be deleted from the list.

---

## 📤 Output

Return the head of the modified doubly linked list after deletion.

---

## ✔️ Constraints

- `0 ≤ number of nodes ≤ 10^4`
- `-10^5 ≤ Node.val ≤ 10^5`
- The list is guaranteed to be sorted in ascending order.

---

## ✅ Example

**Input**
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5 x = 3

**Output**
1 ⇄ 2 ⇄ 4 ⇄ 5


**Explanation**: The node with value 2 is deleted from the list.

---

## 🧪 Test Cases

| # | Input List | x | Output List |
|---|------------|---|-------------|
| 1 | `[1,2,3,4]` | 2 | `[1,3,4]` |
| 2 | `[1,1,1]` | 1 | `[]` |
| 3 | `[2,5,7,9]` | 10 | `[2,5,7,9]` |
| 4 | `[1,2,3,4,5]` | 1 | `[2,3,4,5]` |
| 5 | `[1,2,3,4,5]` | 5 | `[1,2,3,4]` |

---

## 🛠️ Approach

1. **Handle Empty List**: If the list is empty, return `None`.
2. **Delete Head Nodes**: If the head node contains the value to be deleted, update the head.
3. **Traverse and Delete**: 
   - Traverse the list to find nodes with the target value.
   - For each matching node, update the `next` pointer of the previous node and the `prev` pointer of the next node.
4. **Return Head**: Return the head of the modified list.

### Key Insight
- The doubly linked list allows for efficient deletion by updating both `next` and `prev` pointers.
- The solution handles all edge cases including empty list, single node list, and multiple occurrences of the target value.

---

## ⏱️ Complexity

- **Time:** `O(n)` - In the worst case, we may need to traverse the entire list.
- **Space:** `O(1)` - We only use a constant amount of extra space.

---

## 📝 Note
- The solution maintains the sorted order of the list after deletion.
- All node pointers (`next` and `prev`) are properly updated to maintain the doubly linked list structure.
- The solution handles edge cases including empty list and single-node list.