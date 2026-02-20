from essay_bot.security import verify_signup_code


def test_verify_signup_code_exact_match() -> None:
    assert verify_signup_code("strong-code", "strong-code")


def test_verify_signup_code_rejects_non_match() -> None:
    assert not verify_signup_code("wrong", "strong-code")
