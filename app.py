from flask import Flask
import random
import string
import hashlib
import socket
import re
from datetime import datetime
import requests
import whois
import ssl

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "timestamp": datetime.now().isoformat(),
        "project": "Security Toolkit API",
        "version": "2.3",
        "status": "online",
        "endpoints": {
            "health": "/health",
            "password_generator": "/password",
            "hash_generator": "/hash/<text>",
            "dns_lookup": "/dns/<host>",
            "password_strength": "/password-strength/<password>",
            "port_scanner": "/scan/<host>",
            "header_analyzer": "/headers/<host>",
            "whois_lookup": "/whois/<domain>"
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
        "version": "2.3",
        "service": "Security Tollkit API"
    }

@app.route("/info")
def info():
    return {
        "author": "Gleciano Castro",
        "language": "Python",
        "framework": "Flask",
        "version": "2.3"
    }

@app.route("/hash/<algorithm>/<text>")
def generate_hash(algorithm, text):

    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }

    if algorithm not in algorithms:

        return {
            "error": "Unsupported algorithm"
        }

    hash_value = algorithms[algorithm](
        text.encode()
    ).hexdigest()

    return {
        "algorithm": algorithm,
        "text": text,
        "hash": hash_value
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

@app.route("/headers/<host>")
def headers_lookup(host):

    try:

        response = requests.get(
            f"https://{host}",
            timeout=5
        )

        security_headers = {
            "strict-transport-security":
                response.headers.get(
                    "Strict-Transport-Security"
                ),
            "x-frame-options":
                response.headers.get(
                    "X-Frame-Options"
                ),
            "content-security-policy":
                response.headers.get(
                    "Content-Security-Policy"
                ),
            "server":
                response.headers.get(
                    "Server"
                )
        }

        return {
            "host": host,
            "security_headers": security_headers
        }
    
    except Exception as e:
        
        return {
            "error": str(e)
        }
    
@app.route("/whois/<domain>")
def whois_lookup(domain):

        try:

            info = whois.whois(domain)

            return {
                "domain": domain,
                "registrar": str(info.registrar),
                "creation_date": str(info.creation_date),
                "expiration_date": str(info.expiration_date)
            }
        
        except Exception as e:

            return {
                "error": str(e)
            }

@app.route("/ssl/<host>")
def ssl_info(host):

    try:

        context = ssl.create_default_context()

        with context.wrap_socket(
            socket.socket(),
            server_hostname=host
        ) as sock:
            
            sock.settimeout(5)
            sock.connect((host, 443))
            cert = sock.getpeercert()
            issuer = dict(
                x[0]
                for x in cert["issuer"]
            )
            subject = dict(
                x[0]
                for x in cert["subject"]
            )
            return {
                "host": host,
                "issuer": issuer.get(
                    "organizationName",
                    "Unknown"
                ),
                "subject": subject.get(
                    "commonName",
                    "Unknown"
                ),
                "valid_from": cert["notBefore"],
                "valid_until": cert["notAfter"]
            }

    except Exception as e:

        return {
            "error": str(e)
        }

if __name__ == "__main__":
    app.run(debug=True)