from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from app.services.ai_service import qwen_stream_response
from app.db.database import get_db
from app.db.models import Message, ChatSession


router = APIRouter(prefix="/api/ai", tags=["AI大模型对话"])

# 定义请求体模型
class ChatRequest(BaseModel):
    session_id:int
    prompt: str

class SessionCreateRequest(BaseModel):
    user_id: int
    title: str

@router.post("/session", summary="创建新的聊天会话")
async def create_session(
    req: SessionCreateRequest,
    db: Session = Depends(get_db)
):
    new_session = ChatSession(
        user_id=req.user_id,
        title=req.title
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return {
        "session_id": new_session.id,
        "user_id": new_session.user_id,
        "title": new_session.title
    }

@router.post("/chat/stream", summary="通义千问流式对话 SSE打字机输出")
async def chat_stream(
    req: ChatRequest,
    db: Session = Depends(get_db)
):
    user_message = Message(
        session_id=req.session_id,
        role="user",
        content=req.prompt
    )

    db.add(user_message)
    db.commit()

    generator = qwen_stream_response(
        user_prompt=req.prompt,
        session_id=req.session_id,
        db=db
    )

    return StreamingResponse(
        generator,
        media_type="text/event-stream"
    )