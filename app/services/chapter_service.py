# app/services/chapter_service.py
CHAPTER_MAP = [
    {"chapter_id": 1, "title": "逍遥游"},
    {"chapter_id": 2, "title": "齐物论"},
    {"chapter_id": 3, "title": "人间世"},
    {"chapter_id": 4, "title": "德充符"},
    {"chapter_id": 5, "title": "大宗师"},
    {"chapter_id": 6, "title": "应帝王"},
]

def get_all_chapters():
    """查询全部篇目"""
    return CHAPTER_MAP.copy()

def get_by_id(chapter_id: int):
    """根据id查询单条，找不到返回None"""
    for item in CHAPTER_MAP:
        if item["chapter_id"] == chapter_id:
            return item
    return None

def create(title: str):
    """新增篇目"""
    max_id = max(i["chapter_id"] for i in CHAPTER_MAP)
    new_item = {"chapter_id": max_id + 1, "title": title}
    CHAPTER_MAP.append(new_item)
    return new_item

def update(chapter_id: int, new_title: str):
    item = get_by_id(chapter_id)
    if not item:
        return None
    item["title"] = new_title
    item["title"] = new_title
    return item

def remove(chapter_id: int):
    global CHAPTER_MAP
    target = get_by_id(chapter_id)
    if not target:
        return False
    CHAPTER_MAP = [x for x in CHAPTER_MAP if x["chapter_id"] != chapter_id]
    return True