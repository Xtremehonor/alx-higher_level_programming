#!/usr/bin/node
const listOfNumbers = [0];

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < process.argv.length; i++) {
    if (!isNaN(parseInt(process.argv[i]))) {
      listOfNumbers.push(parseInt(process.argv[i]));
    }
  }

  listOfNumbers.sort(function (a, b) {
    return b - a;
  });

  console.log(listOfNumbers[1]);
} else {
  console.log(0);
}
