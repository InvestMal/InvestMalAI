from telegram import Update
from telegram.ext import ContextTypes
from app.services.ai_service import AIService

ai = AIService()

async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ استخدم الأمر هكذا:\n/ai ما هو سؤالك؟")
        return

    user_prompt = " ".join(context.args)

    await update.message.reply_text("⏳ جاري معالجة طلبك…")

    answer = await ai.ask(user_prompt)
    await update.message.reply_text(answer)
