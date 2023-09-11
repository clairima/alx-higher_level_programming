#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const integers = args.map(Number).filter(Number.isInteger);
  if (integers.length < 2) {
    console.log(0);
  } else {
    const sortedIntegers = integers.sort((a, b) => b - a);
    console.log(sortedIntegers[1]);
  }
}
