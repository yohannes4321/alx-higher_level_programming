#!/usr/bin/node

const b = parseInt(process.argv[2]);

if (!isNaN(b)) {
  console.log(`My number: ${b}`);
} else {
  console.log('Not a number');
}
