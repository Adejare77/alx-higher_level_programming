#!/usr/bin/node
// script that display the status code of a GET request

// import the 'request' module using require
const request = require('request');

// get the url from the command line argument
const url = process.argv[2];

// provide the url to rhe request module

request(url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(response.statusCode);
});
