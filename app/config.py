import os

# Required env vars (set these securely in Render)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g. https://your-service.onrender.com
PORT = int(os.getenv("PORT", 10000))

# OpenAI key (used by AI service)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Minimal validation (helps early failure in logs if missing)
if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN is not set in environment")
if not WEBHOOK_URL:
    raise RuntimeError("WEBHOOK_URL is not set in environment")
