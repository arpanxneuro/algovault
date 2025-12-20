# Josephus Problem

> **Difficulty**: Medium  
> **Source**: GeeksforGeeks  
> **Tags**: recursion, mathematics, data‑structure, simulation

---

## 📝 Problem Statement

There are `n` people standing in a circle, numbered from 1 to `n`. Starting from person 1, every `k`‑th person is eliminated (i.e. skip `k‑1` persons, then eliminate the `k`th), and the process continues from the next person after the eliminated one. This continues until only one person remains. Find the position (1‑based index) of the last remaining person (the survivor). ([Josephus Problem — GeeksforGeeks](https://www.geeksforgeeks.org/josephus-problem/))

---

## 📥 Input Format

- `n`: integer, total number of people (1 ≤ n)
- `k`: integer, elimination step (1 ≤ k)

---

## 📤 Output Format

- Return an integer: the 1‑based position of the survivor (the last remaining person).

---

## 🧪 Example Cases

- **Input:** `n = 7, k = 3` → **Output:** `4`  
  **Explanation:** People eliminated in order — 3, 6, 2, 7, 5, 1; survivor is at position 4. :contentReference[oaicite:2]{index=2}
- **Input:** `n = 5, k = 2` → **Output:** `3` :contentReference[oaicite:3]{index=3}

### Additional Sample Cases

| n   | k   | Survivor |
| --- | --- | -------- |
| 1   | any | 1        |
| 4   | 2   | 1        |

---

## 🛠️ Approach

A classical way is via recursion or iterative dynamic programming using the recurrence:
