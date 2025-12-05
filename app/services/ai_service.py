import asyncio
from openai import OpenAI
from app.config import OPENAI_API_KEY

class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    async def ask(self, prompt: str) -> str:
        try:
            loop = asyncio.get_event_loop()

            # تشغيل API بشكل غير متزامن داخل executor
            response = await loop.run_in_executor(
                None,
                lambda: self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt},
                    ]
                )
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"⚠️ AI Error: {e}"
