from app.db.database import SessionLocal
from app.db.models import Message

db = SessionLocal()

try:
    new_message = Message(
        session_id=1,
        role="user",
        content="庄子的逍遥游主要讲了什么？"
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    print("消息创建成功")
    print("id:", new_message.id)
    print("session_id:", new_message.session_id)
    print("role:", new_message.role)
    print("content:", new_message.content)
    print("created_at:", new_message.created_at)

finally:
    db.close()