# Factorial Using Recursion

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: mathematical, algorithms

---

## 📝 Problem Statement

Given a non‑negative integer `N`, compute its factorial:
N! = N × (N−1) × (N−2) × ... × 2 × 1
By convention, `0! = 1`. You need to implement a recursive solution (or optionally an iterative one) to compute `N!`. ([GfG – Factorial of a Number](https://www.geeksforgeeks.org/dsa/program-for-factorial-of-a-number/))

---

## 📥 Input Format

- `N`: a non‑negative integer (e.g. `0 ≤ N ≤ 20` for 64‑bit safe results)

---

## 📤 Output Format

- Return the factorial of `N` (as a 64‑bit integer or appropriate big-integer type if `N` is large).

---

## 🧪 Example Cases

- **Input:** `N = 5` → **Output:** `120` (since 5×4×3×2×1 = 120)
- **Input:** `N = 0` → **Output:** `1` (by definition)

---

## 🛠️ Approach

Use recursion with the base case and recurrence:
