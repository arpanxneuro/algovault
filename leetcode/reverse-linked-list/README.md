# reverse linked list

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: linked-list, pointers

---

## 📝 Problem Statement

Given the head of a singly linked list, reverse the list and return the reversed list.  
You may implement the reversal either **iteratively** or **recursively**.

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

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`. :contentReference[oaicite:1]{index=1}

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

**Explanation**:

- The order of the linked list is reversed from head to tail. :contentReference[oaicite:2]{index=2}

---

## 🧪 Test Cases

| #   | Input         | Output        |
| --- | ------------- | ------------- |
| 1   | `[1,2,3,4,5]` | `[5,4,3,2,1]` |
| 2   | `[]`          | `[]`          |
| 3   | `[1]`         | `[1]`         |

---

## 🛠️ Approach

**Iterative Approach (O(n) time, O(1) space)**

- Initialize two pointers: `prev = None` and `curr = head`.
- Traverse the list while `curr` is not null:
  - Store the next node (`next = curr.next`);
  - Redirect `curr.next` to `prev`;
  - Advance `prev` to `curr`, and `curr` to `next`.
- When traversal completes, `prev` is the new head of the reversed list. :contentReference[oaicite:3]{index=3}

**Recursive Approach (O(n) time, O(n) space)**

- Base case: if the list is empty or has one node, return `head`;
- Recursively reverse the sublist beyond the head;
- After recursion unwinds, fix pointer directions to complete reversal. :contentReference[oaicite:4]{index=4}

---

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**:
  - Iterative: O(1)
  - Recursive: O(n) (due to recursion stack) :contentReference[oaicite:5]{index=5}
