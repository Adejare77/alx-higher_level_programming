#!/usr/bin/node
if (process.argv.length === 2 || isNaN(process.argv[2])) {
    console.log('Missing size');
} else {
    let i = 0;
    const myVar = Number(process.argv[2])
    for (; i < myVar; i++) {
        console.log('X'.repeat(myVar));
    }
}
