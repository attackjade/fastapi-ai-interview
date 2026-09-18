from fastapi import APIRouter
from app.services.chapter_service import get_all_chapters, get_by_id, create, update, remove
from app.core.exceptions import BusinessException
from app.schemas.chapter import ChapterCreate

router = APIRouter(
    prefix="/api/chapters",
    tags=["篇目管理"]
)

# 1. 获取全部篇目列表（分页）
@router.get("", summary="获取全部篇目列表（支持分页）")
async def get_chapter_list(page: int = 1, size: int = 3):
    """
    查询篇目目录
    page：页码，默认第1页
    size：单页条数，默认3条
    """
    data_source = get_all_chapters()
    start_index = (page - 1) * size
    end_index = start_index + size
    page_data = data_source[start_index:end_index]
    return {
        "code": 200,
        "msg": "查询成功",
        "data": {
            "page": page,
            "size": size,
            "total": len(data_source),
            "list": page_data
        }
    }

# 2. 根据ID查询单篇篇目
@router.get("/{chapter_id}", summary="根据ID查询单篇篇目")
async def get_chapter(chapter_id: int):
    item = get_by_id(chapter_id)
    if not item:
        raise BusinessException(code=404, msg="该篇目不存在")
    return {
        "code": 200,
        "msg": "查询成功",
        "data": item
    }

# 3. POST 新增篇目
@router.post("", summary="新增篇目")
async def create_chapter(body: ChapterCreate):
    new_item = create(body.title)
    return {
        "code": 200,
        "msg": "新增篇目成功",
        "data": new_item
    }

# 4. PUT 修改篇目名称
@router.put("/{chapter_id}", summary="修改篇目名称")
async def update_chapter(chapter_id: int, body: ChapterCreate):
    updated_item = update(chapter_id, body.title)
    if not updated_item:
        raise BusinessException(code=404, msg="篇目不存在")
    return {
        "code": 200,
        "msg": "更新成功",
        "data": updated_item
    }

# 5. DELETE 删除篇目
@router.delete("/{chapter_id}", summary="删除篇目")
async def delete_chapter(chapter_id: int):
    success = remove(chapter_id)
    if not success:
        raise BusinessException(code=404, msg="篇目不存在")
    return {
        "code": 200,
        "msg": "删除成功"
    }