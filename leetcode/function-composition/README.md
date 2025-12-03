# Function Composition

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: functional‑programming, higher‑order‑functions, function‑composition

---

## 📝 Problem Statement

Given an array of unary functions `functions = [f1, f2, f3, ..., fn]`, return a single function that represents their composition. The composed function, when called with input `x`, should compute:
f1(f2(f3(...(fn(x))...)))

In other words, functions are applied from right to left. If the array is empty, the result should be the identity function — i.e., `f(x) = x`. ([LeetCode #2629 Function Composition](https://leetcode.com/problems/function-composition/))

---

## 📥 Input Format

- `functions`: array of functions, each accepts one integer and returns one integer. (`0 ≤ functions.length ≤ 1000`) :contentReference[oaicite:2]{index=2}
- When the composed function is invoked, it accepts an integer `x`, where `-1000 ≤ x ≤ 1000`. :contentReference[oaicite:3]{index=3}

---

## 📤 Output Format

- Returns a function `fn`. When `fn(x)` is called, it returns an integer — the result of applying all provided functions in composition on `x`.

## ✔️ Constraints

- `-1000 ≤ x ≤ 1000` :contentReference[oaicite:4]{index=4}
- `0 ≤ functions.length ≤ 1000` :contentReference[oaicite:5]{index=5}
- Each function accepts exactly one integer argument and returns one integer. :contentReference[oaicite:6]{index=6}

---

## 🧪 Sample Cases

### Example 1

**Input:**  
functions = [x => x + 1, x => x * x, x => 2 * x]
x = 4
**Output:** `65`  
**Explanation:**

- Start with x = 4
- Apply the rightmost function: 2 \* 4 = 8
- Next: square → 8 \* 8 = 64
- Next: +1 → 64 + 1 = 65 :contentReference[oaicite:7]{index=7}

### Example 2

**Input:**  
functions = [x => 10 * x, x => 10 * x, x => 10 * x]
x = 1
**Output:** `1000`  
**Explanation:**  
10 × (10 × (10 × 1)) = 1000 :contentReference[oaicite:8]{index=8}

### Example 3

**Input:**  
functions = []
x = 42
**Output:** `42`  
**Explanation:**  
Empty function array → identity function, returns input as is. :contentReference[oaicite:9]{index=9}

---

## 🛠️ Approach

- Use a higher‑order function `compose(functions)` that returns a new function `fn`.
- When `fn(x)` is invoked, apply all functions in the array from right to left.
- In JavaScript, you can implement this cleanly using `reduceRight`: start with initial value `x`, then apply each function in reverse order:
