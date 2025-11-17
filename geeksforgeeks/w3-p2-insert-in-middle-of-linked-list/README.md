# Insert in Middle of Linked List

> **Difficulty**: Basic  
> **Companies**: Amazon, Microsoft, Adobe

---

## 📝 Problem Statement

Given the head of a singly linked list, insert a new node with a given value in the middle of the list. For an even-length list, insert after n/2 nodes (i.e., at index n/2).

---

## 📥 Input

- `head`: The head node of the linked list (can be `None` for empty list).
- `val`: The integer value to insert in the middle.

---

## 📤 Output

Return the head of the modified linked list after inserting the new value in the middle.

---

## ✔️ Constraints

- `0 ≤ n ≤ 10^4` where n is the number of nodes in the list
- `-10^4 ≤ val ≤ 10^4`
- List can be empty

---

## ✅ Example

**Input**
```
head = [1, 2, 3, 4]
val = 9
```

**Output**
```
[1, 2, 9, 3, 4]
```

**Explanation**: The value 9 is inserted in the middle of the list. For even-length lists, we insert after the first middle element.

---

## 🧪 Test Cases

| # | Linked List | Value | Output |
|---|-------------|-------|--------|
| 1 | `[1,2,3,4]` | 9 | `[1,2,9,3,4]` |
| 2 | `[10,20,30,40,50]` | 25 | `[10,20,25,30,40,50]` |
| 3 | `[7]` | 3 | `[7,3]` |
| 4 | `[]` | 1 | `[1]` |
| 5 | `[5,10]` | 7 | `[5,7,10]` |

---

## 🛠️ Approach

1. **Edge Cases**: Handle empty list and single-node list separately.
2. **Two Pointers**: Use slow and fast pointers to find the middle node.
3. **Insertion**: Insert the new node after the middle node found.

### Key Insight
- The slow pointer moves one step at a time while the fast pointer moves two steps at a time.
- When fast reaches the end, slow will be at the middle node.

---

## ⏱️ Complexity

- **Time:** `O(n)` - We traverse the list once to find the middle.
- **Space:** `O(1)` - Constant extra space is used.

---

## 📝 Note
- For even-length lists, the middle is defined as the first middle element (n/2 - 1 for 0-based indexing).
- The solution handles all edge cases including empty list and single-node list.
