# Sleep

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: promise, async-programming, concurrency

---

## 📝 Problem Statement

Given a positive integer `millis`, write an async function that sleeps for `millis` milliseconds. It can resolve with any value.

---

## 📥 Input

- `millis`: A positive integer (1 ≤ millis ≤ 1000)
  - Represents the number of milliseconds to sleep

---

## 📤 Output

- Returns a Promise that resolves after the specified delay
- The resolved value can be anything (or undefined)

## ✔️ Constraints

- 1 ≤ millis ≤ 1000
- The function must be asynchronous and return a Promise
- The Promise should not resolve before the specified delay

---

## ✅ Example

**Input:**  
100
**Output:**  
Promise resolved after ~100ms
**Input:**  
200
**Output:**  
Promise resolved after ~200ms

---

## 🧪 Test Cases

| #   | Input  | Output                           |
| --- | ------ | -------------------------------- |
| 1   | `100`  | `Promise resolves after ~100ms`  |
| 2   | `200`  | `Promise resolves after ~200ms`  |
| 3   | `1000` | `Promise resolves after ~1000ms` |

---

## 🛠️ Approach

1. Create a Promise.
2. Use `setTimeout` inside the Promise executor to delay resolution.
3. Resolve the Promise after the specified `millis`.
4. The function works with both `async/await` and Promise chaining.

---

### Time and Space Complexity

- **Time Complexity:** O(1) — the timer is created and handled asynchronously
- **Space Complexity:** O(1) — only a constant amount of space is used

---

## 🔗 Related Problems

- [Promise Time Limit](https://leetcode.com/problems/promise-time-limit/)
- [Promise Pool](https://leetcode.com/problems/promise-pool/)
- [Debounce](https://leetcode.com/problems/debounce/)
