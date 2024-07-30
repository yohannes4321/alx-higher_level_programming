#!/usr/bin/node

// Import the 'fs' module
const fs = require('fs');

// Get the filename from the command-line arguments
const value = process.argv[2];

// Read the file asynchronously
fs.readFile(value, 'utf8', (err, data) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  console.log(data);
});
