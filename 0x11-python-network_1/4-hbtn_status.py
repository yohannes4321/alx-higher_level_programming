#!/usr/bin/python3
"""This script  /status'"""
import requests

if __name__ == "__main__":
    name = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(name.text)))
    print("\t- content: {}".format(name.text))
