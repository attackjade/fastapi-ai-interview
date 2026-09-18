from fastapi import Request
from fastapi.responses import JSONResponse

# 自定义业务异常
class BusinessException(Exception):
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg
        super().__init__(msg)


# 业务异常捕获处理器
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        content={
            "code": exc.code,
            "msg": exc.msg,
            "data": None
        }
    )

# 全局兜底未知异常处理器
async def _unknown_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        content={
            "code": 500,
            "msg": "服务运行异常，请稍后重试",
            "data": None
        }
    )


def register_global_exception(app):
    """注册全局异常捕获"""
    app.add_exception_handler(BusinessException, business_exception_handler)
    app.add_exception_handler(Exception, _unknown_exception_handler)