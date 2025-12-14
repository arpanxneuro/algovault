function divideString(s: string, k: number, fill: string): string[] {
  let str: string;
  let myArr: string[] = [];
  let fillCount: number = 0;
  if (s.length % k !== 0) {
    fillCount = k - (s.length % k);
  }
  for (let i = 0; i < s.length; i += k) {
    str = s.slice(i, i + k);
    if (str.length < k) {
      str = str + fill.repeat(fillCount);
    }
    myArr.push(str);
  }

  return myArr;
}
