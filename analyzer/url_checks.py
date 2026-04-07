import re
from urllib.parse import urlparse

def extract_features(url: str):
      parsed = urlparse(url)
      domain = parsed.netloc
      return {
        "length": len(url),
        "num_dots": url.count('.'),
        "has_at": int('@' in url),
        "has_https": int(url.startswith("https")),
        "num_digits": sum(c.isdigit() for c in url),
        "has_login": int("login" in url.lower()),
        "domain_length": len(domain),
        "num_hyphens": domain.count('-'),
        "suspicious_tld": int(domain.endswith((".xyz", ".tk", ".ru")))
    }