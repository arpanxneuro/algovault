# remove duplicates from sorted list

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: linked-list, pointers

---

## 📝 Problem Statement

Given the `head` of a sorted singly linked list, delete all duplicates such that each element appears only once and return the modified linked list. The list must remain sorted. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

```
head = [1,1,2,3,3]
```

---

## 📤 Output

```
[1,2,3]
```

## ✔️ Constraints

- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`.
- The linked list is guaranteed to be sorted in ascending order. :contentReference[oaicite:1]{index=1}

---

## ✅ Example

**Input**:

```
head = [1,1,2]
```

**Output**:

```
[1, 2]
```

**Explanation**:  
All consecutive duplicate values are removed such that only one occurrence of each value remains in the sorted list. :contentReference[oaicite:2]{index=2}

---

## 🧪 Test Cases

| #   | Input         | Output    |
| --- | ------------- | --------- |
| 1   | `[1,1,2]`     | `[1,2]`   |
| 2   | `[1,1,2,3,3]` | `[1,2,3]` |
| 3   | `[]`          | `[]`      |

---

## 🛠️ Approach

Since the list is sorted, all duplicate values appear consecutively. Traverse the linked list with a pointer (`current`) and compare each node’s value with the next node’s value:

- If `current.val == current.next.val`, skip the next node by updating `current.next = current.next.next`.
- Otherwise advance `current` to `current.next`.
- Continue until the end of the list. :contentReference[oaicite:3]{index=3}

This ensures that duplicates are removed in place without additional data structures.

### Time and Space Complexity

- **Time Complexity**: O(n) — one pass through the list
- **Space Complexity**: O(1) — no extra space needed

---

## 🧾 Notes

- Edge cases include an empty list or a list with all identical values.
