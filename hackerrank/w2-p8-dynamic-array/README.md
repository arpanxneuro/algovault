# Dynamic Array

> **Difficulty**: Easy  
> **Platform**: HackerRank  
> **Tags**: Array, Data Structure, Dynamic Programming

---

## 📝 Problem Statement

Implement a dynamic array with the following operations:
1. **Query Type 1 (1 x y)**:
   - Find the sequence at index `(x ^ lastAnswer) % N`
   - Append `y` to this sequence

2. **Query Type 2 (2 x y)**:
   - Find the sequence at index `(x ^ lastAnswer) % N`
   - Find the value at index `y % size` in this sequence
   - Update `lastAnswer` to this value
   - Print the new `lastAnswer`

Initialize `lastAnswer` to 0.

---

## 📥 Input

- The first line contains two space-separated integers:
  - `N`: Number of sequences (1 ≤ N ≤ 10^5)
  - `Q`: Number of queries (1 ≤ Q ≤ 10^5)
- The next `Q` lines each contain a query in one of the following formats:
  - `1 x y` (Type 1 query)
  - `2 x y` (Type 2 query)
  - Where 0 ≤ x, y ≤ 10^9

---

## 📤 Output

For each Type 2 query, print the value of `lastAnswer` on a new line.

## ✔️ Constraints

- 1 ≤ N, Q ≤ 10^5
- 0 ≤ x, y ≤ 10^9
- It is guaranteed that Type 2 queries reference valid indices

---

## ✅ Example

**Input**:
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

**Output**:
7
3


**Explanation**:
1. Initial: `lastAnswer = 0`, `arr = [[], []]`
2. Query 1 0 5: `seq = (0 ^ 0) % 2 = 0` → `arr = [[5], []]`
3. Query 1 1 7: `seq = (1 ^ 0) % 2 = 1` → `arr = [[5], [7]]`
4. Query 1 0 3: `seq = (0 ^ 0) % 2 = 0` → `arr = [[5, 3], [7]]`
5. Query 2 1 0: `seq = (1 ^ 0) % 2 = 1` → `lastAnswer = arr[1][0 % 1] = 7`
6. Query 2 1 1: `seq = (1 ^ 7) % 2 = 0` → `lastAnswer = arr[0][1 % 2] = 3`

---

## 🧪 Test Cases

| # | Input | Output |
|---|-------|--------|
| 1 | `2 5`<br>`1 0 5`<br>`1 1 7`<br>`1 0 3`<br>`2 1 0`<br>`2 1 1` | `7`<br>`3` |
| 2 | `3 4`<br>`1 0 1`<br>`1 1 2`<br>`2 1 0`<br>`2 1 1` | `1`<br>`2` |
| 3 | `1 3`<br>`1 0 1`<br>`1 0 2`<br>`2 0 1` | `2` |

---

## 🛠️ Approach

### Dynamic Array with XOR Hashing
1. **Initialization**:
   - Create an array of N empty sequences
   - Initialize `lastAnswer` to 0

2. **Processing Queries**:
   - For Type 1 (1 x y):
     - Calculate sequence index: `(x ^ lastAnswer) % N`
     - Append `y` to this sequence
   - For Type 2 (2 x y):
     - Calculate sequence index: `(x ^ lastAnswer) % N`
     - Find value at `y % sequence_size`
     - Update `lastAnswer` to this value
     - Print `lastAnswer`

### Time and Space Complexity
- **Time Complexity**: O(Q) - Each query is processed in constant time
- **Space Complexity**: O(N + Q) - To store up to Q elements across N sequences

---

## 📝 Note
- The XOR operation ensures uniform distribution of queries across sequences
- The modulo operation with sequence size ensures safe array access
- For large inputs, use efficient I/O operations
- The solution handles all edge cases, including:
  - Single sequence (N = 1)
  - Large number of queries
  - Maximum constraint values

## 🔗 Related Problems
- [Sparse Arrays](https://www.hackerrank.com/challenges/sparse-arrays)
- [Dynamic Array in C](https://www.hackerrank.com/challenges/crush)
- [Array Manipulation](https://www.hackerrank.com/challenges/crush)