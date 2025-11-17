# Reverse a Linked List

> **Difficulty**: Basic  
> **Companies**: Amazon, Microsoft, Google

---

## 📝 Problem Statement

Reverse a singly linked list and return the new head.

## Input
- A singly linked list represented by its head.

## Output
The head of the reversed linked list.

## Example

**Input**
```
[1,2,3,4]
```

**Output**
```
[4,3,2,1]
```

**Explanation**
```
1 -> 2 -> 3 -> 4

4 -> 3 -> 2 -> 1
```

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | `[1,2,3,4]` | `[4,3,2,1]` |
| 2 | `[1,2,3,4]` | `[4,3,2,1]` |
| 3 | `[1,2,3,4]` | `[4,3,2,1]` |
| 4 | `[1,2,3,4]` | `[4,3,2,1]` |
| 5 | `[1,2,3,4]` | `[4,3,2,1]` |

---

## 🛠️ Approach

Iteratively reverse the `next` pointers by keeping track of previous, current and next nodes. A recursive solution is also possible.

### Key Insights

- The solution handles edge cases like empty lists and ensures the result is in the correct order.
- The dummy node is used to simplify edge cases and return the correct head of the list.

---

## ⏱️ Time Complexity

O(n)

---

## 📊 Space Complexity

O(1) iterative, O(n) recursive stack
