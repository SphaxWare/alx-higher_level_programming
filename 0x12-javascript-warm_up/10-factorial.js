#!/usr/bin/node
function factor (a) {
  if ((isNaN(a)) || a === 0 || a === 1) {
    return (1);
  } else {
    return (a * factor(a - 1));
  }
}
console.log(factor(parseInt(process.argv[2])));
