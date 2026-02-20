import logging
from datetime import time
from zoneinfo import ZoneInfo

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from essay_bot.config import settings
from essay_bot.database import init_db, list_active_users, upsert_user
from essay_bot.prompts import weekly_prompt
from essay_bot.security import verify_signup_code

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("essay_bot")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Welcome! Use /signup <code> to register for weekly Friday essay prompts at 5 p.m."
        )


async def signup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_user or not update.effective_chat or not update.message:
        return

    if not context.args:
        await update.message.reply_text("Usage: /signup <signup_code>")
        return

    if not verify_signup_code(context.args[0], settings.signup_code):
        await update.message.reply_text("Invalid signup code.")
        return

    user = update.effective_user
    upsert_user(
        telegram_user_id=user.id,
        chat_id=update.effective_chat.id,
        username=user.username,
        first_name=user.first_name,
    )
    await update.message.reply_text("Signup successful. You'll get a prompt every Friday at 5 p.m.")


async def prompt_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(f"Essay prompt:\n\n{weekly_prompt()}")


async def send_weekly_prompt(context: ContextTypes.DEFAULT_TYPE) -> None:
    users = list_active_users()
    prompt_text = weekly_prompt()
    if not users:
        logger.info("No active users to notify")
        return

    for user in users:
        try:
            await context.bot.send_message(
                chat_id=user.chat_id,
                text=f"Weekly essay prompt:\n\n{prompt_text}",
            )
        except Exception as exc:
            logger.warning("Unable to send prompt to chat_id=%s: %s", user.chat_id, exc)


def build_application() -> Application:
    init_db()
    application = Application.builder().token(settings.telegram_bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signup", signup))
    application.add_handler(CommandHandler("prompt", prompt_now))

    local_tz = ZoneInfo(settings.app_timezone)
    application.job_queue.run_daily(
        send_weekly_prompt,
        time=time(hour=settings.friday_send_hour, minute=0, tzinfo=local_tz),
        days=(4,),  # Friday
        name="weekly-essay-prompt",
        job_kwargs={"misfire_grace_time": 60 * 60},
    )
    return application


def main() -> None:
    app = build_application()
    logger.info("Starting essay prompter bot")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
