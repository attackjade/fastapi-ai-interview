import numpy as np

from app.rag.embedding import get_embedding


def cosine_similarity(vector_a, vector_b):
    a = np.array(vector_a)
    b = np.array(vector_b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def retrieve(query: str, chunks: list[str], top_k: int = 2):
    # 1. 用户问题 → 向量
    query_vector = get_embedding(query)

    results = []

    # 2. 每一个知识块 → 向量
    for chunk in chunks:
        chunk_vector = get_embedding(chunk)

        # 3. 计算问题和知识块的相似度
        score = cosine_similarity(
            query_vector,
            chunk_vector
        )

        results.append({
            "text": chunk,
            "score": float(score)
        })

    # 4. 相似度从高到低排序
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # 5. 只返回最相关的 Top-K
    return results[:top_k]