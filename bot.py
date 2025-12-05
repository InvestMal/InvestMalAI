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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 البوت يعمل بنجاح!")

async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ استخدم الأمر:\n/ai سؤالك…")
        return

    prompt = " ".join(context.args)
    await update.message.reply_text("⏳ جاري معالجة سؤالك…")

    answer = await ai.ask(prompt)
    await update.message.reply_text(answer)

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
