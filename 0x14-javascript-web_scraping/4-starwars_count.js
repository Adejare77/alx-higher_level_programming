#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode
// number matches a given integer

// import the 'request' module using require
const request = require('request');

// get the url from the command line argument
const url = process.argv[2];

// provide the url to rhe request module

request(url, (err, response, data) => {
  if (err) {
    console.error(err);
    return;
  }

  let count = 0;

  (function WedgeAntilles () {
    // where results is a key containing array of objects

    const parsedResponseResults = JSON.parse(data).results;
    for (const movie of parsedResponseResults) {
      const characters = movie.characters;
      // where characters is also an array of character urls
      characters.map(character => {
        const urlID = character.match(/18\/$/);
        if (urlID) {
          count++;
        }
        return undefined;
      });
    }
    console.log(count);
  })();
});
