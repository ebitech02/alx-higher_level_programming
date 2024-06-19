#!/usr/bin/node
/*
 * prints the first argument passed to it
 */

const argsNo = process.argv;

if (argsNo[2] !== undefined) {
  console.log(argsNo[2]);
} else {
  console.log('No argument');
}
