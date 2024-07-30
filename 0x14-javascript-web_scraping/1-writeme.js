#!/usr/bin/node

// Import the 'fs' module
const fs = require('fs');

// Get the filename and content from the command-line arguments
const filename = process.argv[2];
const content = process.argv[3];

// Write the content to the specified file
fs.writeFile(filename, content, 'utf8', (err, data) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  console.log(data);
});
