#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = this.height;
    while (i > 0) {
      console.log('X'.repeat(this.width));
      i--;
    }
  }

  rotate () {
    const myVar = this.height;
    this.height = this.width;
    this.width = myVar;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

module.exports = Rectangle;
