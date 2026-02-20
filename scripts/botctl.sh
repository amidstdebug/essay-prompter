#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"
PID_FILE="$ROOT_DIR/var/bot.pid"
LOG_FILE="$ROOT_DIR/logs/bot.log"

mkdir -p "$ROOT_DIR/var" "$ROOT_DIR/logs"

ensure_venv() {
  if [[ ! -d "$VENV_DIR" ]]; then
    python3 -m venv "$VENV_DIR"
    "$VENV_DIR/bin/pip" install --upgrade pip
    "$VENV_DIR/bin/pip" install -e "$ROOT_DIR"
  fi
}

is_running() {
  [[ -f "$PID_FILE" ]] || return 1
  local pid
  pid="$(cat "$PID_FILE")"
  kill -0 "$pid" 2>/dev/null
}

start() {
  if is_running; then
    echo "Bot already running (PID $(cat "$PID_FILE"))"
    return
  fi

  ensure_venv
  set -a
  [[ -f "$ROOT_DIR/.env" ]] && source "$ROOT_DIR/.env"
  set +a

  nohup "$VENV_DIR/bin/python" -m essay_bot >>"$LOG_FILE" 2>&1 &
  echo $! >"$PID_FILE"
  echo "Bot started (PID $(cat "$PID_FILE"))"
}

stop() {
  if ! is_running; then
    echo "Bot is not running"
    rm -f "$PID_FILE"
    return
  fi

  local pid
  pid="$(cat "$PID_FILE")"
  kill "$pid"
  rm -f "$PID_FILE"
  echo "Bot stopped"
}

status() {
  if is_running; then
    echo "Bot is running (PID $(cat "$PID_FILE"))"
  else
    echo "Bot is not running"
  fi
}

logs() {
  touch "$LOG_FILE"
  tail -n 50 -f "$LOG_FILE"
}

case "${1:-}" in
  start) start ;;
  stop) stop ;;
  restart) stop || true; start ;;
  status) status ;;
  logs) logs ;;
  *)
    echo "Usage: $0 {start|stop|restart|status|logs}"
    exit 1
    ;;
esac
