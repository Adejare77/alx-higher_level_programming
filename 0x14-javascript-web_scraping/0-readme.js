#!/usr/bin/node
// Script that reads and prints the content of a file

// import the file system module (fs) using require
const fs = require('fs');

// get the name of the file from cmd line arg using process.argv
const filePath = process.argv[2];

// read from the filePath using the method readFile and print
// error if it occurred during the reading
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(`{ Error: ${err.message}
      at Error (native)
    errno: ${err.errno},
    code: '${err.code}',
    syscall: '${err.syscall}',
    path: '${err.path}' }`);
    return;
  }

  console.log(data);
});
