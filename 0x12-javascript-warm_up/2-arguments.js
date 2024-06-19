#!/usr/bin/node
/*
 * prints a message depending on the number of arguments passed
 */

const argsNo = process.argv.slice(2);

if (argsNo.length === 0) {
  console.log('No argument');
} else if (argsNo.length === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
