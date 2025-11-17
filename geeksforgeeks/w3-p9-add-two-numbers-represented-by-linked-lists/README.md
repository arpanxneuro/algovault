# Add Two Numbers Represented by Linked Lists

> **Difficulty**: Medium  
> **Companies**: Amazon, Microsoft, Google, Facebook

---

## 📝 Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list in the same reversed order.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## 📥 Input

- `l1`: The head node of the first linked list (non-empty, represents a non-negative integer in reverse order).
- `l2`: The head node of the second linked list (non-empty, represents a non-negative integer in reverse order).

---

## 📤 Output

Return the head of the resulting linked list representing the sum of the two numbers in reverse order.

---

## ✔️ Constraints

- The number of nodes in each linked list is in the range `[1, 100]`
- `0 ≤ Node.val ≤ 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

---

## ✅ Example

**Input**
```
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output**
```
[7,0,8]
```

**Explanation**
```
243 + 564 = 807
```

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | `[2,4,3]` | `[5,6,4]` |
| 2 | `[1,2,3]` | `[4,5,6]` |
| 3 | `[7,8,9]` | `[1,2,3]` |
| 4 | `[4,5,6]` | `[7,8,9]` |
| 5 | `[7,8,9]` | `[4,5,6]` |

---

## 🛠️ Approach

1. Initialize a dummy node to build the result list.
2. Use a carry variable to handle the sum of digits.
3. Traverse both lists simultaneously:
   - Add corresponding digits and the carry.
   - Update the carry for the next iteration.
   - Create a new node with the current digit and append it to the result list.
4. Return the result list starting from the dummy node's next node.

### Key Insights
- The solution handles edge cases like empty lists and ensures the result is in the correct order.
- The dummy node is used to simplify edge cases and return the correct head of the list.

---

## ⏱️ Complexity

- **Time:** `O(max(n, m))` - We traverse both lists once.
- **Space:** `O(max(n, m))` - Space for the result list.

---

## 📝 Note
- The solution returns the result list in the correct order, with the least significant digit at the head.
- The dummy node is used to handle edge cases and simplify the code.
- The solution handles all edge cases including empty lists and single-node lists.
