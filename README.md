# Essay Prompter Telegram Bot

A production-style starter for a Telegram bot that allows users to sign up and receive a weekly essay prompt every Friday at 5 p.m. (configurable timezone).

## Features

- `/signup <code>` flow with constant-time signup code verification.
- SQLite-backed user registry for authentication/authorization of recipients.
- Weekly scheduled delivery using Telegram JobQueue (Friday 17:00 in configured timezone).
- Weekly prompt generator now uses a configurable 4-variable assignment engine (essay type, topic, lens, rhetorical brief).
- Prompt caching layer to avoid expensive re-computation during the same week.
- Operational shell control script for `start`, `stop`, `restart`, `status`, and `logs`.
- Structured package layout with tests and linting hooks.

## Project layout

- `src/essay_bot/bot.py`: Telegram handlers and Friday scheduler.
- `src/essay_bot/database.py`: SQLAlchemy models and database helpers.
- `src/essay_bot/security.py`: security-related primitives.
- `src/essay_bot/prompts.py`: placeholder prompt generation + caching.
- `scripts/botctl.sh`: service management script.
- `tests/`: baseline unit tests.

## Quick start

1. Copy env file and edit values:
   ```bash
   cp .env.example .env
   ```
2. Start bot:
   ```bash
   ./scripts/botctl.sh start
   ```
3. Check status/logs:
   ```bash
   ./scripts/botctl.sh status
   ./scripts/botctl.sh logs
   ```
4. Stop bot:
   ```bash
   ./scripts/botctl.sh stop
   ```

## Environment variables

- `TELEGRAM_BOT_TOKEN` (required): Bot token from BotFather.
- `SIGNUP_CODE` (required): Secret shared with allowed users.
- `DATABASE_URL` (optional): Defaults to `sqlite:///./var/essay_bot.db`.
- `APP_TIMEZONE` (optional): IANA timezone (default `UTC`).
- `FRIDAY_SEND_HOUR` (optional): 0-23 hour (default `17`).

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
ruff check .
pytest
```

## Security notes

- Do not commit `.env`.
- Use a strong random `SIGNUP_CODE`.
- For production, move from SQLite to managed Postgres and run behind a process supervisor (systemd, Docker, etc.).
