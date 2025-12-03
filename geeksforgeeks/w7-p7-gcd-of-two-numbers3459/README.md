# GCD of Two Numbers (Recursive)

> **Difficulty**: Easy  
> **Source**: GeeksforGeeks  
> **Tags**: mathematical, algorithms

---

## 📝 Problem Statement

Write a recursive function to find the greatest common divisor (GCD) of two non‑negative integers A and B. The GCD is the largest positive integer that divides both numbers without leaving a remainder. ([GeeksforGeeks – GCD of Two Numbers](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1))

---

## 📥 Input Format

- `A`: non‑negative integer (0 ≤ A ≤ 10⁹)
- `B`: non‑negative integer (0 ≤ B ≤ 10⁹)

At least one of `A` or `B` is non-zero.

---

## 📤 Output Format

- Return a non‑negative integer — the GCD of `A` and `B`.

---

## 🧪 Example Cases

| Input            | Output | Explanation                                             |
| ---------------- | ------ | ------------------------------------------------------- |
| `A = 24, B = 36` | `12`   | Divisors of 24 and 36, largest common divisor is 12.    |
| `A = 35, B = 10` | `5`    | 5 is the largest integer dividing both 35 and 10.       |
| `A = 0, B = 5`   | `5`    | GCD(0, b) = b (when b ≠ 0)                              |
| `A = 13, B = 13` | `13`   | Same numbers → GCD is the number itself                 |
| `A = 0, B = 0`   | `0`    | As per implementation (though mathematically undefined) |

---

## 🛠️ Approach

Use the recursive version of the Euclidean Algorithm to compute GCD in O(log (min(A,B))) time:
