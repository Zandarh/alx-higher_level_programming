#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const myVar = process.argv[2];
  for (let i = 0; i < myVar; i++) {
    console.log('X'.repeat(myVar));
  }
}
