# Counter II

**Platform:** [LeetCode](https://leetcode.com/problems/counter-ii/)  
**Category:** Closures / Objects  
**Difficulty:** Easy  
**Problem Statement:** Create a counter object with methods to increment, decrement, and reset an internal counter. The counter should maintain its state between method calls using closures.

---

## 📘 Problem Overview
Implement a function `createCounter(init)` that returns an object with three methods that modify an internal counter value starting from `init`:
- `increment()`: Increases the counter by 1 and returns the new value
- `decrement()`: Decreases the counter by 1 and returns the new value
- `reset()`: Resets the counter to `init` and returns it

---

## 📥 Input Format
- `init`: Initial integer value (-1000 ≤ init ≤ 1000)
- `calls`: Array of method names ("increment", "decrement", or "reset") to be called in sequence

## 📤 Output Format
- Returns an array of values returned by each method call in sequence

## 🔍 Constraints
- `-1000 <= init <= 1000`
- `0 <= calls.length <= 1000`
- `calls[i]` is one of `["increment", "decrement", "reset"]`
- Must use closure to maintain state (no global variables)

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`init = 5`  
`calls = ["increment", "reset", "decrement"]`  
**Output:** `[6, 5, 4]`  
**Explanation:**  
- counter.increment() → 5 + 1 = 6
- counter.reset() → resets to 5
- counter.decrement() → 5 - 1 = 4

### Example 2
**Input:**  
`init = 0`  
`calls = ["increment", "increment", "decrement", "reset", "reset"]`  
**Output:** `[1, 2, 1, 0, 0]`  
**Explanation:**  
- counter.increment() → 0 + 1 = 1
- counter.increment() → 1 + 1 = 2
- counter.decrement() → 2 - 1 = 1
- counter.reset() → resets to 0
- counter.reset() → already at 0, returns 0

### Example 3
**Input:**  
`init = -1`  
`calls = ["increment", "decrement", "reset"]`  
**Output:** `[0, -1, -1]`  
**Explanation:**  
- counter.increment() → -1 + 1 = 0
- counter.decrement() → 0 - 1 = -1
- counter.reset() → resets to -1

---

## 🧠 Approach
1. **Closure Implementation**: Capture the initial value `init` in a closure
2. **State Management**: Maintain the current value in the closure scope
3. **Method Definitions**: Return an object with three methods that modify the captured value
   - `increment()`: Increments and returns the current value
   - `decrement()`: Decrements and returns the current value
   - `reset()`: Resets to the initial value and returns it

### Solution Code
```javascript
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let current = init;
    
    return {
        increment: () => ++current,
        decrement: () => --current,
        reset: () => (current = init, current)
    };
};
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(1)` per operation  
  Each method call performs a constant-time operation (increment, decrement, or reset).
  
- **Space Complexity**: `O(1)`  
  Only a single number is stored in the closure, regardless of the number of operations.

---

## 📝 Notes
- The counter maintains its state between method calls using closure
- The reset operation returns the counter to its original initial value
- All operations are performed in constant time
- The solution is memory efficient, using only O(1) extra space

## 🔗 Related Problems
- [Counter](https://leetcode.com/problems/counter/)
- [Create Hello World Function](https://leetcode.com/problems/create-hello-world-function/)
- [Memoize](https://leetcode.com/problems/memoize/)
