from flask import Flask
import random
import string
import hashlib
import socket
import re
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "timestamp": datetime.now().isoformat(),
        "project": "Security Toolkit API",
        "version": "2.0",
        "status": "online",
        "endpoints": {
            "health": "/health",
            "password_generator": "/password",
            "hash_generator": "/hash/<text>",
            "dns_lookup": "/dns/<host>",
            "password_strength": "/password-strength/<password>",
            "port_scanner": "/scan/<host>"
        }
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
        "version": "2.0",
        "service": "Security Tollkit API"
    }

@app.route("/info")
def info():
    return {
        "author": "Gleciano Castro",
        "language": "Python",
        "framework": "Flask",
        "version": "2.0"
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

@app.route("/scan/<host>")
def port_scan(host):
    ports = [21, 22, 25, 53, 80, 110, 143, 443, 3389]
    open_ports = []
    try:

        ip = socket.gethostbyname(host)

        for port in ports:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
            sock.settimeout(2)
            result = sock.connect_ex(
                (ip, port)
            )
            if result == 0:
                open_ports.append(port)
            sock.close()
        return {
                "host": host,
                "ip": ip,
                "open_ports": open_ports
            }
    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    app.run(debug=True)