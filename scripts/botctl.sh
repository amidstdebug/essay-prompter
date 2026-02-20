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

load_env() {
  set -a
  [[ -f "$ROOT_DIR/.env" ]] && source "$ROOT_DIR/.env"
  set +a
}

is_running() {
  [[ -f "$PID_FILE" ]] || return 1
  local pid
  pid="$(cat "$PID_FILE")"
  kill -0 "$pid" 2>/dev/null
}

start() {
  if is_running; then
    echo "A detached bot is already running (PID $(cat "$PID_FILE"))."
    echo "Use '$0 stop' to stop it before running attached mode."
    return 1
  fi

  ensure_venv
  load_env

  echo "Starting bot in attached mode (Ctrl+C to stop)..."
  exec "$VENV_DIR/bin/python" -m essay_bot
}

start_bg() {
  if is_running; then
    echo "Bot already running in detached mode (PID $(cat "$PID_FILE"))"
    return
  fi

  ensure_venv
  load_env

  nohup "$VENV_DIR/bin/python" -m essay_bot >>"$LOG_FILE" 2>&1 &
  echo $! >"$PID_FILE"
  echo "Bot started in detached mode (PID $(cat "$PID_FILE"))"
}

stop() {
  if ! is_running; then
    echo "No detached bot is running"
    rm -f "$PID_FILE"
    return
  fi

  local pid
  pid="$(cat "$PID_FILE")"
  kill "$pid"
  rm -f "$PID_FILE"
  echo "Detached bot stopped"
}

status() {
  if is_running; then
    echo "Detached bot is running (PID $(cat "$PID_FILE"))"
  else
    echo "No detached bot is running"
  fi
}

logs() {
  touch "$LOG_FILE"
  tail -n 50 -f "$LOG_FILE"
}

case "${1:-}" in
  start) start ;;
  start-bg) start_bg ;;
  stop) stop ;;
  restart) stop || true; start_bg ;;
  status) status ;;
  logs) logs ;;
  *)
    echo "Usage: $0 {start|start-bg|stop|restart|status|logs}"
    exit 1
    ;;
esac
