#!/usr/bin/python3
"""Module for save_to_json_file function."""
import json
"""ssss"""

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        """aaaaa"""
        json.dump(my_obj, f)
