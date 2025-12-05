from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available Commands:\n"
        "/start — Start the bot\n"
        "/help — Get help\n"
        "/ai <question> — Ask the AI"
    )
