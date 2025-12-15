# Add Two Numbers Represented by Linked Lists

> **Difficulty**: medium  
> **Platform**: GeeksforGeeks  
> **Tags**: linked-list, math, two‑pointers, data‑structure

---

## 📝 Problem Statement

You are given two non-empty singly linked lists representing two non-negative integers.  
Each node of the linked list contains a single digit. The digits are stored in **reverse order**, meaning the 1’s digit is at the head of the list.

Add the two numbers and return the sum as a linked list — also in reverse order.  
You may assume the two numbers do not contain any leading zeros, except the number 0 itself. :contentReference[oaicite:2]{index=2}

---

## 📥 Input

- `l1`: head of the first linked list (represents a non-negative integer in reverse order)
- `l2`: head of the second linked list (same representation)

---

## 📤 Output

- Return the head of a new linked list representing the sum of the two numbers, with digits stored in reverse order.

---

## ✅ Example

**Input**  
l1 = [2,4,3] # represents 342
l2 = [5,6,4] # represents 465
**Output**  
[7,0,8] # represents 807 (since 342 + 465 = 807)

**Explanation**

- 342 + 465 = 807
- The result list in reverse order of digits is 7 → 0 → 8 :contentReference[oaicite:3]{index=3}

---

## 🛠️ Approach

A straightforward and standard solution:

1. Reverse both linked lists so that their heads represent the least significant digit (i.e. ones place). :contentReference[oaicite:4]{index=4}
2. Traverse both reversed lists simultaneously, adding corresponding digits along with any carry from the previous addition.
3. For each sum, create a new node whose value is `sum % 10`, update carry to `sum // 10`. Append node to result list.
4. If one list is longer — continue adding remaining digits plus carry.
5. If after processing both lists there is a leftover carry — create a new node for it.
6. Reverse the result list and return its head — now digits are back in reverse order representation. :contentReference[oaicite:5]{index=5}

This yields a correct sum representation, handles carry properly, and works for different-length inputs.

---

## ⏱️ Complexity

- **Time Complexity:** O(n + m), where n, m are lengths of the two lists (you traverse each at most once, plus reversals).
- **Space Complexity:** O(n + m) for the result list (plus O(1) auxiliary space if ignoring output storage).

---

## 📌 Notes & Edge Cases

- Works even when one list is longer than the other.
- Handles carry propagation properly (e.g. 9 + 9 → carry).
- Handles final carry by appending extra node.
- Works when inputs have leading zeros — but you may trim if needed (GfG mentions trimming leading zeros in some variants). :contentReference[oaicite:6]{index=6}
