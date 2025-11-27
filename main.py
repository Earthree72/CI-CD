# main.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    """
    Root endpoint to check API health.
    """
    return jsonify({"status": "ok", "version": "1.0.0"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """
    Simple logic function to test mathematics.
    """
    return jsonify({"result": a + b})

from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = "super-secret-key"   # Needed for session login

# Temporary database (in-memory)
users = {
    "admin": "password123"
}

@app.route("/")
def root():
    """
    Root endpoint to check API health.
    """
    return jsonify({"status": "ok", "version": "1.0.0"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """
    Simple logic function to test mathematics.
    """
    return jsonify({"result": a + b})

# -----------------------------
# ✅ LOGIN FUNCTION (temporary DB)
# -----------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Check against temporary database
    if username in users and users[username] == password:
        session["logged_in"] = True
        return jsonify({"message": "Login successful"})

    return jsonify({"error": "Invalid credentials"}), 401

# --------------------------------------------------------
# ✅ SUBTRACT FUNCTION — PROTECTED (only after login)
# --------------------------------------------------------
@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    if not session.get("logged_in"):
        return jsonify({"error": "Unauthorized — please log in first"}), 401

    return jsonify({"result": a - b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


