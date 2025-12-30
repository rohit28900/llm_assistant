from fastapi import APIRouter, HTTPException
from app.schemas.assistant_schema import AssistantRequest, AssistantResponse
from app.services.assistant_service import AssistantService
from app.core.logging import logger

router = APIRouter(prefix="/api/v1")

assistant_service = AssistantService()

@router.post("/assistant", response_model=AssistantResponse)
async def assistant(request: AssistantRequest):
    logger.info("Incoming assistant request")

    try:
        reply = await assistant_service.handle_user_message(request.message)
        return AssistantResponse(reply=reply)

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Assistant service unavailable"
        )
