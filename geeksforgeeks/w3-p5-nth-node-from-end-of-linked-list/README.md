# Nth Node from End of Linked List

> **Difficulty**: Basic  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given the head of a singly linked list and an integer `n`, return the value of the nth node from the end of the list.

---

## 📥 Input

- `head`: The head node of a linked list (can be `None` for empty list).
- `n`: A positive integer (1-based index from the end).

---

## 📤 Output

Return the integer value of the nth node from the end of the list. If `n` is greater than the length of the list, return `-1`.

---

## ✔️ Constraints

- `1 ≤ n ≤ 10^4`
- `0 ≤ Node.val ≤ 10^5`
- `1 ≤ number of nodes ≤ 10^4`

---

## ✅ Example

**Input**
1 → 2 → 3 → 4 → 5

**Output**
4

**Explanation**
The 4th node from the end is 4.

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

1. **Two Pointers**: Use two pointers, `fast` and `slow`, to traverse the list.
2. **Advance Fast Pointer**: Move the `fast` pointer `n` steps ahead.
3. **Move Both Pointers**: If the `fast` pointer reaches the end, return `-1` (n is too large). Otherwise, move both pointers until the `fast` pointer reaches the end.
4. **Return Value**: The `slow` pointer will be at the nth node from the end.

### Key Insight
- The distance between the two pointers is `n` when the `fast` pointer starts `n` steps ahead.
- When the `fast` pointer reaches the end, the `slow` pointer will be at the nth node from the end.

---

## ⏱️ Complexity

- **Time:** `O(n)` - We traverse the list at most twice.
- **Space:** `O(1)` - We only use a constant amount of extra space.

---

## 📝 Note
- The solution handles all edge cases including:
  - Empty list
  - Single node list
  - n > number of nodes
  - n = 1 (returns the last node)
- The approach is efficient with O(n) time complexity and O(1) space complexity.
