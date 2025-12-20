# Roman to Integer

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: hash-table, math, string, parsing

---

## 📝 Problem Statement

Given a Roman numeral string, convert it to its integer equivalent. Roman numerals are represented by seven symbols: I, V, X, L, C, D, and M, with respective values 1, 5, 10, 50, 100, 500, 1000. Normally numerals are written from largest to smallest from left to right — but some cases use subtractive notation:  
- I may precede V (5) or X (10) to make 4 or 9.  
- X may precede L (50) or C (100) to make 40 or 90.  
- C may precede D (500) or M (1000) to make 400 or 900.  

Given a valid Roman numeral representing a value in the inclusive range [1, 3999], return its integer value. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

- `s`: string — a valid Roman numeral composed only of the characters `'I'`, `'V'`, `'X'`, `'L'`, `'C'`, `'D'`, `'M'`.  
- `1 <= s.length <= 15`.  
- It is guaranteed that `s` represents a number between 1 and 3999. :contentReference[oaicite:1]{index=1}

---

## 📤 Output

- An integer — the decimal value corresponding to the Roman numeral.

## ✔️ Constraints

- `s.length` from 1 to 15. :contentReference[oaicite:2]{index=2}  
- `s` contains only valid Roman numeral characters: I, V, X, L, C, D, M. :contentReference[oaicite:3]{index=3}  

---

## ✅ Example

**Input:**  
"III"
**Output:**  
3
**Explanation:**  
III = 1 + 1 + 1 = 3  

**Input:**  
"MCMXCIV"
**Output:**  
1994
**Explanation:**  
M = 1000, CM = 900, XC = 90, IV = 4 → total 1994  

---

## 🛠️ Approach

- Build a mapping from Roman characters to integer values.  
- Traverse the string left to right: for each symbol, if its value is less than the value of the next symbol, subtract it; otherwise add it. This handles subtractive notation (like "IV", "IX", "XC", etc.).  
- Accumulate the total and return it.  