#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);

const custom_list = list.map((x) => x * (x - 1));
console.log(custom_list);
