import asyncio
import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from app.config import TELEGRAM_TOKEN, WEBHOOK_URL, PORT
from app.logging_config import setup_logging
from app.handlers.start import start
from app.handlers.help import help_command
from app.handlers.errors import error_handler


async def main():
    setup_logging()

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Error handler
    app.add_error_handler(error_handler)

    # Webhook mode
    await app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}"
    )


if __name__ == "__main__":
    asyncio.run(main())
from app.handlers.ai import ai_chat

# داخل main():
app.add_handler(CommandHandler("ai", ai_chat))
