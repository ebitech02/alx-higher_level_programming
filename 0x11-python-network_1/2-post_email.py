#!/usr/bin/python3
# a python script that handles a post request
import urllib.request
import urllib.parse
import parse
""""
using the urllib handles url and the post request
and also the sys argument
"""
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
