#!/bin/bash
# sends a get request and display the body of the respons if 200 status

curl -sL "$1" -o /dev/null -w "%{http_code}" | grep -q "200" && curl -sL "$1"
