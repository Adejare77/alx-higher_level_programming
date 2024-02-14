#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    let myLen = this.height;
    let myVar = c;
    if (c === undefined) {
      myVar = 'X';
    }
    while (myLen > 0) {
      console.log(myVar.repeat(this.width));
      myLen--;
    }
  }
}

module.exports = Square;
