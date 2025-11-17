# Function Composition

**Platform:** [LeetCode](https://leetcode.com/problems/function-composition/)  
**Category:** Functional Programming / Higher-Order Functions  
**Difficulty:** Easy  
**Problem Statement:** Create a function that composes an array of functions into a single function, where each function consumes the return value of the function that follows. The composition should work right-to-left, and an empty list of functions should return the identity function.

---

## 📘 Problem Overview
Given an array of functions `[f1, f2, f3, ..., fn]`, return a new function `fn(x)` that computes the composition of the array of functions. The composition of `[f1, f2, f3, ..., fn]` is the function `f(x) = f1(f2(f3(...(fn(x)))))`.

### Key Points:
- Function composition is the process of combining two or more functions to produce a new function
- The composition is done from right to left
- An empty list of functions should return the identity function `f(x) = x`
- All functions are guaranteed to be unary (accept exactly one argument)

---

## 📥 Input Format
- `functions`: An array of functions to be composed (0 ≤ functions.length ≤ 1000)
- `x`: The input value to the composed function (-1000 ≤ x ≤ 1000)

## 📤 Output Format
- Returns a function that takes one argument `x` and returns the result of the function composition
- The return value will be in the range `[-1000, 1000]`

## 🔍 Constraints
- `-1000 <= x <= 1000`
- `0 <= functions.length <= 1000`
- All functions in the array are unary (accept exactly one argument)
- `x` and all return values are guaranteed to be in the range `[-1000, 1000]`

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`functions = [x => x + 1, x => x * x, x => 2 * x]`  
`x = 4`  
**Output:** `65`  
**Explanation:**  
Evaluating from right to left:  
- Start with x = 4  
- 2 * 4 = 8  
- 8 * 8 = 64  
- 64 + 1 = 65  

### Example 2
**Input:**  
`functions = [x => 10 * x, x => 10 * x, x => 10 * x]`  
`x = 1`  
**Output:** `1000`  
**Explanation:**  
- 10 * 1 = 10  
- 10 * 10 = 100  
- 10 * 100 = 1000  

### Example 3
**Input:**  
`functions = []`  
`x = 42`  
**Output:** `42`  
**Explanation:**  
The composition of zero functions is the identity function `f(x) = x`.

---

## 🧠 Approach
1. **Right-to-Left Execution**: Process functions in reverse order (right-to-left)
2. **Reduce Pattern**: Use `reduceRight` to apply each function to the accumulated result
3. **Identity Function**: Return the input directly if no functions are provided
4. **Function Composition**: Chain the functions such that the output of one becomes the input of the next

### Solution Code
```javascript
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        return functions.reduceRight((acc, fn) => fn(acc), x);
    }
};
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(n)`  
  Where n is the number of functions. Each function is called exactly once.
  
- **Space Complexity**: `O(1)`  
  The space used is constant as we only store the intermediate result.

---

## 📝 Notes
- The solution uses JavaScript's `reduceRight` for clean right-to-left function application
- The identity function case (empty array) is handled naturally by the implementation
- All functions are assumed to be pure (no side effects) and unary (single argument)
- The solution is concise yet readable, making good use of functional programming principles

## 🔗 Related Problems
- [Compose](https://leetcode.com/problems/compose/)
- [Function Composition](https://leetcode.com/problems/function-composition/)
- [Memoize](https://leetcode.com/problems/memoize/)

## 📚 Additional Resources
- [MDN: Function Composition](https://developer.mozilla.org/en-US/docs/Glossary/Function_composition)
- [JavaScript.info: Function Composition](https://javascript.info/currying-partials#going-partial-without-context)