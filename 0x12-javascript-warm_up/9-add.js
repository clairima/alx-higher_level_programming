#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const args = process.argv.slice(2);
const argv1 = args[0];
const argv2 = args[1];
const num1 = parseInt(argv1);
const num2 = parseInt(argv2);

if (!isNaN(num1) && !isNaN(num2)) {
  const result = add(num1, num2);
  console.log(result);
} else {
  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
  }
}
