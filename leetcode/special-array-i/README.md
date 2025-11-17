# Special Array I

**Platform:** [LeetCode](https://leetcode.com/problems/special-array-i/)  
**Category:** Array / Simulation  
**Difficulty:** Easy  
**Problem Statement:** An array is considered **special** if every pair of its adjacent elements has opposite parity (one even and one odd). Given an array `nums`, return `true` if the array is special, otherwise return `false`.

---

## 📘 Problem Overview
An array is special if for every pair of adjacent elements, one is even and the other is odd. This means the array must alternate between even and odd numbers throughout its length.

### Key Points:
- A single-element array is always considered special
- The array can start with either an even or odd number
- The parity must alternate strictly between adjacent elements
- The solution should be efficient with time complexity O(n) and space complexity O(1)

---

## 📥 Input Format
- `nums`: An array of integers (1 ≤ nums.length ≤ 100)
  - Each element nums[i] is an integer (0 ≤ nums[i] ≤ 100)

## 📤 Output Format
- Returns `true` if the array is special, `false` otherwise

## 🔍 Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`[1]`  
**Output:** `true`  
**Explanation:**  
A single-element array is always special.

### Example 2
**Input:**  
`[2, 1, 4]`  
**Output:** `true`  
**Explanation:**  
- (2, 1) → even–odd
- (1, 4) → odd–even
All adjacent pairs have opposite parity.

### Example 3
**Input:**  
`[4, 3, 1, 6]`  
**Output:** `true`  
**Explanation:**  
- (4, 3) → even–odd
- (3, 1) → odd–odd (both odd, violates the condition)
The array is not special.

### Example 4
**Input:**  
`[1, 2, 3, 4]`  
**Output:** `true`  
**Explanation:**  
- (1, 2) → odd–even
- (2, 3) → even–odd
- (3, 4) → odd–even
All adjacent pairs have opposite parity.

---

## 🧠 Approach
1. **Iterate through the array**: Check each pair of adjacent elements
2. **Check parity**: For each pair, verify that one element is even and the other is odd
3. **Early termination**: If any adjacent pair has the same parity, return `false` immediately
4. **Return result**: If all pairs pass the check, return `true`

### Solution Code (JavaScript)
```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isArraySpecial = function(nums) {
    for (let i = 1; i < nums.length; i++) {
        // Check if current and previous elements have the same parity
        if (nums[i] % 2 === nums[i - 1] % 2) {
            return false;
        }
    }
    return true;
};
```

### Solution Code (TypeScript)
```typescript
function isArraySpecial(nums: number[]): boolean {
    for (let i = 1; i < nums.length; i++) {
        if ((nums[i] % 2) === (nums[i - 1] % 2)) {
            return false;
        }
    }
    return true;
};
```

### Solution Code (Python)
```python
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i] % 2) == (nums[i-1] % 2):
                return False
        return True
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(n)`  
  - We iterate through the array once, checking each adjacent pair
  - The modulo operation is O(1) for each element
  
- **Space Complexity**: `O(1)`  
  - We only use a constant amount of extra space
  - No additional data structures are used that grow with input size

---

## 📝 Notes
- The solution efficiently checks for the special array property in a single pass
- The modulo operation (`% 2`) is used to determine if a number is even or odd
- The function returns early as soon as it finds any adjacent pair with the same parity
- The solution handles edge cases like single-element arrays correctly

## 🔗 Related Problems
- [Special Array II](https://leetcode.com/problems/special-array-ii/)
- [Array With Elements Not Equal to Average of Neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/)
- [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/)

## 📚 Additional Resources
- [LeetCode: Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)
- [GeeksforGeeks: Check if all elements in an array are same](https://www.geeksforgeeks.org/check-if-all-the-elements-can-be-made-equal-by-dividing-elements-with-2-and-3/)
- [Wikipedia: Parity (mathematics)](https://en.wikipedia.org/wiki/Parity_(mathematics))

### Example 3

**Input:**  
`nums = [4, 3, 1, 6]`  
**Output:**  
`false`

**Explanation:**  
Adjacent elements at positions 1 and 2 → (3, 1) are both odd ✘  
This breaks the alternating-parity requirement.

---

## 🔒 Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- All values are positive integers

---

## 🧠 Conceptual Approach

- Iterate through the array from index 1 onward.
- For each adjacent pair `(nums[i-1], nums[i])`, evaluate parity using modulo-based classification.
- If any pair shares the same parity (both odd or both even), classification fails immediately.
- If no violations occur across the full scan, the array is considered special.

---

## 🚀 Output Behavior

The function delivers a boolean response confirming whether the input array adheres to strict alternating-parity integrity across all adjacent indices.

---

## 📄 License

MIT License.
