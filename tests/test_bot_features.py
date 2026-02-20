import importlib


def test_generate_button_keyboard_present(monkeypatch) -> None:
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test-token-12345")
    monkeypatch.setenv("SIGNUP_CODE", "test-signup-code")

    bot = importlib.import_module("essay_bot.bot")
    assert bot.PROMPT_KEYBOARD.keyboard[0][0].text == bot.GENERATE_PROMPT_BUTTON
