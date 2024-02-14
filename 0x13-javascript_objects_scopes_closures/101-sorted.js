#!/usr/bin/node

const dict = require('./101-data').dict;

const myDict = {};
Object.entries(dict).forEach(([key, value]) => {
  if (value in myDict) {
    myDict[value].push(key);
  } else {
    myDict[value] = [key];
  }
});
console.log(myDict);
