#!/usr/bin/node
let x = 0;

if (process.argv.length === 2 || isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
} else {
    while (x < process.argv[2]) {
        console.log('C is fun');
        x++;
    }
}
