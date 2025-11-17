# Delete a Node in Single Linked List

> **Difficulty**: Basic  
> **Companies**: Samsung, Adobe, Amazon

---

## 📝 Problem Statement

Delete the node at a given position in a singly linked list and return the modified list. If the position is out of bounds, the list remains unchanged.

---

## 📥 Input

- `head`: The head node of the linked list (can be `None` for empty list).
- `pos`: An integer (0 ≤ pos < n) indicating the 0-based position of the node to delete.

---

## 📤 Output

Return the head of the modified linked list after deletion.

---

## ✔️ Constraints

- `0 ≤ n ≤ 10^4` where n is the number of nodes in the list
- `-10^4 ≤ Node.val ≤ 10^4`
- `0 ≤ pos < n`
- List can be empty

---

## ✅ Example

**Input**
```
head = [1, 2, 3, 4]
pos = 2
```

**Output**
```
[1, 2, 4]
```

**Explanation**: The node at position 2 (0-based) with value 3 is deleted from the list.

---

## 🧪 Test Cases

| # | Linked List | Position | Output |
|---|-------------|----------|--------|
| 1 | `[1,2,3,4]` | 2 | `[1,2,4]` |
| 2 | `[10,20,30,40,50]` | 0 | `[20,30,40,50]` |
| 3 | `[7]` | 0 | `[]` |
| 4 | `[1,2,3,4,5]` | 4 | `[1,2,3,4]` |
| 5 | `[5,10,15,20]` | 2 | `[5,10,20]` |

---

## 🛠️ Approach

1. **Edge Cases**: Handle empty list and deletion at head (pos = 0) separately.
2. **Traversal**: Move to the node before the target position (pos-1).
3. **Deletion**: Update the next pointer to skip the target node.
4. **Out of Bounds**: If position exceeds list length, return original list.

### Key Insight
- For position 0, simply return `head.next`
- For other positions, find the node before the target and update its next pointer
- If position is invalid (≥ list length), return the original list

---

## ⏱️ Complexity

- **Time:** `O(n)` - In worst case, we may need to traverse the entire list.
- **Space:** `O(1)` - Constant extra space is used.

---

## 📝 Note
- The position is 0-based, with 0 being the head of the list.
- If the position is equal to or greater than the length of the list, the list remains unchanged.
- The solution handles all edge cases including empty list and single-node list.
