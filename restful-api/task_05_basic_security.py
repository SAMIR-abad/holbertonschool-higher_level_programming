#!/usr/bin/python3
"""Basic Auth, JWT və Rol əsaslı təhlükəsizlik mexanizmləri modulu."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün istifadəçi adı və şifrəni təsdiqləyir."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None


@app.route("/login", methods=["POST"])
def login():
    """İstifadəçi məlumatlarını yoxlayır və JWT token yaradır."""
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401
    access_token = create_access_token(identity=user)
    return jsonify({"access_token": access_token}), 200


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Yalnız düzgün Basic Auth məlumatları ilə daxil oluna bilən marşrut."""
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Yalnız düzgün JWT token ilə daxil oluna bilən marşrut."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Yalnız rolu 'admin' olan istifadəçilər üçün nəzərdə tutulmuş marşrut."""
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Token göndərilmədikdə və ya tapılmadıqda 401 xətası qaytarır."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Tokenin strukturu xətalı olduqda 401 xətası qaytarır."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err, token_data):
    """Tokenin vaxtı bitdikdə 401 xətası qaytarır."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err, token_data):
    """Ləğv edilmiş tokenlər üçün 401 xətası qaytarır."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err, token_data):
    """Təzə token tələb olunduqda 401 xətası qaytarır."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
