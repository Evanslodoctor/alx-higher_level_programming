#!/usr/bin/node

exports.esrever = function (list) {
  return (list.map((item, index) => list[list.length - 1 - index]));
};
