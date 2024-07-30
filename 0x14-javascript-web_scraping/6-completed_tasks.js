#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const dict = {};

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    process.exit(1); // Exit with an error code if there's an error
  }
  const result = JSON.parse(body);
  for (const i of result) {
    if (i.completed) {
      if (dict[i.userId]) {
        dict[i.userId]++;
      } else {
        dict[i.userId] = 1;
      }
    }
  }
  console.log(dict);
});
