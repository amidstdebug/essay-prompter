import hmac


def verify_signup_code(provided_code: str, expected_code: str) -> bool:
    sanitized = provided_code.strip()
    return hmac.compare_digest(sanitized, expected_code)
