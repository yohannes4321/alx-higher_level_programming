#!/usr/bin/node

const i = parseInt(process.argv[2]);
if (!isNaN(i)) {
  for (let j = 0; j < i; j++) {
    let row = '';
    for (let u = 0; u < i; u++) {
      row += ('x');
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
