def split_text(text: str, chunk_size: int = 300):
    paragraphs = text.split("\n\n")

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        # 如果加入下一段后没有超过限制，就继续合并
        if len(current_chunk) + len(paragraph) <= chunk_size:
            if current_chunk:
                current_chunk += "\n\n"
            current_chunk += paragraph

        else:
            # 先保存当前 chunk
            if current_chunk:
                chunks.append(current_chunk)

            current_chunk = paragraph

    # 保存最后一个 chunk
    if current_chunk:
        chunks.append(current_chunk)

    return chunks