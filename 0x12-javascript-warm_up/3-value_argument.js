#!/usr/bin/node
//  this prints the first argment passed to it

if (process.argv[2] === undefind) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
