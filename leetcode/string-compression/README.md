# string compression

> **Difficulty**: medium  
> **Platform**: LeetCode  
> **Tags**: string, two pointers, array, in-place

---

## 📝 Problem Statement

Given an array of characters `chars`, compress it using the following rules:

- For each group of consecutive repeating characters:
  - If the group length is `1`, append only the character.
  - Otherwise, append the character followed by the group's length.
- The compressed result must be written **in-place** into the input array.
- Return the new length of the compressed array.

Group lengths of `10` or more must be split into individual digit characters.  
Only constant extra space is allowed.

---

## 📥 Input

- An array of characters `chars`

---

## 📤 Output

- An integer representing the new length of the compressed array
- The first `k` characters of `chars` contain the compressed result

## ✔️ Constraints

- `1 <= chars.length <= 2000`
- `chars[i]` may be a lowercase letter, uppercase letter, digit, or symbol

---

## ✅ Example

**Input**:
`["a","a","b","b","c","c","c"]`

**Output**:
`6`

**Compressed Array**:
`["a","2","b","2","c","3"]`

**Explanation**:
Consecutive character groups are `"aa"`, `"bb"`, and `"ccc"`, which compress to `"a2b2c3"`.

---

## 🧪 Test Cases

| #   | Input                                                 | Output |
| --- | ----------------------------------------------------- | ------ |
| 1   | ["a","a","b","b","c","c","c"]                         | 6      |
| 2   | ["a"]                                                 | 1      |
| 3   | ["a","b","b","b","b","b","b","b","b","b","b","b","b"] | 4      |

---

## 🛠️ Approach

The algorithm leverages a **two-pointer strategy**:

- One pointer iterates through the input array to identify character groups.
- A second pointer writes the compressed output back into the same array.
- For each group, the character is written once, followed by the digit characters of its count (if greater than one).

This ensures strict compliance with the **in-place constraint** while maintaining linear performance.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
