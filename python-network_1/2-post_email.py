#!/usr/bin/env python3
"""URL-ə email parametrilə POST sorğusu göndərən və cavabı çap edən modul."""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
