#!/usr/bin/node
// script that writes a string to a file

// import file system to write to a file using require
const fs = require('fs');

// provide the file path from the command line arg
const filePath = process.argv[2];
const content = process.argv[3];

// write string content into the file using utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err.message);
  }
});
