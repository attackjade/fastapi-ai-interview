import time
from fastapi import Request
from fastapi.responses import JSONResponse

async def log_middleware(request: Request, call_next):
    start_time = time.time()
    # 执行接口逻辑
    response = await call_next(request)
    # 计算耗时
    cost = round((time.time() - start_time) * 1000, 2)
    client_ip = request.client.host if request.client else "unknown"
    path = request.url.path
    method = request.method

    print(f"【API日志】{method} {path} | IP:{client_ip} | 耗时:{cost} ms")
    return response

def register_middleware(app):
    app.middleware("http")(log_middleware)