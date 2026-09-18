from fastapi import FastAPI
from app.routers.chapter import router as chapter_router
# 导入异常注册函数
from app.core.exceptions import register_global_exception
# 导入AI路由
from app.routers.ai_chat import router as ai_chat_router

app = FastAPI(
    title="当我们在谈论《庄子》的时候我们在谈论什么？",
    version="5.2.0",
    description='''基于FastAPI构建的典籍研读后端API。
### 功能模块
- 篇目管理: 查询《庄子》内篇
- 段落管理: 浏览篇目段落、全文检索
- 研读笔记: CRUD个人研读笔记，支持标签和评分

## 技术栈
1. FastAPI + Pydantic + async/await
2. 标准三层架构：Router → Service → Model
3. 当前内存假数据，后续平滑迁移 SQLAlchemy'''
)

# 注册路由
app.include_router(chapter_router)

# 注册全局异常拦截
register_global_exception(app)

from app.common.middleware import register_middleware
register_middleware(app)

# 在注册chapter路由下方加上
app.include_router(ai_chat_router)
# 注册路由
app.include_router(chapter_router)
# AI对话路由
app.include_router(ai_chat_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)