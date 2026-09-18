from app.rag.embedding import get_embedding


text = "《逍遥游》强调无待，追求精神上的自由。"

vector = get_embedding(text)

print("向量生成成功")
print("向量维度：", len(vector))
print("前10个值：", vector[:10])