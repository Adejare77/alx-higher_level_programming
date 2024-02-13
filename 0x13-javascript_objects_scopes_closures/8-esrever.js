#!/usr/bin/node

exports.esrever = function (list) {
  let myLen = list.length - 1;
  for (let i = 0; i < myLen; i++) {
    const myTemp = list[myLen];
    list[myLen] = list[i];
    list[i] = myTemp;
    myLen--;
  }
  return list;
};
