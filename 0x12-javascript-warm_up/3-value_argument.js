#!/usr/bin/node
/*
 * prints the first argument passed to it
 */

const argsNo = process.argv;

if (!argsNo[2]) {
  console.log('No argument');
} else {
  console.log(argsNo[2]);
}
