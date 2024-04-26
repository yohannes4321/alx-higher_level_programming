#!/usr/bin/python3
from urllib import request

url = "https://alx-intranet.hbtn.io/status"
with request.urlopen(url) as response:
    type = response.getheader("Content-Type")
    content = response.read()
    utf8 = content.decode("utf-8")
    print("Body response:")
    print("\t- type: " + type)
    print("\t- content: " + content)
    print("\t- utf content: " + utf8)

