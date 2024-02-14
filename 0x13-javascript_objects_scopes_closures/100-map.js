#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);

let previousValue = 0;
const customList = list.map((currentValue) => {
  const result = previousValue * currentValue;
  previousValue = currentValue;
  return result;
});
console.log(customList);
