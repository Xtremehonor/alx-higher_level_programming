#!/usr/bin/node
const myNumber = process.argv[2];

if (isNaN(myNumber)) {
    console.log('Not a number');
} else {
    console.log('My number: ' + parseInt(myNumber));
}
