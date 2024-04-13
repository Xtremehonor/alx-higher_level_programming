#!/usr/bin/node

const xTime = process.argv[2];

if (xTime > 0) {
  for (i = 0; i <= xTime; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
