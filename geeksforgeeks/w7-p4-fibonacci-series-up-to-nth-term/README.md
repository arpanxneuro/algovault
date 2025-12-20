# Fibonacci Series Up to Nth Term

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: recursion, fibonacci, algorithms, dynamic programming

---

## 📝 Problem Statement

Generate the first `N` terms of the Fibonacci sequence. The Fibonacci series is defined as:

- F(0) = 0
- F(1) = 1
- F(n) = F(n−1) + F(n−2) for n > 1.

Return a list of the first `N` Fibonacci numbers. ([GfG – Fibonacci Series Up to Nth Term](https://www.geeksforgeeks.org/problems/fibonacci-series-up-to-nth-term/1))

---

## 📥 Input Format

- `N`: Positive integer, number of terms to generate.

---

## 📤 Output Format

- A list/array of integers representing the first `N` terms of the Fibonacci sequence (0‑indexed: starting from F(0) = 0).

---

## 🧪 Example Cases

- **Input:** `N = 5`  
  **Output:** `[0, 1, 1, 2, 3]`  
  **Explanation:** First five Fibonacci numbers.

- **Input:** `N = 8`  
  **Output:** `[0, 1, 1, 2, 3, 5, 8, 13]`

---

## 🛠️ Approach

Use recursion (optionally with memoization) or iteration:

- **Recursive (naive):** Recursively compute F(n) for each required term — but naive recursion yields exponential time for large `N`.
- **Optimized (with memoization or iterative build):** Build the sequence iteratively in O(n), or cache intermediate results in recursion to ensure each Fibonacci term is computed once.
