# valid parentheses

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: string, stack

---

## 📝 Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.  
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

A string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.  
- `1 <= s.length <= 10^4`  
- `s` consists only of parentheses characters. :contentReference[oaicite:1]{index=1}

---

## 📤 Output

Return `true` if the string is valid, or `false` otherwise.

## ✔️ Constraints

- Only parentheses characters are present in the input string.  
- Validity requires correct type matching and proper order of closures. :contentReference[oaicite:2]{index=2

---

## ✅ Example

**Input**:
```
s = "()"
```

**Output**:
```
true
```

**Input**:
```
s = "([])"
```

**Output**:
```
true
```

**Input**:
```
s = "([)]"
```
**Output**:
```
false
```

---

## 🧪 Test Cases

| # | Input           | Output |
|---|-----------------|--------|
| 1 | `"()"`          | true   |
| 2 | `"()[]{}"`      | true   |
| 3 | `"(]"`          | false  |
| 4 | `"([])"`        | true   |
| 5 | `"([)]"`        | false  |

---

## 🛠️ Approach

Use a **stack** to enforce matching and order:

1. Create a mapping from closing to opening brackets.  
2. Traverse each character in `s`.  
3. If it’s an opening bracket, push it onto the stack.  
4. If it’s a closing bracket, check if the stack is non-empty and the top matches; otherwise return `false`.  
5. At the end, if the stack is empty then every bracket matched correctly. :contentReference[oaicite:3]{index=3}

### Time and Space Complexity
- **Time Complexity**: O(n) — traverse the string once  
- **Space Complexity**: O(n) — stack storage in worst case
