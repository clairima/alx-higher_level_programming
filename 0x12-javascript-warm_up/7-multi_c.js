#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const parsedInt = parseInt(firstArg);

if (isNaN(parsedInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < parsedInt; x++) {
    console.log('C is fun');
  }
}
