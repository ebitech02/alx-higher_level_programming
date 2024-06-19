#!/usr/bin/node
/*
 * prints two arguments passed to it in is format
 */

const argsNo = process.argv;

if (argsNo[2] !== undefined && argsNo[3] !== undefined) {
  console.log(`${argsNo[2]} is ${argsNo[3]}`);
} else {
  console.log(`${argsNo[2]} is undefined`);
}
