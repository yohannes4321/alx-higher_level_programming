#!/usr/bin/node
// Use strict mode to enforce cleaner code
'use strict';

// Count the number of command-line arguments
const argvcount = process.argv.length;

// Check the number of arguments and print a message accordingly
if (argvcount === 2) {
  console.log('No argument');
} else if (argvcount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
