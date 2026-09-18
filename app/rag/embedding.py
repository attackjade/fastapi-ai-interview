from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-v4",
        input=text
    )

    return response.data[0].embedding