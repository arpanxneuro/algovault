# Palindrome Number

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: math, two-pointers, number-theory

---

## 📝 Problem Statement

Given an integer `x`, return `true` if `x` is a palindrome integer. A palindrome integer reads the same backward and forward.

Examples:

- `121` is a palindrome — reads the same backward.
- `-121` is not a palindrome — the negative sign breaks the symmetry.
- `10` is not a palindrome — reversed digits produce `01`, which differs from `10`.

---

## 📥 Input

- `x`: integer, where `-2³¹ ≤ x ≤ 2³¹ - 1`.

---

## 📤 Output

- Boolean (`true` / `false`) — whether `x` is a palindrome integer or not.

## ✔️ Constraints

- The input integer `x` lies within the signed 32-bit integer range: `-2^{31} ≤ x ≤ 2^{31} - 1`.

---

## ✅ Example

**Input:**  
x = 121
**Output:**  
true
**Explanation:**  
121 reads the same forward and backward.

**Input:**  
x = -121
**Output:**  
false
**Explanation:**  
Negative numbers are not considered palindrome numbers due to the minus sign.

**Input:**  
x = 10
**Output:**  
false
**Explanation:**  
10 reversed is 01 — not equal to original number.

---

## 🛠️ Approach

1. **Handle Edge Cases First**

   - If `x` is negative: cannot be palindrome → return `false`.
   - If `x` ends with digit `0` and `x != 0`: cannot be palindrome (because reversed would start with `0`, which is invalid) → return `false`.

2. **Reverse Half the Number (without converting to string)**

   - Maintain a variable `reversedHalf = 0`.
   - While the original number (`x`) > `reversedHalf`:
     - Extract last digit of `x` → `digit = x % 10`,
     - Update `reversedHalf = reversedHalf * 10 + digit`,
     - Reduce `x = x // 10`.

3. **Compare Halves**

   - For even-length numbers: `x == reversedHalf` → palindrome.
   - For odd-length numbers: `x == reversedHalf // 10` → palindrome (ignoring the middle digit).

4. **Return Result**
