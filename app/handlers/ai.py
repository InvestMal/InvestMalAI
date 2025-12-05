from telegram import Update
from telegram.ext import ContextTypes
from app.services.ai_service import AIService

_ai_service = AIService()

async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Support both /ai text and /ai <args>
    # If user sends /ai without args, show usage
    user_text = ""
    if context.args:
        user_text = " ".join(context.args)
    else:
        # Also support messages like "/ai\n<text>" if exists in message.text
        full = (update.message.text or "").strip()
        parts = full.split(maxsplit=1)
        if len(parts) == 2:
            user_text = parts[1].strip()

    if not user_text:
        await update.message.reply_text("❗ استخدم الأمر هكذا:\n/ai ما هو سؤالك؟")
        return

    await update.message.reply_text("⏳ جاري معالجة طلبك…")
    answer = await _ai_service.ask(user_text)
    await update.message.reply_text(answer)
