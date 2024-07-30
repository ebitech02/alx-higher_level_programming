#!/usr/bin/node

const args = process.argv[2];
const text = process.argv[3];
const fs = require('fs');

fs.writeFile(args, text, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
