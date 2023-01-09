#!/usr/bin/node
const op = process.argv[2];
let sp = '';
if (isNaN(op) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < op; i++) {
    sp += 'X';
  }
  for (let j = 0; j < op; j++) {
    console.log(sp);
  }
}
