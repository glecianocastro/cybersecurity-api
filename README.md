# cybersecurity-api
Simple Cybersecurity API built with Flask.

## Endpoints
### GET /

Returns API information.

### GET /health

Returns API health status.

### GET /password

Generates a random password.

### GET /hash/<text>

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

## Roadmap

- [x] v1.0 Password Generator
- [x] v1.1 SHA256 Hash Generator
- [x] v1.2 DNS Lookup
- [ ] v1.3 Password Stregth Checker
- [ ] v1.4 Port Scanner