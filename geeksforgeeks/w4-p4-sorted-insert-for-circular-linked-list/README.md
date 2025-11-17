# Sorted Insert for Circular Linked List

> **Difficulty**: Medium  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value `x` into the list such that it remains a sorted circular list. The function should return the newly inserted node.

---

## 📥 Input

- `head`: A reference to any node in a sorted circular linked list (can be `None` for empty list).
- `x`: The integer value to be inserted.

---

## 📤 Output

Return a reference to any node in the modified circular linked list (typically the new node).

---

## ✔️ Constraints

- `0 ≤ number of nodes ≤ 10^4`
- `-10^6 ≤ Node.val ≤ 10^6`
- The list is guaranteed to be sorted in ascending order.
- The list may contain duplicate values.

---

## ✅ Example

**Input**
3 → 5 → 7 → 9 
x = 6

**Output**
3 → 5 → 6 → 7 → 9


**Explanation**: The value 6 is inserted between 5 and 7 to maintain the sorted order.

---

## 🧪 Test Cases

| # | Input List | x | Output List |
|---|------------|---|-------------|
| 1 | `[1,3,4]` | 2 | `[1,2,3,4]` |
| 2 | `[]` | 1 | `[1]` |
| 3 | `[1,1,1]` | 1 | `[1,1,1,1]` |
| 4 | `[1,3,5]` | 0 | `[0,1,3,5]` |
| 5 | `[1,3,5]` | 7 | `[1,3,5,7]` |

---

## 🛠️ Approach

1. **Create New Node**: Initialize a new node with the given value.
2. **Handle Empty List**: If the list is empty, make the new node point to itself and return it.
3. **Find Insertion Point**:
   - Traverse the list to find the correct position where the new node should be inserted.
   - Handle the case where the new node needs to be inserted at the end (wrapping around to the head).
4. **Insert Node**:
   - Update the `next` pointer of the previous node to point to the new node.
   - Set the new node's `next` pointer to the next node.
5. **Return**: Return the new node or any node in the modified list.

### Key Insight
- The circular nature of the list requires special handling for the wrap-around case.
- The insertion must maintain the sorted order of the list.

---

## ⏱️ Complexity

- **Time:** `O(n)` - In the worst case, we may need to traverse the entire list.
- **Space:** `O(1)` - We only use a constant amount of extra space.

---

## 📝 Note
- The solution handles all edge cases including:
  - Empty list
  - Single node list
  - Insertion at the beginning
  - Insertion at the end (wrap-around)
  - Duplicate values
- The insertion is done in-place without using any additional data structures.