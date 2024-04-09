#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let numbers = process.argv.slice(2).map(Number);
  let max = Math.max.apply(null, numbers);
  numbers = numbers.filter(num => num !== max);
  console.log(Math.max.apply(null, numbers));
}
