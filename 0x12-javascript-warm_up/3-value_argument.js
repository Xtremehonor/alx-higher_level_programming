#!/usr/bin/node
//  this prints the first argment passed to it

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
