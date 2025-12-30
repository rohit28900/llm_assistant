from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential
from app.core.config import settings
from app.core.logging import logger

class LLMRepository:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=1, max=5)
    )
    async def generate(self, messages: list[dict]) -> str:
        try:
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=messages,
                temperature=0.3,
                timeout=settings.OPENAI_TIMEOUT
            )
            return response.choices[0].message.content

        except Exception:
            logger.exception("LLM repository failure")
            raise
