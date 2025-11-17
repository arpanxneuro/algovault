# Palindrome Number

**Platform:** [LeetCode](https://leetcode.com/problems/palindrome-number/)  
**Category:** Math / Two Pointers  
**Difficulty:** Easy  
**Problem Statement:** Given an integer `x`, return `true` if `x` is a palindrome integer. An integer is a palindrome when it reads the same backward as forward.

---

## 📘 Problem Overview
A palindrome number is a number that remains the same when its digits are reversed. For example, 121 is a palindrome while 123 is not.

### Key Points:
- Negative numbers cannot be palindromes (e.g., -121 is not a palindrome)
- Numbers ending with 0 (except 0 itself) cannot be palindromes
- The solution should be optimized to not use extra space (O(1) space complexity)
- The solution should be efficient with time complexity O(log n)

---

## 📥 Input Format
- `x`: An integer (-2³¹ ≤ x ≤ 2³¹ - 1)

## 📤 Output Format
- Returns `true` if `x` is a palindrome, `false` otherwise.

## 🔍 Constraints
- `-2³¹ <= x <= 2³¹ - 1`

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`x = 121`  
**Output:** `true`  
**Explanation:**  
121 reads the same from left to right and right to left.

### Example 2
**Input:**  
`x = -121`  
**Output:** `false`  
**Explanation:**  
From left to right, it reads -121. From right to left, it becomes 121-.

### Example 3
**Input:**  
`x = 10`  
**Output:** `false`  
**Explanation:**  
Reads 01 from right to left, which is not equal to 10.

### Example 4
**Input:**  
`x = 0`  
**Output:** `true`  
**Explanation:**  
0 reads the same from left to right and right to left.

### Example 5
**Input:**  
`x = 12321`  
**Output:** `true`  
**Explanation:**  
12321 reads the same from left to right and right to left.

---

## 🧠 Approach
1. **Handle Edge Cases**:
   - If `x` is negative, return `false`
   - If `x` is 0, return `true`
   - If `x` is a positive number ending with 0 (except 0), return `false`

2. **Reverse Half of the Number**:
   - Initialize `reversed_num` to 0
   - While `x` is greater than `reversed_num`:
     - Append the last digit of `x` to `reversed_num`
     - Remove the last digit from `x`

3. **Check for Palindrome**:
   - If `x` equals `reversed_num` (even length) or `x` equals `reversed_num // 10` (odd length), return `true`
   - Otherwise, return `false`

### Solution Code (Python)
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases:
        # 1. Negative numbers are not palindromes
        # 2. If last digit is 0, first digit must also be 0 (only 0 satisfies this)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_num = 0
        # Only reverse half of the number to avoid overflow
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
            
        # When the length is odd, we can get rid of the middle digit
        return x == reversed_num or x == reversed_num // 10
```

### Solution Code (TypeScript)
```typescript
function isPalindrome(x: number): boolean {
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }
    
    let reversed = 0;
    let original = x;
    
    while (original > reversed) {
        reversed = reversed * 10 + original % 10;
        original = Math.floor(original / 10);
    }
    
    return original === reversed || original === Math.floor(reversed / 10);
}
```

### Solution Code (C)
```c
#include <stdbool.h>

bool isPalindrome(int x) {
    // Edge cases:
    // 1. Negative numbers are not palindromes
    // 2. If last digit is 0, first digit must also be 0 (only 0 satisfies this)
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }
    
    int reversed = 0;
    // Only reverse half of the number to avoid overflow
    while (x > reversed) {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }
    
    // When the length is odd, we can get rid of the middle digit
    return x == reversed || x == reversed / 10;
}
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(log n)`  
  - We divide the input by 10 for every iteration, so the time complexity is O(log₁₀n)
  
- **Space Complexity**: `O(1)`  
  - We only use a constant amount of extra space

---

## 📝 Notes
- The solution efficiently checks for palindromes without converting the number to a string
- By only reversing half of the number, we optimize both time and space complexity
- The solution handles all edge cases including negative numbers and numbers ending with 0
- The algorithm is efficient with O(log n) time complexity and O(1) space complexity

## 🔗 Related Problems
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
- [Palindrome Number II](https://leetcode.com/problems/palindromic-substrings/)

## 📚 Additional Resources
- [LeetCode Article: Palindrome Number](https://leetcode.com/articles/palindrome-number/)
- [GeeksforGeeks: Check if a number is a palindrome](https://www.geeksforgeeks.org/check-if-a-number-is-palindrome/)
- [Tech Interview Handbook: Palindrome Number](https://www.techinterviewhandbook.org/algorithms/number/#palindrome-number)

---

## 🧪 Test Cases

| No test cases | - | - |

**Time Complexity:** O(n)

**Space Complexity:** O(1)
