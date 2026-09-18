from openai import OpenAI
import json
import os

from sqlalchemy.orm import Session

from app.db.models import Message
from app.rag.rag_service import build_rag_context
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-o6ymfo8ngp3n0jo4.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)
def qwen_stream_response(
    user_prompt: str,
    session_id: int,
    db: Session
):
    try:
        # 1. RAG 检索
        rag_context = build_rag_context(user_prompt)

        # 2. 查询最近 10 条历史消息
        history = (
            db.query(Message)
            .filter(Message.session_id == session_id)
            .order_by(Message.id.desc())
            .limit(10)
            .all()
        )

        history.reverse()

        # 3. 构造 RAG Prompt
        system_prompt = f"""
你是一个《庄子》研读助手。

请优先根据下面提供的《庄子》知识库内容回答问题。

【知识库内容】
{rag_context}

回答要求：
1. 优先依据知识库内容回答。
2. 如果知识库内容不足，请明确说明。
3. 不要编造《庄子》原文。
4. 同时结合当前会话历史理解用户的上下文。
"""

        # 4. 组装 messages
        llm_messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        for message in history:
            llm_messages.append({
                "role": message.role,
                "content": message.content
            })

        # 5. 调用 Qwen
        stream = client.chat.completions.create(
            model="qwen3.7-flash",
            messages=llm_messages,
            stream=True
        )

        full_answer = ""

        # 6. SSE 流式返回
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content

                full_answer += content

                yield (
                    f"data: "
                    f"{json.dumps({'content': content}, ensure_ascii=False)}"
                    f"\n\n"
                )

        # 7. 保存完整 AI 回答
        if full_answer:
            assistant_message = Message(
                session_id=session_id,
                role="assistant",
                content=full_answer
            )

            db.add(assistant_message)
            db.commit()

    except Exception as e:
        yield (
            f"data: "
            f"{json.dumps({'error': f'LLM调用异常: {str(e)}'}, ensure_ascii=False)}"
            f"\n\n"
        )