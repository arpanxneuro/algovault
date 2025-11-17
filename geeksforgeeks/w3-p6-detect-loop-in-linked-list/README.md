# Detect Loop in Linked List

> **Difficulty**: Basic  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if there is some node in the list that can be reached again by continuously following the `next` pointer.

---

## 📥 Input

- `head`: The head node of a linked list (can be `None` for empty list).

---

## 📤 Output

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

---

## ✔️ Constraints

- `0 ≤ n ≤ 10^4` where n is the number of nodes in the list
- `-10^5 ≤ Node.val ≤ 10^5`
- The list may or may not contain a cycle.

---

## ✅ Example

**Input**
1 → 2 → 3 → 4 → 2

**Output**
true

**Explanation**
The linked list contains a cycle starting at node 2.

---

## 🧪 Test Cases

| # | Input List | Cycle Start | Output List |
|---|------------|-------------|-------------|
| 1 | `[1,2,3,4]` | 2 | `[1,2,3,4]` |
| 2 | `[1,2,3,4,5]` | 3 | `[1,2,3,4,5]` |
| 3 | `[1]` | 1 | `[1]` |
| 4 | `[1,2,3,4,5]` | 1 | `[1,2,3,4,5]` |
| 5 | `[1,2,3,4,5]` | 5 | `[1,2,3,4,5]` |

---

## 🛠️ Approach

1. **Detect the Loop**: Use Floyd's cycle-finding algorithm to determine if a loop exists.
2. **Find the Start of the Loop**: If a loop is found, use two pointers (one from the meeting point and one from the head) to find the start of the loop.
3. **Remove the Loop**: Once the start of the loop is found, traverse to the node before the start of the loop and set its next pointer to null.

### Key Insight
- The distance from the head to the start of the loop is equal to the distance from the meeting point to the start of the loop when moving around the cycle.

---

## ⏱️ Complexity

- **Time:** `O(n)` - We traverse the list at most twice: once to detect the loop and once to find the start of the loop.
- **Space:** `O(1)` - We only use a constant amount of extra space.

---

## 📝 Note
- The solution handles all edge cases including:
  - Empty list
  - Single node with no cycle
  - Single node with a cycle to itself
  - Cycle starting at the head
  - Cycle starting at the last node
- The modification is done in-place without using any extra space.
