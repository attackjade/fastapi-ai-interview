from pathlib import Path

from app.rag.chunker import split_text
from app.rag.retriever import retrieve


def build_rag_context(query: str):
    text = Path(
        "knowledge/zhuangzi.txt"
    ).read_text(encoding="utf-8")

    chunks = split_text(
        text,
        chunk_size=100
    )

    results = retrieve(
        query=query,
        chunks=chunks,
        top_k=2
    )

    context = "\n\n".join(
        result["text"]
        for result in results
    )

    return context
