# Counter Function

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: closure, functions, counter

---

## 📝 Problem Statement

Given an integer `n`, create a counter function using closures. The returned counter function initially returns `n`, and every subsequent call returns the next integer (i.e., `n + 1`, `n + 2`, …). The counter must retain its internal state across calls without using global variables. ([LeetCode #2620 Counter](https://leetcode.com/problems/counter/))

---

## 📥 Input

- `n`: starting integer value (constraints: `-1000 <= n <= 1000`)
- Calls: a sequence of `"call"` operations (at most 1000 calls)

---

## 📤 Output

- Returns a function — each time this function is called, it returns the next number in the sequence starting from `n`.

## ✔️ Constraints

- `-1000 <= n <= 1000`
- At most 1000 calls to the returned counter function.

---

## ✅ Example

**Input:**  
n = 10
calls = ["call", "call", "call"]
**Output:**  
[10, 11, 12]
**Explanation:**

- First call returns 10
- Second call returns 11
- Third call returns 12

**Input:**  
n = -2
calls = ["call", "call", "call", "call", "call"]
**Output:**  
[-2, -1, 0, 1, 2]
**Explanation:** The counter starts from –2 and increments by 1 on each call.

---

## 🧪 Test Cases

| #   | Input              | Output      |
| --- | ------------------ | ----------- |
| 1   | n = 10             | [10, 11, 12]|
| 2   | n = -2 (5 calls)   | [-2, -1, 0, 1, 2] |

---

## 🛠️ Approach

Use a closure to capture the initial value `n`. Return an inner function which, when invoked, returns the current value and increments it. This way, the internal state persists across calls without using global variables.

### Time and Space Complexity

- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
