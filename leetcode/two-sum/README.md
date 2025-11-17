# Two Sum

**Platform:** [LeetCode](https://leetcode.com/problems/two-sum/)  
**Category:** Array / Hash Table  
**Difficulty:** Easy  
**Problem Statement:** Given an array of integers `nums` and an integer `target`, return *indices* of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

---

## 📘 Problem Overview
Given an array of integers `nums` and a target value, we need to find two numbers in the array that add up to the target and return their indices. The solution must be efficient and handle various edge cases, including negative numbers and large input sizes.

### Key Points:
- Each input has exactly one solution
- You cannot use the same element twice
- The array can contain negative numbers and zeros
- The solution should be efficient with time complexity O(n)

---

## 📥 Input Format
- `nums`: An array of integers (2 ≤ nums.length ≤ 10⁴)
  - Each element nums[i] is an integer (-10⁹ ≤ nums[i] ≤ 10⁹)
- `target`: An integer (-10⁹ ≤ target ≤ 10⁹)

## 📤 Output Format
- Return an array `[i, j]` where `nums[i] + nums[j] == target`
- The order of the indices in the result does not matter
- The solution is guaranteed to exist and be unique

## 🔍 Constraints
- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Only one valid answer exists

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`nums = [2, 7, 11, 15]`  
`target = 9`  
**Output:** `[0, 1]`  
**Explanation:**  
`nums[0] + nums[1] = 2 + 7 = 9`

### Example 2
**Input:**  
`nums = [3, 2, 4]`  
`target = 6`  
**Output:** `[1, 2]`  
**Explanation:**  
`nums[1] + nums[2] = 2 + 4 = 6`

### Example 3
**Input:**  
`nums = [3, 3]`  
`target = 6`  
**Output:** `[0, 1]`  
**Explanation:**  
`nums[0] + nums[1] = 3 + 3 = 6`

### Example 4
**Input:**  
`nums = [-1, -2, -3, -4, -5]`  
`target = -8`  
**Output:** `[2, 4]`  
**Explanation:**  
`nums[2] + nums[4] = -3 + (-5) = -8`

---

## 🧠 Approach
1. **Hash Map (Optimal Solution)**
   - Use a hash map to store the difference between the target and the current element (complement) as the key and the current index as the value
   - For each element, check if its complement exists in the hash map
   - If found, return the indices of the current element and its complement
   - If not found, add the current element and its index to the hash map

2. **Brute Force (For Comparison)**
   - Use two nested loops to check every possible pair of elements
   - Return the indices of the first pair that sums to the target
   - Time Complexity: O(n²)
   - Space Complexity: O(1)

### Solution Code (Python)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  # This line is theoretically unreachable due to the problem's constraints
```

### Solution Code (TypeScript)
```typescript
function twoSum(nums: number[], target: number): number[] {
    const numIndices = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (numIndices.has(complement)) {
            return [numIndices.get(complement)!, i];
        }
        numIndices.set(nums[i], i);
    }
    return []; // This line is theoretically unreachable due to the problem's constraints
}
```

### Solution Code (JavaScript)
```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return [];
};
```

### Solution Code (Java)
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }
}
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(n)`  
  - We traverse the list containing `n` elements only once. Each lookup in the hash table costs only O(1) time.
  
- **Space Complexity**: `O(n)`  
  - The extra space required depends on the number of items stored in the hash table, which stores at most `n` elements.

---

## 📝 Notes
- The hash table reduces the lookup time from O(n) to O(1) by trading space for speed
- The solution handles all edge cases, including negative numbers and zeros
- The algorithm is optimal as it only requires a single pass through the array
- The problem guarantees exactly one solution, so we don't need to handle multiple solutions

## 🔗 Related Problems
- [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [3Sum](https://leetcode.com/problems/3sum/)
- [4Sum](https://leetcode.com/problems/4sum/)
- [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
- [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/)

## 📚 Additional Resources
- [LeetCode: Two Sum Solution Article](https://leetcode.com/problems/two-sum/solution/)
- [GeeksforGeeks: Two Sum Problem](https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/)
- [NeetCode: Two Sum Video Explanation](https://www.youtube.com/watch?v=KLlXCFG5TnA)
