# Print the Elements of a Linked List

> **Difficulty**: Basic  
> **Accuracy**:   
> **Submissions**:   
> **Points**: 

---

## 📝 Problem Statement

This exercise focuses on traversing a linked list. You are given a pointer to the head node of a linked list. The task is to print the data of each node, one per line. If the head pointer is `NULL`, indicating the list is empty, nothing should be printed.

---

---

## 📥 Input

- The first line of input contains an integer `n`, the number of elements in the linked list.  
- The next `n` lines contain one element each, representing the data values for the nodes.

**Note:**  
Do not read input from `stdin` or console. The function will receive the list head reference.

---

---

---

## 📤 Output

Output the data of each node, one per line.

---

## ✅ Example

**Input**:
3 16 13 7

**Output**:
16 13 7


**Explanation**: The linked list contains three nodes with values 16, 13, and 7, which are printed in order.

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | `3`<br>`16`<br>`13`<br>`7` | `16`<br>`13`<br>`7` |
| 2 | `5`<br>`1`<br>`2`<br>`3`<br>`4`<br>`5` | `1`<br>`2`<br>`3`<br>`4`<br>`5` |
| 3 | `1`<br>`42` | `42` |
| 4 | `0` | *(no output)* |

---

## 🛠️ Approach

### Iterative Traversal
1. **Initialization**: Start with the head node
2. **Traversal**:
   - While the current node is not null:
     - Print the node's data
     - Move to the next node
3. **Termination**: Stop when reaching a null pointer

### Recursive Traversal
1. **Base Case**: If the node is null, return
2. **Recursive Step**:
   - Print the current node's data
   - Recursively call the function with the next node

### Time and Space Complexity
- **Time Complexity**: O(n) - We visit each node exactly once
- **Space Complexity**:
  - Iterative: O(1) - Constant extra space
  - Recursive: O(n) - Recursion stack space (implicit)

---

## 📝 Note
- The solution handles edge cases:
  - Empty list (head is null)
  - Single node list
  - Large lists (up to 1000 nodes)
- The problem is a fundamental exercise in linked list traversal
- The iterative solution is more space-efficient for large lists
- The recursive solution is more elegant but has O(n) space complexity due to the call stack

## 🔗 Related Problems
- [Print in Reverse](https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse)
- [Insert a Node at the Tail](https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list)
- [Delete a Node](https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list)