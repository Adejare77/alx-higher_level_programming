#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode
// number matches a given integer

// import the 'request' module using require
const request = require('request');

// get the url from the command line argument
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

// provide the url to rhe request module

request(url, (err, response, data) => {
  if (err) {
    console.error(err);
    return;
  }
  // print reponse body
  const parsedResponse = JSON.parse(data);
  console.log(`${parsedResponse.title}`);
});
