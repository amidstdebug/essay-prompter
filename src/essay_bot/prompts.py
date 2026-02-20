from datetime import date

from cachetools import TTLCache

PROMPT_CACHE = TTLCache(maxsize=8, ttl=60 * 60 * 24 * 7)


def weekly_prompt() -> str:
    year, week, _ = date.today().isocalendar()
    cache_key = f"{year}-W{week}"
    if cache_key not in PROMPT_CACHE:
        PROMPT_CACHE[cache_key] = (
            "Placeholder prompt: Describe a historical event and explain how it still affects "
            "modern society."
        )
    return PROMPT_CACHE[cache_key]
