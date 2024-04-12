#!/usr/bin/node
//  this prints the first argment passed to it

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
