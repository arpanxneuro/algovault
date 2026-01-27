# length of last word

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: string, simulation

---

## 📝 Problem Statement

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A word is defined as a maximal substring consisting only of non-space characters.  
There will be at least one word in `s`. :contentReference[oaicite:1]{index=1}

---

## 📥 Input

```
s = "Hello World"
```

---

## 📤 Output

```
5
```

## ✔️ Constraints

- `1 <= s.length <= 10^4`
- `s` consists only of English letters and spaces `' '`
- There will be at least one word in `s`. :contentReference[oaicite:2]{index=2}

---

## ✅ Example

**Input**:

```
s = " fly me to the moon "
```

**Output**:

```
4
```

**Explanation**:  
The last word is `"moon"` which has a length of 4. :contentReference[oaicite:3]{index=3}

---

## 🧪 Test Cases

| #   | Input                           | Output |
| --- | ------------------------------- | ------ |
| 1   | `"Hello World"`                 | `5`    |
| 2   | `"   fly me   to   the moon  "` | `4`    |
| 3   | `"luffy is still joyboy"`       | `6`    |

---

## 🛠️ Approach

**Iterative Backward Scan**

- Traverse the string from end to start.
- Skip all trailing spaces first.
- Count characters until either the start of the string is reached or a space is encountered.
- Return the count as the length of the last word. :contentReference[oaicite:4]{index=4}

This avoids additional memory overhead and handles trailing spaces effectively.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
