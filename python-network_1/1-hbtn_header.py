#!/usr/bin/python3
"""URL-ə sorğu göndərən və X-Request-Id başlıq dəyərini çap edən modul."""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
