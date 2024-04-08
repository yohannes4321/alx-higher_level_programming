#!/usr/bin/node

const k = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);

if (!isNaN(k) && !isNaN(y)) {
  function add(k, y) {
    const result = k + y;
    console.log(result);
  }

  add(k, y); // Call the add function with provided arguments
} else {
  console.log('NaN');
}
