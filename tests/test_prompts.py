from essay_bot.prompts import weekly_prompt


def test_weekly_prompt_returns_placeholder() -> None:
    assert "Placeholder prompt" in weekly_prompt()
