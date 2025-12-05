import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception("Unhandled error while handling an update.")
    # optional: inform user
    try:
        if isinstance(update, Update) and update.message:
            await update.message.reply_text("⚠️ An internal error occurred. The team has been notified.")
    except Exception:
        logger.exception("Failed to send error message to user.")
