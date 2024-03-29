#!/usr/bin/node
// Scripts that computes the number of tasks completed by user id

// import request module using require
const request = require('request');

// get the url argument from command line
const url = process.argv[2];

request({ url, followAllRedirects: true }, (err, resp, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const parsedResponse = JSON.parse(data);

  const objects = {};

  for (const obj of parsedResponse) {
    if (obj.userId in objects) {
      if (obj.completed) {
        objects[obj.userId] += 1;
      }
    } else {
      objects[obj.userId] = 0;
      if (obj.completed) {
        objects[obj.userId] += 1;
      }
    }
  }
  console.log(objects);
});
