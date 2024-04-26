#!/usr/bin/python3
"""This   request
to  """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    urll= "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    response = requests.post(urll, data)
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
