import logging
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
from app.services.ai_service import AIService
from app.config import TELEGRAM_TOKEN, WEBHOOK_URL, PORT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ai = AIService()

# --------------------------- Commands ---------------------------

from telegram.ext import CommandHandler, CallbackQueryHandler
from app.handlers.help import help_command
from app.handlers.help_callbacks import help_callback

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CallbackQueryHandler(help_callback))
# --------------------------- Main ---------------------------

def main():
    logger.info("🚀 Starting Telegram Bot...")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ai", ai_chat))

    # -------- Render Webhook Mode --------
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}",
    )

if __name__ == "__main__":
    main()
