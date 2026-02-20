import os
import subprocess
import sys


def test_main_entrypoint_reports_configuration_error() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    env["TELEGRAM_BOT_TOKEN"] = "test-token-12345"
    env.pop("SIGNUP_CODE", None)

    result = subprocess.run(
        [sys.executable, "-m", "essay_bot"],
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert result.returncode == 1
    assert "Failed to start bot due to configuration/runtime import error." in result.stderr
    assert "SIGNUP_CODE" in result.stderr
