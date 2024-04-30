#!/usr/bin/python3
"""This script sends a POST request to the URL"""
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try: 
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except:
        print("Error code:{}".format(urllib.error.HTTPError.code))
