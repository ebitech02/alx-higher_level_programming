#!/usr/bin/node

const args = process.argv[2];
const fs = require('fs');

fs.readFile(args, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
