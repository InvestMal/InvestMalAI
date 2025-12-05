from telegram import Update
from telegram.ext import ContextTypes

async def help_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = {
        "help_ai": (
            "🤖 **AI Trading Commands**\n"
            "/ai - Ask AI anything\n"
            "/analysis - Full market analysis\n"
            "/chat - Start AI session\n"
            "/stop - End AI session\n"
            "/summary - Summarize text\n"
            "/translate - Translate text"
        ),
        "help_market": (
            "📊 **Market Tools**\n"
            "/price - Live asset price\n"
            "/chart - AI chart analysis\n"
            "/levels - Support & resistance\n"
            "/sentiment - Market sentiment\n"
            "/compare - Compare two assets"
        ),
        "help_trading": (
            "💰 **Trading Tools**\n"
            "/convert - Currency converter\n"
            "/calculator - Profit/Loss calculator"
        ),
        "help_alerts": (
            "🔔 **Alerts**\n"
            "/alert - Set a price alert\n"
            "/alerts - Show active alerts\n"
            "/clearalerts - Clear all alerts"
        ),
        "help_general": (
            "⚙️ **General Commands**\n"
            "/start - Start bot\n"
            "/help - Show commands\n"
            "/about - About InvestMal Ai\n"
            "/support - Contact support\n"
            "/ping - Bot speed test"
        )
    }

    text = data.get(query.data, "❗ Unknown section")
    await query.edit_message_text(text, parse_mode="Markdown")
