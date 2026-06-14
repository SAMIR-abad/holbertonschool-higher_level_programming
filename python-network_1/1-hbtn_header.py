#!/usr/bin/python3
"""Fetches the X-Request-Id header from a given URL"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.headers.get("X-Request-Id"))
