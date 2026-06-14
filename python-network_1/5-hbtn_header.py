#!/usr/bin/python3
"""URL-ə sorğu göndərən və header-dən X-Request-Id dəyərini çıxaran modul."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
