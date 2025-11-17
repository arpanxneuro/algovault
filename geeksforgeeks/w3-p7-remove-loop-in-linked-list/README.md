# Remove Loop in Linked List

> **Difficulty**: Medium  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given a linked list that contains a cycle, remove the loop so that the list becomes linear while preserving the node order outside the loop. The task is to find the node where the cycle begins and break the link that forms the cycle.

---

## 📥 Input

- `head`: The head node of a linked list that contains at most one cycle.

---

## 📤 Output

- Modify the linked list in-place to remove the cycle.
- No need to return anything, but the function should modify the list in place.

---

## ✔️ Constraints

- `0 ≤ n ≤ 10^4` where n is the number of nodes in the list
- `-10^5 ≤ Node.val ≤ 10^5`
- The list is guaranteed to have at most one cycle.
- The list can be empty.

---

## ✅ Example


**Input**
1 → 2 → 3 → 4 

**Output**
1 → 2 → 3 → 4 → null


**Explanation**: The cycle starting at node 2 is removed by setting the next pointer of node 4 to null.

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