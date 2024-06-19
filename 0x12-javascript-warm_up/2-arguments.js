#!/usr/bin/node
/*
 * prints a message depending on the number of arguments passed
 */

const argsNo = process.argv;

// checks for arguments and print message if found
if (argsNo.length === 2) {
  console.log('No argument');
} else if (argsNo.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
