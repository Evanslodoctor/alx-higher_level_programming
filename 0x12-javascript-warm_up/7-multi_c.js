#!/usr/bin/node
const op = process.argv[2];
if (isNaN(op) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < op; i++) {
    console.log('C is fun');
  }
}
