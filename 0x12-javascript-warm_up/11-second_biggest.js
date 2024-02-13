#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.map(Number).sort((a, b) => b - a);
  const secondLargest = sortedArgs[1];
  console.log(secondLargest);
}
