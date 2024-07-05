#!/bin/bash
# outputs the byte count

curl -sI "$1" | grep 'Content-length:' | cut -d' ' -f2
