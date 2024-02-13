#!/usr/bin/node

exports.converter = function (base) {
  console.log(`The base passed is: ${base}`);
  return function (num) {
    console.log(`The num passed is: ${num}`);
    console.log(`The num.to.string(base) is: ${num.toString(base)}`);
    return num.toString(base);
  };
};
