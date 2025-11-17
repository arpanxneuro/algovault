# Sleep

**Platform:** [LeetCode](https://leetcode.com/problems/sleep/)  
**Category:** Asynchronous Programming / Promises  
**Difficulty:** Easy  
**Problem Statement:** Given a positive integer `millis`, write an async function that sleeps for `millis` milliseconds. It can resolve with any value.

---

## 📘 Problem Overview
This problem requires implementing a sleep function that pauses execution for a specified number of milliseconds. The function should be asynchronous and return a Promise that resolves after the given delay.

### Key Points:
- The function should return a Promise
- The Promise should resolve after at least `millis` milliseconds
- The function should work with both `async/await` and Promise chaining
- The solution should be non-blocking and leverage JavaScript's event loop
- The function can resolve with any value or no value
- The actual delay may be slightly longer due to JavaScript's single-threaded nature

---

## 📥 Input Format
- `millis`: A positive integer (1 ≤ millis ≤ 1000)
  - Represents the number of milliseconds to sleep

## 📤 Output Format
- Returns a Promise that resolves after the specified delay
- The resolved value can be anything (or undefined)

## 🔍 Constraints
- `1 <= millis <= 1000`
- The function must be asynchronous and return a Promise
- The Promise should not resolve before the specified delay

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`100`  
**Explanation:**  
The function should sleep for 100 milliseconds

### Example 2
**Input:**  
`200`  
**Explanation:**  
The function should sleep for 200 milliseconds

### Example 3
**Input:**  
`1000`  
**Explanation:**  
The function should sleep for 1000 milliseconds (1 second)

---

## 🧠 Approach
1. **Create a Promise**: The function should return a Promise
2. **Use setTimeout**: Inside the Promise executor, use `setTimeout` to delay the resolution
3. **Resolve the Promise**: After the specified delay, resolve the Promise
4. **Handle Edge Cases**: Ensure the function works with minimum and maximum allowed values

### Solution Code (JavaScript)
```javascript
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise((resolve) => {
        setTimeout(resolve, millis);
    });
}

/** 
 * Example usage:
 * let t = Date.now();
 * sleep(100).then(() => {
 *   console.log(Date.now() - t); // ~100
 * });
 */
```

### Solution Code (TypeScript)
```typescript
async function sleep(millis: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, millis));
}
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(1)`  
  - The function creates a single timer and resolves immediately after the delay
  - The actual delay is handled by the browser/Node.js event loop
  
- **Space Complexity**: `O(1)`  
  - We only use a constant amount of space
  - The Promise and timer are managed by the JavaScript runtime

---

## 📝 Notes
- The sleep function is non-blocking and allows other code to run during the delay
- The actual delay might be slightly longer than specified due to JavaScript's event loop
- This is a fundamental building block for implementing timeouts, retries, and rate limiting
- The function can be used with both async/await and Promise chaining

## 🔗 Related Problems
- [Promise Time Limit](https://leetcode.com/problems/promise-time-limit/)
- [Promise Pool](https://leetcode.com/problems/promise-pool/)
- [Debounce](https://leetcode.com/problems/debounce/)

## 📚 Additional Resources
- [MDN: setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)
- [JavaScript.info: Promises](https://javascript.info/promise-basics)
- [You Don't Know JS: Async & Performance](https://github.com/getify/You-Dont-Know-JS/tree/1st-ed/async%20%26%20performance)
- [JavaScript Event Loop Explained](https://www.youtube.com/watch?v=8aGhZQkoFbQ)
