# reverse words in a string

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: string, two pointers, parsing

---

## 📝 Problem Statement

Given an input string `s`, reverse the order of the words in the string.

A word is defined as a sequence of non-space characters. Words in the string are separated by at least one space. The returned string must contain exactly one space between words, with no leading or trailing spaces.

---

## 📥 Input

- A string `s` that may contain leading spaces, trailing spaces, or multiple spaces between words

---

## 📤 Output

- A string with the words in reversed order, separated by a single space

## ✔️ Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces
- There is at least one word in `s`

---

## ✅ Example

**Input**:
s = " hello world "
**Output**:
world hello

**Explanation**:
Leading and trailing spaces are removed, multiple spaces between words are reduced to one, and the word order is reversed.

---

## 🧪 Test Cases

| #   | Input             | Output            |
| --- | ----------------- | ----------------- |
| 1   | "the sky is blue" | "blue is sky the" |
| 2   | " hello world "   | "world hello"     |
| 3   | "a good example"  | "example good a"  |

---

## 🛠️ Approach

The solution involves parsing the string to extract valid words while ignoring extra spaces. Once extracted, the word list is reversed and joined using a single space. This approach ensures correctness while maintaining readability and robustness.

For environments where the string is mutable, the problem can be extended to an in-place solution using string reversal and space normalization techniques.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
