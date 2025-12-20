# Filter Elements from Array

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array, higher‑order‑functions, functional‑programming

---

## 📝 Problem Statement

You are given an integer array `arr` and a filtering function `fn`. Your task is to return a new array containing only those elements `arr[i]` for which `fn(arr[i], i)` returns a truthy value. You must implement this functionality **without** using the built-in `Array.filter` method. ([LeetCode #2634 Filter Elements from Array](https://leetcode.com/problems/filter-elements-from-array/))

---

## 📥 Input Format

- `arr`: integer array, where `0 ≤ arr.length ≤ 1000`. Each element `arr[i]` satisfies `-10^9 ≤ arr[i] ≤ 10^9`. :contentReference[oaicite:0]{index=0}
- `fn`: a callback function that receives two arguments — the element value and its index — i.e., `fn(element, index)`.

---

## 📤 Output Format

- Return a new array containing elements from `arr` that satisfy the predicate. Order must be preserved.

## ✔️ Constraints

- The filtering must be done without using `Array.prototype.filter`. :contentReference[oaicite:1]{index=1}
- Worst‑case array length: 1000. Elements in range ±10⁹. :contentReference[oaicite:2]{index=2}

---

## 🧪 Example Cases

**Example 1**  
Input:  
arr = [0, 10, 20, 30]
fn = n => n > 10
Output:  
[20, 30]
Explanation: Only 20 and 30 are greater than 10. :contentReference[oaicite:3]{index=3}

**Example 2**  
Input:  
arr = [1, 2, 3]
fn = (n, i) => i === 0
Output:  
[1]
Explanation: Only the element at index 0 is kept. :contentReference[oaicite:4]{index=4}

**Example 3**  
Input:  
arr = [-2, -1, 0, 1, 2]
fn = n => n + 1
Output:  
[-2, 0, 1, 2]
Explanation: `fn(n)` returns truthy for all except when `n + 1` evaluates to a falsy value (i.e. 0) — so 0 is excluded. :contentReference[oaicite:5]{index=5}

---

## 🛠️ Approach

- Initialize an empty result array.
- Iterate over each element `arr[i]` with its index `i`:
  - Evaluate `fn(arr[i], i)`.
  - If the result is truthy (i.e. `Boolean(fn(arr[i], i)) === true`), push `arr[i]` into result.
- Return the result array. This manual loop replicates the behavior of `filter` without using the built-in method. :contentReference[oaicite:6]{index=6}
