# Power of Numbers (Recursive)

> **Difficulty**: Medium  
> **Topic**: Modular Exponentiation, Recursion / Divide & Conquer

---

## 📝 Problem Statement

Implement a function that calculates `power(N, P)`, which computes `N^P % (10^9 + 7)` for given integers `N` and non-negative integer `P`.

---

## 📥 Input Format

- `N`: integer, `1 ≤ N ≤ 10^6`
- `P`: non-negative integer, `0 ≤ P ≤ 10^6`

---

## 📤 Output Format

- Return `(N^P) mod (10^9 + 7)`

---

## 🛠️ Approach

Use binary (divide‑and‑conquer) recursion (or iterative exponentiation by squaring) under modulo to compute power in `O(log P)` time.

**Algorithm (recursive):**

- Base cases: if `P == 0`, return `1`; if `P == 1`, return `N % MOD`.
- Else recursively compute:
  - `half = power(N, P // 2)`
  - If `P` is even → return `(half * half) % MOD`
  - Else → return `(N % MOD * half * half) % MOD`

---

## ✅ Example

- `N = 2, P = 3` → output `8`
- `N = 2, P = 5` → output `32`

---

## 📊 Complexity Analysis

- **Time Complexity**: `O(log P)`
- **Space Complexity**: `O(log P)` due to recursion stack

---

## 📚 Notes

This is a standard modular exponentiation implementation suited for large exponents. For extremely large exponents or repeated queries — iterative or fast‑power loop may be preferred to avoid recursion overhead.
