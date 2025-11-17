# Insert in Sorted Way in a Sorted Doubly Linked List

> **Difficulty**: Medium  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given the head of a sorted doubly linked list in ascending order, insert a new node with a given value into the list while maintaining the sorted order. The list may contain duplicate values.

---

## 📥 Input

- `head`: The head node of a sorted doubly linked list (can be `None` for empty list).
- `data`: An integer value to be inserted into the list.

---

## 📤 Output

Return the head of the modified doubly linked list after the insertion.

---

## ✔️ Constraints

- `0 ≤ number of nodes ≤ 10^4`
- `-10^5 ≤ Node.val ≤ 10^5`
- The list is guaranteed to be sorted in ascending order.

---

## ✅ Example

**Input**
1 ⇄ 3 ⇄ 4 data = 2

**Output**
1 ⇄ 2 ⇄ 3 ⇄ 4

**Explanation**
The node with value 2 is inserted between 1 and 3, maintaining the sorted order.

---

## 🧪 Test Cases

| # | Input List | n | Output |
|---|------------|---|--------|
| 1 | `[1,2,3,4]` | 2 | `3` |
| 2 | `[1,2,3,4,5]` | 3 | `3` |
| 3 | `[1]` | 1 | `1` |
| 4 | `[1,2,3,4,5]` | 1 | `5` |
| 5 | `[1,2,3,4,5]` | 5 | `-1` |

---

## 🛠️ Approach

1. **Handle Edge Cases**: If the list is empty, create a new node and return it as the head.
2. **Traverse List**: Use a pointer to traverse the list until finding the correct position to insert the new node.
3. **Insert Node**: Insert the new node at the correct position by updating the `prev` and `next` pointers of the relevant nodes.
4. **Return Head**: Return the head of the modified list.

### Key Insights
- The approach handles all edge cases including empty list and duplicate values.
- The insertion is performed in O(n) time complexity where n is the number of nodes in the list.
- The approach is efficient and maintains the sorted order of the list.

---

## ⏱️ Complexity

- **Time:** `O(n)` - We traverse the list at most once.
- **Space:** `O(1)` - We only use a constant amount of extra space.

---

## 📝 Note
- The solution handles all edge cases including:
  - Empty list
  - Single node list
  - Duplicate values
  - Insertion at head and tail
- The approach is efficient with O(n) time complexity and O(1) space complexity.
