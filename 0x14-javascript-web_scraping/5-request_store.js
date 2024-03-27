#!/usr/bin/node
// scripts that gets the content of a webpage and stores it in a file

// import request module using require
const request = require('request');

// import file ssytem modulue
const fs = require('fs');

// get url from the command line argument
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const content = JSON.stringify(body);
  // Where to write the file
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err.message);
    }
  });
});
