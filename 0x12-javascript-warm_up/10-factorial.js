#!/usr/bin/node
function factorial (a) {
    if (isNaN(a) || a === 0) {
        return (1);
    } else if (Number(a) === 1){
        return (-1);
    }
    factorial (x * factorial(x - 1));
}
console.log(factorial(Number(process.argv[2])));
