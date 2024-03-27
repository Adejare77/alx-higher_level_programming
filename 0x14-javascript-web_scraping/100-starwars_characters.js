#!/usr/bin/node
// Scripts that prints all characters of a Star Wars movie

// import the request module using 'require'
const request = require('request');

// get the movie id from the command line argument
const movieId = process.argv[2];

// use this url
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// start to query. followRedirect is not needed. Just for future ref
request({ url, followRedirect: true }, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const parsedResponseCharacters = JSON.parse(body).characters;

  for (const characterUrl of parsedResponseCharacters) {
    request(characterUrl, (err, response, Name) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterName = JSON.parse(Name).name;
      console.log(characterName);
    });
  }
});
