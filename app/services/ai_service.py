import asyncio
from openai import OpenAI
from typing import Optional
from app.config import OPENAI_API_KEY
import logging

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or OPENAI_API_KEY
        if not key:
            raise RuntimeError("OPENAI_API_KEY is not set in environment")
        # new OpenAI client
        self.client = OpenAI(api_key=key)

    async def ask(self, prompt: str) -> str:
        """Call OpenAI chat completion in a thread to avoid blocking event loop."""
        try:
            loop = asyncio.get_running_loop()

            def call_api():
                # synchronous call inside thread
                return self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt},
                    ],
                    # optionally set max_tokens, temperature, etc.
                )

            response = await loop.run_in_executor(None, call_api)

            # adapt to response shape
            content = ""
            if getattr(response, "choices", None):
                # new client returns objects; be defensive
                try:
                    content = response.choices[0].message.content.strip()
                except Exception:
                    # fallback if shape differs
                    content = str(response)
            else:
                content = str(response)

            return content

        except Exception as e:
            logger.exception("OpenAI request failed")
            return f"⚠️ AI Error: {e}"
