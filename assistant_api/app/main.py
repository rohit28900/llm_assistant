from fastapi import FastAPI
from app.controllers.assistant_controllers import router as assistant_router

app = FastAPI(
    title="Production LLM Assistant API",
    version="1.0.0"
)

app.include_router(assistant_router)
