#!/bin/bash
# outputs the byte count

curl -s -w "%{size_download}\n" -o /dev/null "$1"
