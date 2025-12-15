
**Output:**  
[5, 1, 2, 3, 4]

**Input:**  
arr = [2, 3, 4, 5, 1]

**Output:**  
[1, 2, 3, 4, 5]

---

## 🛠️ Approach

One efficient in-place approach (O(n) time, O(1) space):  
- Store the last element (`last = arr[n-1]`) in a temporary variable. :contentReference[oaicite:4]{index=4}  
- Shift every element from index `n-2` down to `0` one step to the right (`arr[i+1] = arr[i]`). :contentReference[oaicite:5]{index=5}  
- Assign `arr[0] = last`. :contentReference[oaicite:6]{index=6}  

This achieves the clockwise rotation by one, with:  
- **Time Complexity**: O(n) :contentReference[oaicite:7]{index=7}  
- **Space Complexity**: O(1) :contentReference[oaicite:8]{index=8}

---

## 📌 Notes

- Works for any integer array, including negative, positive, or zero values.  
- Supports arrays of arbitrary size `n ≥ 1`.  
