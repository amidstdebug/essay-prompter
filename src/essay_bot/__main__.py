import sys


def main() -> None:
    try:
        from essay_bot.bot import main as run_bot
    except Exception as exc:
        print("Failed to start bot due to configuration/runtime import error.", file=sys.stderr)
        print(f"Details: {exc}", file=sys.stderr)
        print(
            "Ensure TELEGRAM_BOT_TOKEN and SIGNUP_CODE are set in .env or environment.",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc

    run_bot()


if __name__ == "__main__":
    main()
