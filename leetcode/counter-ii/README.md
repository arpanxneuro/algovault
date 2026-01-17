# Counter II

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: closure, object, design

---

## 📝 Problem Statement

Write a function `createCounter(init)` which accepts an integer `init`. It should return an object with three methods:

- `increment()`: increases the internal counter value by 1, and returns the new value.
- `decrement()`: decreases the internal counter value by 1, and returns the new value.
- `reset()`: resets the internal counter value to the original `init`, and returns it.

---

## 📥 Input

- `init`: initial integer value (constraints: `-1000 <= init <= 1000`)
- `calls`: array of method names (`"increment"`, `"decrement"`, or `"reset"`) to be invoked sequentially.

---

## 📤 Output

- Returns an array of values — each corresponding to the return value of the respective method call in `calls`.

## ✔️ Constraints

- `-1000 <= init <= 1000`
- At most 1000 method calls.
- Methods invoked are strictly among `"increment"`, `"decrement"`, or `"reset"`.

---

## ✅ Example

**Example 1**  
**Input:**  
init = 5
calls = ["increment", "reset", "decrement"]
**Output:**  
[6, 5, 4]
**Explanation:**

- `increment()` → 6
- `reset()` → 5
- `decrement()` → 4

**Example 2**  
**Input:**  
init = 0
calls = ["increment", "increment", "decrement", "reset", "reset"]
**Output:**  
[1, 2, 1, 0, 0]
**Explanation:** Follows increment/decrement/reset operations as defined.

---

## 🛠️ Approach

- Use closure to capture `init` and maintain an internal mutable variable (say `current`).
- Return an object with three methods referencing that internal state:
  - `increment()` → increment `current` by 1 and return it.
  - `decrement()` → decrement `current` by 1 and return it.
  - `reset()` → set `current = init`, return `current`.
- All operations are constant-time and constant-space.
