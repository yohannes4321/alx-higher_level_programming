#!/usr/bin/node

const argvm = process.argv[2];
if (argvm === undefined) {
  console.log('No argument');
} else {
  console.log(argvm);
}
