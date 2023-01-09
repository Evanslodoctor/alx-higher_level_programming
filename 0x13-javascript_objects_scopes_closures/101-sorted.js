#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = Object.entries(dict).reduce((adict, [key, value]) => {
  adict[value] = adict[value] ? [...adict[value], key] : [key];
  return adict;
}, {});
console.log(newDict);
