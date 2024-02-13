#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv[3] === undefined) {
  console.log(process.argv[2]);
}
