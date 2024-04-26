#!/usr/bin/python3
"""  sends a  """
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response_ = requests.get(url)
    if response_.status_code >= 400:
        print("Error code: {}".format(response_.status_code))
    else:
        print(response_.text)
