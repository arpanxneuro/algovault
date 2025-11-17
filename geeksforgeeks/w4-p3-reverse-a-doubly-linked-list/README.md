# Reverse a Doubly Linked List

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given a doubly linked list, reverse the list in place and return the new head of the reversed list.

---

## 📥 Input

- `head`: The head node of a doubly linked list (can be `None` for empty list).

---

## 📤 Output

Return the head of the reversed doubly linked list.

---

## ✔️ Constraints

- `0 ≤ number of nodes ≤ 10^4`
- `-10^5 ≤ Node.val ≤ 10^5`

---

## ✅ Example

**Input**
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5

**Output**
5 ⇄ 4 ⇄ 3 ⇄ 2 ⇄ 1


**Explanation**: The list is reversed in place by swapping each node's `prev` and `next` pointers.

---

## 🧪 Test Cases

| # | Input List | Output List |
|---|------------|-------------|
| 1 | `[1,2,3,4]` | `[4,3,2,1]` |
| 2 | `[1]` | `[1]` |
| 3 | `[]` | `[]` |
| 4 | `[1,2]` | `[2,1]` |
| 5 | `[1,1,2,3,3]` | `[3,3,2,1,1]` |

---

## 🛠️ Approach

1. **Initialize Pointers**: 
   - `current` starts at the head
   - `temp` is used for swapping pointers
2. **Traverse and Swap**:
   - For each node, swap its `prev` and `next` pointers
   - Move to the next node using the previous `next` (now in `prev`)
3. **Update Head**: 
   - After traversal, the new head is the last non-null node

### Key Insight
- The doubly linked list structure allows for efficient reversal by simply swapping `prev` and `next` pointers.
- The operation is done in a single pass through the list.

---

## ⏱️ Complexity

- **Time:** `O(n)` - We traverse the list exactly once.
- **Space:** `O(1)` - We only use a constant amount of extra space.

---

## 📝 Note
- The solution handles all edge cases:
  - Empty list
  - Single node list
  - List with duplicate values
- The reversal is done in-place without using any additional data structures.
- All node pointers are properly updated to maintain the doubly linked list structure.