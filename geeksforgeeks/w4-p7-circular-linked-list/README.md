# Circular Linked List

> **Difficulty**: Easy  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value `x` into the list such that it remains a sorted circular list. The function should return the newly inserted node.

---

## 📤 Input

- `head`: A reference to any node in a sorted circular linked list (can be `None` for empty list).
- `x`: The integer value to be inserted.

---

## 📤 Output

Return a reference to any node in the modified circular linked list (typically the new node).



## ✔️ Constraints

- `0 ≤ number of nodes ≤ 10^4`
- `-10^6 ≤ Node.val ≤ 10^6`
- The list is guaranteed to be sorted in ascending order.
- The list may contain duplicate values.

## ✅ Example

**Initial List**: `[1, 2, 3]` (circular)

**Operations**:
1. Insert 0 at beginning: `[0, 1, 2, 3]`
2. Insert 4 at end: `[0, 1, 2, 3, 4]`
3. Delete 2: `[0, 1, 3, 4]`

---

## 🧪 Test Cases

| # | Operations | Output |
|---|------------|--------|
| 1 | Insert(1), Insert(2), Insert(3) | `[1, 2, 3]` |
| 2 | Insert(1), Delete(1) | `[]` |
| 3 | Insert(1), Insert(2), Delete(1) | `[2]` |
| 4 | Insert(2), Insert(1), Insert(3) | `[1, 2, 3]` |
| 5 | Insert(1), Insert(1) (duplicate) | `[1]` |

---

## 🛠️ Approach

### Insertion at Beginning
1. Create a new node with the given value.
2. If the list is empty, make the new node point to itself and return it.
3. Otherwise, traverse to the last node and update its next pointer to the new node.
4. Make the new node point to the old head.
5. Update the head to the new node.

### Insertion at End
1. Create a new node with the given value.
2. If the list is empty, make the new node point to itself and return it.
3. Otherwise, traverse to the last node.
4. Make the last node point to the new node.
5. Make the new node point to the head.

### Deletion
1. If the list is empty, return.
2. If the node to be deleted is the only node, set head to null.
3. Otherwise, traverse the list to find the node to be deleted and its previous node.
4. Update the previous node's next pointer to skip the node to be deleted.
5. If the node to be deleted is the head, update the head.

### Traversal
1. If the list is empty, return.
2. Start from the head and print each node's value.
3. Stop when we reach the head again.

### Key Insight
- The circular nature of the list requires special handling to maintain the circular structure during operations.
- The last node always points back to the head.

---

## ⏱️ Complexity

- **Time:**
  - Insertion at beginning/end: `O(n)` (need to find the last node)
  - Deletion: `O(n)` (in the worst case)
  - Traversal: `O(n)`
- **Space:** `O(1)` for all operations (not counting the space for the list itself)

---

## 📝 Note
- The solution handles all edge cases including empty list, single node list, and operations on non-existent elements.
- All operations maintain the circular nature of the list.
- The list remains sorted if insertions are done in order.