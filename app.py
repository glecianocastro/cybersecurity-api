from flask import Flask
import random
import string
import hashlib
import socket
import re

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "Cybersecurity API",
        "version": "1.3",
        "status": "online"
    }
@app.route("/password")
def password():

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    generated = "".join(
        random.choice(characters)
        for _ in range(16)
    )

    return {
        "password": generated
    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "api": "running"
    }

@app.route("/hash/<text>")
def generate_hash(text):

    sha256_hash = hashlib.sha256(
        text.encode()
    ).hexdigest()

    return {
        "text": text,
        "sha256": sha256_hash
    }

@app.route("/dns/<host>")
def dns_lookup(host):
    
    try:
        ip = socket.gethostbyname(host)

        return {
            "host": host,
            "ip": ip
        }
    except Exception:
        return {
            "error": "Host not found"
        }

@app.route("/password-strength/<password>")
def password_strength(password):
    
    score = 0

    if len(password) >= 8:
        score += 1
    
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "password": password,
        "strength": strength,
        "score": score
    }
if __name__ == "__main__":
    app.run(debug=True)