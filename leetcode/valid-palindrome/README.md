# valid palindrome

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: string, two-pointers, palindrome

---

## 📝 Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

- A string `s` of printable ASCII characters, including letters, numbers, spaces, and punctuation. :contentReference[oaicite:1]{index=1}

---

## 📤 Output

Return `true` if the cleaned and normalized string reads the same forward and backward; otherwise return `false`. :contentReference[oaicite:2]{index=2}

## ✔️ Constraints

- `1 <= s.length <= 2 * 10⁵`
- `s` consists only of printable ASCII characters. :contentReference[oaicite:3]{index=3}

---

## ✅ Example

**Input**:
s = "A man, a plan, a canal: Panama"
**Output**:
true
**Explanation**:
After removing non-alphanumeric characters and converting to lowercase, the string becomes `"amanaplanacanalpanama"` which is a palindrome. :contentReference[oaicite:4]{index=4}

---

## 🧪 Test Cases

| #   | Input                              | Output |
| --- | ---------------------------------- | ------ |
| 1   | `"A man, a plan, a canal: Panama"` | true   |
| 2   | `"race a car"`                     | false  |
| 3   | `" "`                              | true   |
| 4   | `"Ab@#Ba"`                         | true   |

---

## 🛠️ Approach

Use the **two-pointer** technique to check palindrome validity in **O(n)** time with **O(1)** extra space:

1. Initialize two pointers, `left` at the start and `right` at the end of the string.
2. While `left < right`:
   - Advance `left` while `s[left]` is not alphanumeric.
   - Decrement `right` while `s[right]` is not alphanumeric.
   - Compare the lowercase of `s[left]` and `s[right]`. If they differ, return `false`.
   - Move both pointers inward.
3. If all valid pairs match, return `true`. :contentReference[oaicite:5]{index=5}

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (excluding input)
