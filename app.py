from flask import Flask
import random
import string

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "Cybersecurity APi",
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
        "status": "healthy"
    }
if __name__ == "__main__":
    app.run(debug=True)