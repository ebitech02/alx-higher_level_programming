#!/bin/bash
# outputs the byte count
curl -s "$1" | wc -c
