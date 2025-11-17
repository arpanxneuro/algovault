# Josephus Problem

> **Difficulty**: Medium  
> **Companies**: Amazon, Microsoft, Google, Adobe

---

## 📝 Problem Statement

Given the total number of people `n` and a number `k` which indicates that `k-1` persons are skipped and the `k-th` person is eliminated in a circle. The task is to find the position of the last remaining person.

---

## 📥 Input

- `n`: An integer representing the total number of people in the circle (1 ≤ n ≤ 10^5).
- `k`: An integer representing the step size for elimination (1 ≤ k ≤ 10^5).

---

## 📤 Output

Return the position (1-based index) of the last remaining person.

---

## ✔️ Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ k ≤ 10^5

---

## ✅ Example

**Input**
n = 7, k = 3

**Output**
4


**Explanation**:
1. People are in a circle: 1, 2, 3, 4, 5
2. First, the person at position 3 is eliminated: 1, 2, 4, 5
3. Next, the person at position 1 is eliminated: 2, 4, 5
4. Next, the person at position 5 is eliminated: 2, 4
5. Next, the person at position 2 is eliminated: 4
6. The last remaining person is at position 4.

---

## 🧪 Test Cases

| # | n | k | Output |
|---|---|---|--------|
| 1 | 5 | 3 | 4 |
| 2 | 7 | 3 | 4 |
| 3 | 4 | 2 | 1 |
| 4 | 1 | 1 | 1 |
| 5 | 40 | 7 | 28 |

---

## 🛠️ Approach

### Recursive Approach
1. **Base Case**: If there's only one person, return 0 (0-based index).
2. **Recursive Case**: The position of the last remaining person in a circle of size `n` can be derived from the position in a circle of size `n-1` using the formula: