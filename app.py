from flask import Flask
import random
import string
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "Cybersecurity API",
        "version": "1.1",
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

if __name__ == "__main__":
    app.run(debug=True)