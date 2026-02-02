# plus one

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: math, rotation, array

---

## 📝 Problem Statement

Given an array and a number k, rotate the array to the right by k steps, where k is non-negative.

---

## 📥 Input

```
An integer array and integer k
```

---

## 📤 Output

```
Rotated array
```

## ✔️ Constraints

k may be greater than array length

---

## ✅ Example

**Input**:

```
[1,2,3,4,5,6,7], k = 3
```

**Output**:

```
[5,6,7,1,2,3,4]
```

**Explanation**:
Rotated right by 3 steps.

---

## 🧪 Test Cases

| #   | Input              | Output          |
| --- | ------------------ | --------------- |
| 1   | [1,2,3,4,5,6,7], 3 | [5,6,7,1,2,3,4] |

---

## 🛠️ Approach

Use reverse method: reverse whole array, then reverse first k and last n-k.

### Time and Space Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
