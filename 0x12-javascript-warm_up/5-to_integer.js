#!/usr/bin/node
const mynum = Number.parseInt(process.argv[2]);
if (!isNaN(mynum)) {
  console.log('My number: ' + mynum);
} else {
  console.log('Not a number');
}
