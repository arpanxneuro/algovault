# Array Reduce Transformation

> **Difficulty**: easy  
> **Platform**: LeetCode  
> **Tags**: array

---

## 📝 Problem Statement

Implement a custom reduce function that takes an array `nums`, a reducer `fn(accumulator, currentValue)`, and an initial value `init`, returning the aggregated value by applying `fn` sequentially over the array. When `nums` is empty, the result must equal `init`.

---

## 📥 Input

- `nums`: integer array of length `n` where `0 ≤ n ≤ 1000`
- `fn(accum, curr)`: reducer callback returning an integer
- `init`: integer initial accumulator value (0 ≤ init ≤ 1000)

---

## 📤 Output

- Return the final accumulated integer produced by applying `fn` to each element of `nums` from left to right, starting with `init`.

## ✔️ Constraints

- 0 ≤ nums.length ≤ 1000
- 0 ≤ nums[i] ≤ 1000
- 0 ≤ init ≤ 1000
- Do not use `Array.prototype.reduce`

---

## ✅ Example

**Input:**

```
nums = [1,2,3,4]
fn = (accum, curr) => accum + curr
init = 0
```

**Output:**  
`10`
**Explanation:** `Summing all elements yields 10.`

**Input:**

```nums = [1,2,3,4]
fn = (accum, curr) => accum + curr \* curr
init = 100
```

**Output:**  
`130`
**Explanation:** `Adds squares of each element to the accumulator starting at 100.`

**Input:**

```nums = []
fn = () => 0
init = 25
```

**Output:**  
`25`
**Explanation:** ``Empty arrays always return `init` without calling `fn`.``

---

## 🧪 Test Cases

| #   | Input                                           | Output |
| --- | ----------------------------------------------- | ------ |
| 1   | `[1,2,3,4], (accum,curr)=>accum+curr, 0`        | `10`   |
| 2   | `[1,2,3,4], (accum,curr)=>accum+curr*curr, 100` | `130`  |
| 3   | `[], ()=>0, 25`                                 | `25`   |

---

## 🛠️ Approach

1. Set a variable `acc` to `init`.
2. Iterate through `nums` in order.
3. For each value `curr`, update `acc = fn(acc, curr)`.
4. After the loop, return `acc`. For empty arrays, the loop is skipped and `init` is returned.

### Considerations

- The reducer can perform arbitrary arithmetic or stateful logic; the implementation must treat it as a black box.
- Ensure the reducer is invoked exactly once per element in original order.

---

### Time and Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
