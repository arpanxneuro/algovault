function isValid(s: string): boolean {
  const stack: string[] = [];
  const mapping: { [key: string]: string } = {
    ")": "(",
    "}": "{",
    "]": "[",
  };
  for (const char of s) {
    if (char == "(" || char == "{" || char == "[") {
      stack.push(char);
    } else {
      if (stack.length === 0 || stack[stack.length - 1] !== mapping[char]) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}
