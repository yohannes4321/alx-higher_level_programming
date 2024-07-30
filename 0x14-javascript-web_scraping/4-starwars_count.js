#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    process.exit(1); // Exit with an error code if there's an error
  }
  const data = JSON.parse(body).results;
  let count = 0;
  for (const movie of data) {
    for (const character of movie.characters) {
      if (character.includes('18')) {
        count++;
        break; // Stop checking other characters in this movie
      }
    }
  }
  console.log(count);
});
