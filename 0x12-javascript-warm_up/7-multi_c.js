#!/usr/bin/node

let xTime = process.argv[2];

if (xTime > 0) {
  while (xTime > 0) {
    console.log('C is fun');
    xTime--;
  }
} else {
  console.log('Missing number of occurrences');
}
