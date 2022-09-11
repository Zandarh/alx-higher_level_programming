#!/usr/bin/node
// imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const values = Object.values(dict);
const uniqValues = [...new Set(values)];
const newDict = {};
for (const j in uniqValues) {
  const list = [];
  for (const key in totalList) {
    if (totalList[key][1] === uniqValues[j]) {
      list.unshift(totalList[key][0]);
    }
  }
  newDict[uniqValues[j]] = list;
}
console.log(newDict);
