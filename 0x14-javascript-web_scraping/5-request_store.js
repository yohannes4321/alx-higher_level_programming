#!/usr/bin/node
// This script takes a URL to request and a file path
// and gets the contents of the page and stores it in a file.
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
