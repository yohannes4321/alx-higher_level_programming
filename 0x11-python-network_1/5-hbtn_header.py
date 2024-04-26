#!/usr/bin/python3
"""Th ader"""
import requests
import sys

if __name__ == '__main__':
    response_method= requests.get(sys.argv[1])
    finale_value = response_method.headers.get('X-Request-Id')
    print(finale_value)
