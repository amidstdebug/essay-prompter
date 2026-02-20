import pytest

from essay_bot.assignment_engine import propose_essay_assignment


def test_assignment_generation_is_seeded() -> None:
    first = propose_essay_assignment("advanced", seed=123)
    second = propose_essay_assignment("advanced", seed=123)
    assert first["proposed_question"] == second["proposed_question"]


def test_invalid_difficulty_raises() -> None:
    with pytest.raises(ValueError):
        propose_essay_assignment("expert")
