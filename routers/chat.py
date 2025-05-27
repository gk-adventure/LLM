from fastapi import APIRouter, HTTPException
from schemas.chat_schema import ChatRequest, ChatResponse
from services.chat_service import handle_message

router = APIRouter()

@router.post("/message", response_model=ChatResponse)
def chat_with_user(request: ChatRequest):
    try:
        result = handle_message(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))