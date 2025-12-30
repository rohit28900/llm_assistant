from app.repositories.llm_repository import LLMRepository

class AssistantService:
    def __init__(self):
        self.llm_repo = LLMRepository()

    async def handle_user_message(self, message: str) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful, concise AI assistant."},
            {"role": "user", "content": message}
        ]

        reply = await self.llm_repo.generate(messages)
        return reply
