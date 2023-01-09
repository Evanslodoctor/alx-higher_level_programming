#!/usr/bin/node
exports.converter = function (base) {
  return function (arg) {
    return arg.toString(base);
  };
};
