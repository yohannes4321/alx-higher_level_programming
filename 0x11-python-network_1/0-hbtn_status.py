#!/usr/bin/python3
"""url """
import urllib.request


if __name__ == '__main__':
    url_data = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url_data) as response:
        data_value = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data_value)))
        print('\t- content: {}'.format(data_value))
        print('\t- utf8 content: {}'.format(data_value.decode('utf-8')))
