#!/usr/bin/node
const x = Number.parseInt(process.argv[2]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let line = '';
    for (let j = 0; j < x; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
