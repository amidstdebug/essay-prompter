import random
from datetime import date, timedelta

from cachetools import TTLCache

from essay_bot.assignment_engine import DIFFICULTY_PROFILES, propose_essay_assignment

PROMPT_CACHE = TTLCache(maxsize=16, ttl=60 * 60 * 24 * 8)


def _difficulty_for_week(year: int, week: int) -> str:
    rng = random.Random(year * 100 + week)
    return rng.choice(tuple(DIFFICULTY_PROFILES))


def _blindfold_prompt(proposed_question: str) -> str:
    hidden_section_marker = " Difficulty level:"
    if hidden_section_marker in proposed_question:
        return proposed_question.split(hidden_section_marker, maxsplit=1)[0]
    return proposed_question


def weekly_prompt() -> str:
    today = date.today()
    year, week, _ = today.isocalendar()
    selected_difficulty = _difficulty_for_week(year, week)
    cache_key = f"{year}-W{week}:{selected_difficulty}"

    if cache_key not in PROMPT_CACHE:
        assignment = propose_essay_assignment(
            difficulty=selected_difficulty,
            seed=year * 100 + week,
        )
        prev_year, prev_week, _ = (today - timedelta(weeks=1)).isocalendar()
        previous_difficulty = _difficulty_for_week(prev_year, prev_week)
        previous_label = DIFFICULTY_PROFILES[previous_difficulty]["label"]
        PROMPT_CACHE[cache_key] = (
            f"Last week's hidden difficulty was: {previous_label}.\n\n"
            f"This week's essay assignment:\n"
            f"{_blindfold_prompt(assignment['proposed_question'])}"
        )

    return PROMPT_CACHE[cache_key]
