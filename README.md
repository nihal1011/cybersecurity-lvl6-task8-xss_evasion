# ShadowBypass: XSS Payload Evasion Toolkit

ShadowBypass is a lightweight toolkit designed to demonstrate evasion of Web Application Firewalls (WAFs) using character-based filter bypass techniques in Cross-Site Scripting (XSS) payloads. It includes a Python payload generator and a local HTML reflection test page.

---

## 📘 Overview

WAFs often rely on simple blacklists or character pattern filters to block malicious input. This project shows how attackers can modify XSS payloads using different encodings and structures to sneak past such filters while maintaining functionality.

---

## 🚀 Features

- Python script that generates multiple obfuscated versions of common XSS payloads
- Test interface using a local `index.html` page that mimics vulnerable input reflection
- Techniques include:
  - URL Encoding
  - HTML Entity Encoding
  - JavaScript Hex Encoding
  - Charcode Injection
  - Fragmentation

---

## 📂 Files

| File Name           | Purpose                                          |
|---------------------|--------------------------------------------------|
| `index.html`        | Local test page to simulate reflected XSS        |
| `xss_payload_gen.py`| Generates bypass payloads                        |
| `README.md`         | Project documentation                           |

---

## 🛠 How to Use

1. Clone this repo or download the files:

```bash
git clone https://github.com/YOUR_USERNAME/shadowbypass.git
cd shadowbypass
