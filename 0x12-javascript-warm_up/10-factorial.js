#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  } else if (Number(a) === 1) {
    return (-1);
  }
  factorial(a * factorial(a - 1));
}
console.log(factorial(Number(process.argv[2])));
