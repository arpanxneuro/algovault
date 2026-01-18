# reverse linked list

> **Difficulty**: easy  
> **Platform**: GeeksforGeeks  
> **Tags**: linked-list, pointers, iterative, recursion

---

## 📝 Problem Statement

You are given the head of a singly linked list. Reverse the linked list and return the head of the reversed list. :contentReference[oaicite:1]{index=1}

---

## 📥 Input

```
head = [1,2,3,4,5]
```

---

## 📤 Output

```
[5,4,3,2,1]
```

## ✔️ Constraints

- `1 ≤ number of nodes ≤ 10^5`
- `1 ≤ node->data ≤ 10^5` :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:

```
head = [1,2]
```

**Output**:

```
[2,1]
```

**Explanation**: Reversing the linked list transforms the node sequence such that the original tail becomes the new head. :contentReference[oaicite:3]{index=3}

---

## 🧪 Test Cases

| #   | Input          | Output         |
| --- | -------------- | -------------- |
| 1   | `[1,2,3,4,5]`  | `[5,4,3,2,1]`  |
| 2   | `[8,9,10,7,2]` | `[2,7,10,9,8]` |
| 3   | `[]`           | `[]`           |

---

## 🛠️ Approach

### Iterative (Optimal)

- Use three pointers: `prev`, `curr`, and `next`.
- Traverse through the list once, reversing the direction of `next` pointers.
- Finally, return `prev` as the new head of the reversed list.

### Recursive (Alternative)

- Recursively reach the end of the list.
- Reverse the pointer links on unwinding the recursion.
- Return the new head obtained from the deepest recursive call.

Both methods guarantee that the list is reversed correctly without allocating new nodes. :contentReference[oaicite:4]{index=4}

### Time and Space Complexity

- **Time Complexity**: O(n) — each node is visited once.
- **Auxiliary Space**:
  - Iterative: O(1)
  - Recursive: O(n) (due to call stack)

---

## 🧾 Notes

- Ensure you handle edge cases such as an empty linked list or a single-node list.
