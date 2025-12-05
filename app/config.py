import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # example: https://investmalai.onrender.com
PORT = int(os.getenv("PORT", "10000"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
