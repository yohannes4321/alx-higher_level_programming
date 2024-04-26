#!/usr/bin/python3
# this is fitching from the website
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        valuef_from = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(valuef_from )))
        print('\t- content: {}'.format(valuef_from ))
        print('\t- utf8 content: {}'.format(valuef_from .decode('utf-8')))