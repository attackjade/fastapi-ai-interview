from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, text

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )


class ChatSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    title = Column(String(100), nullable=False)
    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(
        Integer,
        ForeignKey("sessions.id"),
        nullable=False
    )
    role = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )