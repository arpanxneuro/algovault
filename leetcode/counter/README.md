# Counter Function

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: closure, functions, counter

---

## 📝 Problem Statement

Given an integer `n`, create a counter function using closures. The returned counter function initially returns `n`, and every subsequent call returns the next integer (i.e., `n + 1`, `n + 2`, …). The counter must retain its internal state across calls without using global variables. ([LeetCode #2620 Counter](https://leetcode.com/problems/counter/))

---

## 📥 Input Format

- `n`: starting integer value (constraints: `-1000 <= n <= 1000`) :contentReference[oaicite:0]{index=0}
- Calls: a sequence of `"call"` operations (at most 1000 calls). :contentReference[oaicite:1]{index=1}

---

## 📤 Output Format

- Returns a function — each time this function is called, it returns the next number in the sequence starting from `n`.

## ✔️ Constraints

- `-1000 <= n <= 1000` :contentReference[oaicite:2]{index=2}
- At most 1000 calls to the returned counter function. :contentReference[oaicite:3]{index=3}

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
**Explanation:** The counter starts from –2 and increments by 1 on each call. :contentReference[oaicite:4]{index=4}

---

## 🛠️ Approach

Use a closure to capture the initial value `n`. Return an inner function which, when invoked, returns the current value and increments it. This way, the internal state persists across calls without using global variables. :contentReference[oaicite:5]{index=5}
