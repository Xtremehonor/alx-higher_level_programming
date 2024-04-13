#!/usr/bin/node
const xTime = process.argv[2];

if (xTime > 0) {
    for (let i = 0; i < xTime; i++) {
        let output = '';
        for (let i = 0; i < xTime; i++) {
            output += 'x';
        }
        console.log(output);
    }
} else {
    console.log('Missing size');
}
