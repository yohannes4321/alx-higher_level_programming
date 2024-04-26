#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the response header"""
import requests
import sys

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    value = response.headers.get('X-Request-Id')
    print(value)
