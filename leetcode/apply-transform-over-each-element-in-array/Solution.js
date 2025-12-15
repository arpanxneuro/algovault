/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  let myArr = [];
  for (let i = 0; i < arr.length; i++) {
    myArr.push(fn(arr[i], i));
  }
  return myArr;
};
