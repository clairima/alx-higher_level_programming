#!/usr/bin/node
const size = process.argv[2];
const parsedSize = parseInt(size);

if (isNaN(parsedSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsedSize; i++) {
    console.log('X'.repeat(parsedSize));
  }
}
