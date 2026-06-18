# Security Toolkit API
A cybersecurity-focused API built with Python and Flask.
Current Version: v2.3

## Features

- Password Generator
- SHA256 Hash Generator
- DNS Lookup
- Password Strength Checker
- Port Scanner
- Multi Hash Generator
- Header Analyzer
- WHOIS Lookup
- SSL Certificate Checker

## Installation

Clone the repository:

```bash
git clone https://github.com/glecianocastro/security-toolkit-api.git
```

Navigate to the project:

```bash
cd security-toolkit-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## Endpoints

### GET /

Returns API information.

### GET /health

Returns API health status.

### GET /password

Generates a random password.

### GET /hash/<algorithm>/<text>

Generates a SHA256 hash from the provided text.

Example:

```text
/hash/hello
```

Response:

```json
{
    "text": "hello",
    "sha256": "2cf24dba5fb0..."
}
```

### GET /dns/<host>

Get the IP from the provided host.

Example:

```host
/dns/google.com
```

Response:

```json
{
    "host": "google.com",
    "ip": "142.250.x.x"
}
```

### GET /password-strength/<password>

Get the password provided and check

Example:

```password
/password-strength/admin
```

Response:

```json
{
    "password": "admin",
    "score": "1",
    "strength": "Weak"
}
```

## GET /scan/<host>

Get the host provided and try to resolve the DNS

Example:

```host
/scan/github.com
```

Response:

```json
{
    "host": "github.com",
    "ip": "4.228.31.150",
    "open_ports": [
        22,
        443
    ]
}
```

- Multi Hash Generator

### GET /hash/<algorithm>/<text>
```Supported algorithm
md5
sha1
sha256
sha512
```

- Header Analyzer

### GET /headers/<host>

### GET /whois/<domain>

- Who is the domain

### GET /ssl/<host>

Returns SSL certificate information.

## Roadmap

- [x] v1.0 Password Generator
- [x] v1.1 SHA256 Hash Generator
- [x] v1.2 DNS Lookup
- [x] v1.3 Password Strength Checker
- [x] v1.4 Port Scanner
- [x] v2.0 Security Toolkit API
- [x] v2.1 Multi Hash Generator
- [x] v2.2 HTTP Header Analyzer
- [x] v2.3 WHOIS Lookup
- [x] v2.4 SSL Certificate Checker