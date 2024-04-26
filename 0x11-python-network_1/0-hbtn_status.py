#!/usr/bin/python3
"""Fetch url usaing urllib"""
from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        type = response.getheader("Content-Type")
        content = response.read()
        utf8 = content.decode("utf-8")
        print("Body response:")
        print("\t- type: " + type)
        print("\t- content: " + content)
        print("\t- utf content: " + utf8)

