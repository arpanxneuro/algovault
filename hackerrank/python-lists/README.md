# python list commands

> **Difficulty**: easy  
> **Platform**: HackerRank  
> **Tags**: list, simulation, command-processing

---

## 📝 Problem Statement

You are given an empty list. A sequence of commands is provided, each instructing a specific operation to be performed on the list. These operations include inserting, deleting, appending, sorting, reversing elements, and printing the list.

You must process each command in the order given and apply the corresponding operation on the list.

---

## 📥 Input

```
n
command_1
command_2
...
command_n
```

---

## 📤 Output

- For each `print` command, output the current state of the list on a new line.

## ✔️ Constraints

- All inserted elements are integers
- `1 <= n <= 1000`
- Commands will be valid and follow the defined syntax

---

## ✅ Example

**Input**:

```
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

**Output**:

```
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

**Explanation**:

- Commands are executed sequentially on an initially empty list.
- Whenever the `print` command is encountered, the current list state is displayed.
- Sorting and reversing operations modify the list in place.

---

## 🧪 Test Cases

| #   | Input          | Output         |
| --- | -------------- | -------------- |
| 1   | insert + print | updated list   |
| 2   | sort + reverse | reordered list |
| 3   | pop + print    | final list     |

---

## 🛠️ Approach

- Initialize an empty list.
- Read the total number of commands.
- Parse each command and invoke the corresponding list operation.
- Handle commands with arguments (`insert`, `append`, `remove`) appropriately.
- Print the list whenever a `print` command is encountered.

This command-driven simulation approach ensures deterministic behavior and mirrors real-world interpreter-style execution.

### Time and Space Complexity

- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
