#!/usr/bin/python3
"""Hərflə istifadəçi axtaran və JSON cavabını emal edən modul."""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    try:
        response = requests.post(url, data=payload)
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
