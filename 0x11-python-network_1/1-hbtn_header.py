#!/usr/bin/python3
# a python script that takes in a url, sends request
# to that url and displays the response
import urllib.request
import sys
"""
using the package url that handles url (https)
and sys arguments
"""
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
