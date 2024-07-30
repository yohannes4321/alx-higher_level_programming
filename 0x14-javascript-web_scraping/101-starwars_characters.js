#!/usr/bin/node

const request = require('request');

// Construct the URL for the given movie ID
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

// Fetch the movie data
request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});

// Recursively fetch and print character names
function printCharacters (characters, index) {
  if (index >= characters.length) return; // Base case to stop recursion

  request(characters[index], function (error, response, body) {
    if (error) {
      console.error('Error:', error);
      return;
    }

    try {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(characters, index + 1); // Recursive call for the next character
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  });
}
