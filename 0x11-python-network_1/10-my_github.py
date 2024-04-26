#!/usr/bin/python3
"""This script takes my github credentials(username and
password) and uses the GitHub API to display my id.
It uses Basic Authentication with personal access token
as password. The first argument is my username and the second
argument will be my personal access token as password"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    usernameee = argv[1]
    passworddd = argv[2]
    responseee= requests.get(url, auth=(usernameee, passworddd))
    try:
        print(responseee.json()['id'])
    except KeyError:
        print("None")
