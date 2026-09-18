from pathlib import Path

from app.rag.chunker import split_text


text = Path("knowledge/zhuangzi.txt").read_text(
    encoding="utf-8"
)

chunks = split_text(text, chunk_size=100)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i} ---")
    print(chunk)