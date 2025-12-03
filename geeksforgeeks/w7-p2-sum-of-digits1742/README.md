# Sum of Digits Using Recursion

> **Difficulty**: easy  
> **Source**: GeeksforGeeks  
> **Tags**: number‑theory

---

## 📝 Problem Statement

Given a non‑negative integer `N`, write a recursive function to compute the sum of all its digits. For example, for `N = 1234`, the result is `1 + 2 + 3 + 4 = 10`. ([GfG – Sum of digits of a number using recursion](https://www.geeksforgeeks.org/sum-digit-number-using-recursion/))

---

## 📥 Input Format

- `N`: non‑negative integer (e.g., `0 ≤ N ≤ 10^9`)

---

## 📤 Output Format

- Integer: the sum of all digits in `N`.

---

## 🧪 Example Cases

**Input:** `1234` → **Output:** `10` (1 + 2 + 3 + 4)  
**Input:** `999` → **Output:** `27` (9 + 9 + 9)  
**Input:** `0` → **Output:** `0`

---

## 🛠️ Approach

Use recursion with digit‑extraction:
sumDigits(n):
if n == 0:
return 0
return (n % 10) + sumDigits(n // 10)

- Extract the last digit using `n % 10`.
- Recurse on the truncated number `n // 10`.
- Base case: when `n == 0`, return 0.

This ensures each digit is processed exactly once.

---

## 📊 Complexity Analysis

- **Time Complexity**: O(log₁₀ N) — roughly the number of digits in `N`. :contentReference[oaicite:0]{index=0}
- **Space Complexity**: O(log₁₀ N) — due to recursion stack depth. :contentReference[oaicite:1]{index=1}

---

## 📚 Notes & References

- Official GeeksforGeeks article covering recursion‑based digit‑sum computation. :contentReference[oaicite:2]{index=2}
