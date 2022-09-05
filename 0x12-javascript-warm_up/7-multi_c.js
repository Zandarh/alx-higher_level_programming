#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const myVar = process.argv[2];
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
