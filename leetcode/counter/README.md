# Counter Function

**Platform:** [LeetCode](https://leetcode.com/problems/counter/)  
**Category:** Closures / Functions  
**Difficulty:** Easy  
**Problem Statement:** Create a counter function that returns an incrementing sequence of numbers starting from `n` using closures. The function must maintain its internal state between calls without using global variables.

---

## � Problem Overview
The challenge is to implement a function that generates a counter starting from a given number `n`. Each call to the counter should return the next number in the sequence. The counter must use closures to maintain its state between function calls and should not rely on any global variables.

---

## 📥 Input Format
- `n`: Starting integer value (-1000 ≤ n ≤ 1000)

## 📤 Output Format
- Returns a function that, when called, returns the next number in the sequence.

## 🔍 Constraints
- `-1000 <= n <= 1000`
- `0 <= calls.length <= 1000`
- Each entry in `calls` is `"call"`
- Must use closure to maintain state (no global variables)

---

## 🧪 Sample Cases

### Example 1
**Input:** `n = 10`  
**Calls:** `["call","call","call"]`  
**Output:** `[10, 11, 12]`  
**Explanation:**  
- First call returns the initial value 10
- Second call returns 11 (10 + 1)
- Third call returns 12 (11 + 1)

### Example 2
**Input:** `n = -2`  
**Calls:** `["call","call","call","call","call"]`  
**Output:** `[-2, -1, 0, 1, 2]`  
**Explanation:**  
- The sequence starts at -2 and increments by 1 for each subsequent call

### Example 3
**Input:** `n = 0`  
**Calls:** `["call","call"]`  
**Output:** `[0, 1]`  
**Explanation:**  
- First call returns 0
- Second call returns 1 (0 + 1)

---

## 🧠 Approach
1. **Closure Implementation**: Create a function that captures the initial value `n` in its closure scope.
2. **State Management**: The inner function maintains access to the captured variable even after the outer function has finished execution.
3. **Incremental Logic**: Each call to the inner function returns the current value and then increments it for the next call.

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(1)` per operation  
  Each counter call performs a constant-time operation (increment and return).
  
- **Space Complexity**: `O(1)`  
  Only a single number is stored in the closure, regardless of the number of calls.

---

## 📝 Notes
- The counter can handle both positive and negative starting values
- The counter will continue to increment indefinitely with each call
- The implementation uses JavaScript's closure feature to maintain state between function calls
- The solution is memory efficient as it only stores the current value in the closure

## 🔗 Related Problems
- [Counter II](https://leetcode.com/problems/counter-ii/)
- [Create Hello World Function](https://leetcode.com/problems/create-hello-world-function/)
- [Memoize](https://leetcode.com/problems/memoize/)
