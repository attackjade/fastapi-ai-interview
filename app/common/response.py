from typing import Any

def success(data: Any = None, msg: str = "操作成功"):
    """统一成功返回格式"""
    return {
        "code": 200,
        "msg": msg,
        "data": data
    }

def fail(code: int, msg: str, data: Any = None):
    """统一失败返回"""
    return {
        "code": code,
        "msg": msg,
        "data": data
    }