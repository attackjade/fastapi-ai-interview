from pydantic import BaseModel, Field

# 单条篇目基础模型（查询返回）
class Chapter(BaseModel):
    chapter_id: int
    title: str

# 创建篇目请求模型（POST入参校验）
class ChapterCreate(BaseModel):
    title: str = Field(min_length=1, max_length=32, description="篇目名称")

# 分页数据封装模型
class ChapterPage(BaseModel):
    page: int
    size: int
    total: int
    list: list[Chapter]