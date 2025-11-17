# Linked List Insertion

> **Difficulty**: Basic  
> **Companies**: TCS, Wipro, Hike

---

## 📝 Problem Statement

Insert a new node with a given value at a specified position in a singly linked list. The position is 0-based, meaning position 0 refers to the head of the list.

---

## 📥 Input

- `head`: The head node of the linked list (can be `None` for empty list).
- `pos`: An integer (0 ≤ pos ≤ length of list) indicating where to insert.
- `val`: The integer value to insert.

---

## 📤 Output

Return the head of the modified linked list after insertion.

---

## ✔️ Constraints

- `0 ≤ pos ≤ n` where n is the length of the list
- `-10^4 ≤ val ≤ 10^4`
- List can be empty

---

## ✅ Example

**Input**
```
head = [1, 2, 3]
pos = 1
val = 9
```

**Output**
```
[1, 9, 2, 3]
```

**Explanation**: The value 9 is inserted at position 1 (0-based), between 1 and 2.

---

## 🧪 Test Cases

| # | Linked List | Position | Value | Output |
|---|-------------|----------|-------|--------|
| 1 | `[1,2,3]`   | 1        | 9     | `[1,9,2,3]` |
| 2 | `[10,20]`   | 0        | 5     | `[5,10,20]` |
| 3 | `[7]`       | 1        | 8     | `[7,8]` |
| 4 | `[]`        | 0        | 1     | `[1]` |

---

## ⏱️ Complexity

- **Time:** `O(n)` - In worst case, we may need to traverse the entire list.
- **Space:** `O(1)` - Constant extra space is used.
