from pathlib import Path

from app.rag.chunker import split_text
from app.rag.retriever import retrieve


text = Path(
    "knowledge/zhuangzi.txt"
).read_text(encoding="utf-8")

chunks = split_text(text, chunk_size=100)

results = retrieve(
    query="庄子认为真正的自由需要依赖外界条件吗？",
    chunks=chunks,
    top_k=2
)

for result in results:
    print("\n相似度：", result["score"])
    print("内容：", result["text"])