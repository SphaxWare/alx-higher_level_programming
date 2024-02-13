#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number === 0) {
      return 0;
    } else {
      const remainder = number % base;
      const quotient = Math.floor(number / base);

      if (quotient === 0) {
        return remainder.toString(base);
      } else {
        return exports.converter(base)(quotient) + remainder.toString(base);
      }
    }
  };
};
