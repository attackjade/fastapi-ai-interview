from pydantic import BaseModel, Generic
from typing import TypeVar, Optional

T = TypeVar("T")

class ApiResp(BaseModel, Generic[T]):
    """全局统一API返回格式"""
    code: int
    msg: str
    data: Optional[T] = None