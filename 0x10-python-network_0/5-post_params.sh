#!/bin/bash
# takes in a URL, sends a post request to that URL and displays response
curl -s -X POST -d "test@gmail.com" -d "I will always be here for PLD" "$1"
