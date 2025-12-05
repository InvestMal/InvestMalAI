from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🤖 AI Trading", callback_data="help_ai"),
            InlineKeyboardButton("📊 Market Tools", callback_data="help_market")
        ],
        [
            InlineKeyboardButton("💰 Trading Tools", callback_data="help_trading"),
            InlineKeyboardButton("🔔 Alerts", callback_data="help_alerts")
        ],
        [
            InlineKeyboardButton("⚙️ General", callback_data="help_general")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "**📘 InvestMal Ai — Help Menu**\n"
        "اختر القسم لرؤية الأوامر:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
