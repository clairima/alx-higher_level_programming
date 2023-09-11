#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const parsedInt = parseInt(firstArg);

if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
