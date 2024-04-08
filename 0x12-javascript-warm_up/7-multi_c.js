#!/usr/bin/node

const k = parseInt(process.argv[2]);

if (!isNaN(k)) {
  for (let i = 0; i < k; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
