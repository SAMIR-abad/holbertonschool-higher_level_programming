#!/usr/bin/python3
"""Flask framework-ü ilə RESTful API serveri quran modul."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Kök (root) endpoint üçün qarşılama mətni qaytarır."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Sistemdə qeydiyyatdan keçmiş bütün istifadəçi adlarının siyahısını qaytarır."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """API-ın aktivlik statusunu (OK) qaytarır."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Dinamik marşrutla ötürülən istifadəçinin bütün məlumatlarını qaytarır."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """POST sorğusu ilə gələn məlumatları yoxlayır və yeni istifadəçi əlavə edir."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
