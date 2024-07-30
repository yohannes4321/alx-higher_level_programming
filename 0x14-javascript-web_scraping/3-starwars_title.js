#!/usr/bin/node

const value1 = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
const urlFinal = url + value1;

request(urlFinal, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
