def extract_features(url: str):
      return {
        "length": len(url),
        "num_dots": url.count('.'),
        "has_at": int('@' in url),
        "has_https": int(url.startswith("https")),
        "num_digits": sum(c.isdigit() for c in url),
        "has_login": int("login" in url.lower()),
    }