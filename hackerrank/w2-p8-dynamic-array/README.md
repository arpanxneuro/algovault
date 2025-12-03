# Dynamic Array

> **Difficulty**: easy  
> **Platform**: HackerRank  
> **Tags**: array, data‑structure, dynamic‑array

---

## 📝 Problem Statement

Implement a dynamic array of sequences and process a series of queries: initialize `N` empty sequences, and maintain an integer `lastAnswer = 0`. Depending on the query type, either append to a sequence or read from a sequence to update `lastAnswer`. Return / print `lastAnswer` after each relevant query. :contentReference[oaicite:3]{index=3}

---

## 📥 Input

- First line: two space‑separated integers `N` (number of sequences) and `Q` (number of queries). :contentReference[oaicite:4]{index=4}
- Next `Q` lines: each contains a query of one of two types:
  - `1 x y` — append operation
  - `2 x y` — value‑fetch operation :contentReference[oaicite:5]{index=5}

All indices and values satisfy problem constraints; queries are guaranteed valid per the platform. :contentReference[oaicite:6]{index=6}

---

## 📤 Output

For each query of type `2`, output the updated `lastAnswer` on a new line — in the order the queries are processed. :contentReference[oaicite:7]{index=7}

---

## 🛠️ Operations & Logic

Maintain a list `seqList` of `N` initially‑empty sequences (0‑indexed). Maintain integer `lastAnswer = 0`.

For each query:

- If it is `1 x y`:

  - Compute `idx = (x ^ lastAnswer) % N`
  - Append `y` to `seqList[idx]` :contentReference[oaicite:8]{index=8}

- If it is `2 x y`:
  - Compute `idx = (x ^ lastAnswer) % N`
  - Let `size = length of seqList[idx]`
  - Update `lastAnswer = seqList[idx][ y % size ]`
  - Output / store `lastAnswer` :contentReference[oaicite:9]{index=9}

This solves the problem in a straightforward way. :contentReference[oaicite:10]{index=10}

---

## ⏱️ Complexity

- **Time Complexity:** O(Q) — each query (append or fetch) is processed in constant amortized time using dynamic arrays.
- **Space Complexity:** O(N + total_appended_values) — storing `N` sequences and all appended elements.

---

## 📌 Constraints & Considerations

- `1 ≤ N, Q ≤ 10^5` — large limits, so solution must be efficient. :contentReference[oaicite:11]{index=11}
- `x, y` up to large integers (e.g. 10⁹), but modulo operations and indexing logic ensure valid accesses. :contentReference[oaicite:12]{index=12}
- Ensure efficient I/O and memory‑efficient sequence storage (e.g. dynamic/resizable arrays), especially under C or low‑level languages.
