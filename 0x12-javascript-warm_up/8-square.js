#!/usr/bin/node
const xTime = process.argv[2];

for (let i = 0; i < xTime; i++) {
  let output = '';
  for (let i = 0; i < xTime; i++) {
    output += 'x';
  }
  console.log(output);
}
