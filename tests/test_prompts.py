import importlib


def test_weekly_prompt_blindfolds_current_difficulty_and_reveals_previous(monkeypatch) -> None:
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test-token-12345")
    monkeypatch.setenv("SIGNUP_CODE", "test-signup-code")

    prompts = importlib.import_module("essay_bot.prompts")
    prompt = prompts.weekly_prompt()

    assert "Write a" in prompt
    assert "Last week's hidden difficulty was:" in prompt
    assert "Difficulty level:" not in prompt
