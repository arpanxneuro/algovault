# 242. valid anagram

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: strings, hash table, sorting

---

## 📝 Problem Statement

Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.  
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. :contentReference[oaicite:0]{index=0}

---

## 📥 Input

```
Two strings:
s = "anagram"
t = "nagaram"
```

---

## 📤 Output

```
true
```

## ✔️ Constraints

- `1 <= s.length, t.length <= 5 * 10⁴`
- `s` and `t` consist of lowercase English letters. :contentReference[oaicite:1]{index=1}

---

## ✅ Example

**Input**:

```
s = "anagram", t = "nagaram"
```

**Output**:

```
true
```

**Explanation**:
`t` contains exactly the same letters as `s` with identical frequencies, only in a different order. :contentReference[oaicite:2]{index=2}

---

## 🧪 Test Cases

| #   | Input                        | Output |
| --- | ---------------------------- | ------ |
| 1   | s = "anagram", t = "nagaram" | true   |
| 2   | s = "rat", t = "car"         | false  |

---

## 🛠️ Approach

To determine whether the second string is an anagram of the first:

1. Check if the lengths of `s` and `t` are equal.
2. Count occurrences of each character in `s`.
3. Subtract the count for each character found in `t`.
4. If all counts return to zero and no mismatches occur, return `true`. Otherwise, return `false`.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
