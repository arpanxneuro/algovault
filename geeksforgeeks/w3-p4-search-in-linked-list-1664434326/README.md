# Search in Linked List

> **Difficulty**: Basic  
> **Companies**: Amazon, Microsoft, Google

---

## 📝 Problem Statement

Given a singly linked list and a value `x`, determine whether `x` exists in the list and return its first index (0-based). If the value is not present, return -1.

---

## 📥 Input

- `head`: The head node of the linked list (can be `None` for empty list).
- `x`: The integer value to search for in the linked list.

---

## 📤 Output

Return the index of the first occurrence of `x` in the linked list (0-based), or -1 if the value is not found.

---

## ✔️ Constraints

- `0 ≤ n ≤ 10^4` where n is the number of nodes in the list
- `-10^4 ≤ Node.val ≤ 10^4`
- `-10^4 ≤ x ≤ 10^4`
- List can be empty

---

## ✅ Example

**Input**
```
head = [3, 1, 4, 2]
x = 4
```

**Output**
```
2
```

**Explanation**: The value 4 is found at index 2 (0-based) in the linked list.

---

## 🧪 Test Cases

| # | Linked List | Search Value | Output |
|---|-------------|--------------|--------|
| 1 | `[3,1,4,2]` | 4 | `2` |
| 2 | `[10,20,30]` | 5 | `-1` |
| 3 | `[]` | 1 | `-1` |
| 4 | `[7,7,7]` | 7 | `0` |
| 5 | `[1,2,3,2,1]` | 2 | `1` |

---

## 🛠️ Approach

1. **Initialization**: Start from the head of the linked list and initialize an index counter to 0.
2. **Traversal**: Traverse the linked list node by node.
3. **Comparison**: At each node, check if the node's value matches the target value `x`.
4. **Return**: If a match is found, return the current index. If the end of the list is reached without finding the value, return -1.

### Key Insight
- The solution efficiently handles edge cases like empty lists and ensures the first occurrence is returned.

---

## ⏱️ Complexity

- **Time:** `O(n)` - In the worst case, we may need to traverse the entire list.
- **Space:** `O(1)` - We only use a constant amount of extra space.

---

## 📝 Note
- The solution returns the first occurrence of the value if it appears multiple times.
- The index is 0-based, meaning the first element is at index 0.
- The solution handles all edge cases including empty lists and single-node lists.
