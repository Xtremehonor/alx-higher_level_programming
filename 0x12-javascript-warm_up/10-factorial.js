#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) { // Check if n is NaN
    return 1;
  }
  if (n <= 1) { // Base case: factorial of 0 or 1 is 1
    return 1;
  } else {
    return n * factorial(n - 1); // Recursive call to factorial function
  }
}

const num = parseInt(process.argv[2]); // Convert argument to integer

console.log(factorial(num)); // Print the result
