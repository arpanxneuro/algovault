# Roman to Integer

**Platform:** [LeetCode](https://leetcode.com/problems/roman-to-integer/)  
**Category:** String / Hash Table / Math  
**Difficulty:** Easy  
**Problem Statement:** Given a Roman numeral, convert it to an integer.

---

## 📘 Problem Overview
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written largest to smallest from left to right. However, there are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

### Key Points:
- Input is guaranteed to be within the range from 1 to 3999
- The input string contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
- The length of the string is between 1 and 15
- The solution should be efficient with time complexity O(n) and space complexity O(1)

---

## 📥 Input Format
- `s`: A string representing a valid Roman numeral (1 ≤ s.length ≤ 15)
  - Contains only the characters 'I', 'V', 'X', 'L', 'C', 'D', 'M'
  - It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999]

## 📤 Output Format
- Returns an integer representing the converted value of the Roman numeral

## 🔍 Constraints
- `1 <= s.length <= 15`
- `s` contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
- It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999]

---

## 🧪 Sample Cases

### Example 1
**Input:**  
`"III"`  
**Output:** `3`  
**Explanation:**  
III = 3

### Example 2
**Input:**  
`"LVIII"`  
**Output:** `58`  
**Explanation:**  
L = 50, V = 5, III = 3

### Example 3
**Input:**  
`"MCMXCIV"`  
**Output:** `1994`  
**Explanation:**  
M = 1000, CM = 900, XC = 90, IV = 4

### Example 4
**Input:**  
`"IX"`  
**Output:** `9`  
**Explanation:**  
I before X means subtract 1 from 10

### Example 5
**Input:**  
`"MCMXCVII"`  
**Output:** `1997`  
**Explanation:**  
M = 1000, CM = 900, XC = 90, V = 5, II = 2

---

## 🧠 Approach
1. **Create a Mapping**: Map each Roman numeral to its integer value
2. **Initialize Total**: Start with a total of 0
3. **Iterate Through the String**:
   - For each character, get its value
   - If the current value is less than the next value, subtract it from the total (handles cases like IV, IX, etc.)
   - Otherwise, add it to the total
4. **Return the Result**: The accumulated total is the converted integer

### Solution Code (Python)
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If current value is less than next value, subtract it
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
                
        return total
```

### Solution Code (TypeScript)
```typescript
function romanToInt(s: string): number {
    const romanMap: { [key: string]: number } = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    
    let total = 0;
    
    for (let i = 0; i < s.length; i++) {
        const current = romanMap[s[i]];
        const next = romanMap[s[i + 1]] || 0;
        
        if (current < next) {
            total -= current;
        } else {
            total += current;
        }
    }
    
    return total;
}
```

---

## 📊 Complexity Analysis
- **Time Complexity**: `O(n)`  
  - We traverse the string once from left to right
  - Each character is processed exactly once
  
- **Space Complexity**: `O(1)`  
  - We use a fixed-size dictionary (7 entries) for the Roman numeral mappings
  - Only a constant amount of additional space is used

---

## 📝 Notes
- The solution efficiently handles all valid Roman numeral combinations
- The algorithm processes each character exactly once, making it optimal
- The solution handles all edge cases, including the largest valid Roman numeral (MMMCMXCIX = 3999)
- The code is clean, readable, and easy to understand

## 🔗 Related Problems
- [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
- [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)
- [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

## 📚 Additional Resources
- [LeetCode Article: Roman to Integer](https://leetcode.com/articles/roman-to-integer/)
- [GeeksforGeeks: Converting Roman Numerals to Decimal](https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/)
- [Wikipedia: Roman Numerals](https://en.wikipedia.org/wiki/Roman_numerals)
