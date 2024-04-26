#!/usr/bin/python3
"""This script sends a POST request to the URL"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data_value = {'email': email}
    data_value = urllib.parse.urlencode(data_value)
    data = data_value.encode('ascii')
    req = urllib.request.Request(url, data_value)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
