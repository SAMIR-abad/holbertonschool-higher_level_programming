#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib"""
import urllib.request

url = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("    - type: {}".format(type(body).__name__))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(body.decode("utf-8")))
