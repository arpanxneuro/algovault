
**Output:**  
[5, 1, 2, 3, 4]

**Input:**  
arr = [2, 3, 4, 5, 1]

**Output:**  
[1, 2, 3, 4, 5]

---

## 🛠️ Approach

One efficient in-place approach (O(n) time, O(1) space):  
- Store the last element (`last = arr[n-1]`) in a temporary variable.  
- Shift every element from index `n-2` down to `0` one step to the right (`arr[i+1] = arr[i]`).  
- Assign `arr[0] = last`.  

This achieves the clockwise rotation by one, with:  
- **Time Complexity**: O(n)  
- **Space Complexity**: O(1)

---

## 📌 Notes

- Works for any integer array, including negative, positive, or zero values.  
- Supports arrays of arbitrary size `n ≥ 1`.  
