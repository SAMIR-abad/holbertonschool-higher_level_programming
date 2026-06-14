#!/usr/bin/python3
"""API-dən məlumat çəkən və CSV formatına salan modul."""
import csv
import requests


def fetch_and_print_posts():
    """Bütün postları çəkir, status kodunu və başlıqları çap edir."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Postları çəkir və onları posts.csv faylına yadda saxlayır."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                })
