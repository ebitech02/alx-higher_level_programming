#!/usr/bin/python3
# a python that fetches resources from a url

import urllib.request
"""
this package lets us handle urls (https)
"""
if __name__ == "__main__":
    url = "htpps://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
