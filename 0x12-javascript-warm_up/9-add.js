#!/usr/bin/node
function add(a, b) {
    if (process.argv.length < 4 || isNaN(a) || isNaN(b)) {
        console.log('NaN');
    } else {
        console.log(Number(a) + Number(b));
    }
};
add(process.argv[2], process.argv[3]);
