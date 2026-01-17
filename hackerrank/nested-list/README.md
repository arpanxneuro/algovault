# nested list second lowest grade

> **Difficulty**: easy  
> **Platform**: HackerRank  
> **Tags**: array, sorting, list

---

## 📝 Problem Statement

Given the names and grades for each student in a class, store them in a nested list and determine the name(s) of the student(s) who have the **second lowest grade**.

If multiple students share the second lowest grade, their names must be printed in **alphabetical order**, each on a new line.

---

## 📥 Input

```
n
name_1
grade_1
name_2
grade_2
...
name_n
grade_n
```

---

## 📤 Output

- Print the name(s) of the student(s) having the second lowest grade.
- If multiple students exist, print each name on a new line in alphabetical order.

## ✔️ Constraints

- `n >= 2`
- Grades are real numbers
- There will always be at least one student with the second lowest grade

---

## ✅ Example

**Input**:

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

**Output**:

```
Berry
Harry
```

**Explanation**:

- The lowest grade is `37.2` (Tina).
- The second lowest grade is `37.21`, shared by Berry and Harry.
- Their names are sorted alphabetically and printed line by line.

---

## 🧪 Test Cases

| #   | Input                  | Output                      |
| --- | ---------------------- | --------------------------- |
| 1   | 5 students with grades | Names with 2nd lowest grade |
| 2   | Multiple ties          | Alphabetically sorted names |

---

## 🛠️ Approach

- Store student records as a nested list `[name, grade]`.
- Extract all unique grades and sort them.
- Identify the second lowest grade.
- Filter students matching that grade.
- Sort their names alphabetically and print each on a new line.

This approach ensures correctness while maintaining clarity and efficiency.

### Time and Space Complexity

- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
