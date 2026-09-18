# 基于 RAG 的《庄子》智能研读系统

一个基于 **FastAPI + MySQL + SQLAlchemy + Qwen + RAG** 实现的垂直领域 AI 研读后端项目。

项目面向《庄子》文本研读场景，支持多轮对话、聊天记录持久化、SSE 流式输出，并通过知识库检索增强生成（RAG）为大模型提供相关原文上下文。

## 主要功能

- 基于 FastAPI 搭建后端 API
- 基于 MySQL + SQLAlchemy 实现用户、会话和消息持久化
- 接入通义千问（Qwen）大模型
- 支持多轮上下文对话
- 基于 SSE 实现流式回答
- 对《庄子》知识库进行文本切分
- 使用 DashScope Embedding 生成文本向量
- 使用 NumPy 计算余弦相似度
- 基于 Top-K 检索相关知识片段
- 将检索结果动态注入 Prompt，实现基础 RAG 问答
- 大模型完整回答生成后写入数据库

## 技术栈

- Python
- FastAPI
- Pydantic
- MySQL
- SQLAlchemy
- Qwen LLM API
- DashScope Embedding
- RAG
- NumPy
- SSE
- Git

## 项目结构

```text
fastapi-ai-interview/
├─ app/
│  ├─ db/
│  │  ├─ database.py
│  │  └─ models.py
│  ├─ rag/
│  │  ├─ chunker.py
│  │  ├─ embedding.py
│  │  ├─ retriever.py
│  │  └─ rag_service.py
│  ├─ routers/
│  │  └─ ai_chat.py
│  └─ services/
│     └─ ai_service.py
├─ knowledge/
│  └─ zhuangzi.txt
├─ main.py
└─ README.md
```

## RAG 流程

```text
用户问题
  ↓
读取知识库
  ↓
文本 Chunk
  ↓
Embedding
  ↓
余弦相似度计算
  ↓
Top-K 检索
  ↓
组装 RAG Prompt
  ↓
Qwen 生成回答
  ↓
SSE 流式返回
  ↓
完整回答写入 MySQL
```

## 环境变量

项目中的 API Key 和数据库连接信息不应直接提交到 GitHub。

建议通过环境变量配置：

```text
DASHSCOPE_API_KEY=your_api_key
DATABASE_URL=your_database_url
```

请勿将真实 `.env` 文件、API Key 或数据库密码提交到公开仓库。

## 当前状态

已完成：

- FastAPI 后端接口
- MySQL / SQLAlchemy 数据持久化
- 多轮上下文对话
- Qwen 大模型接入
- SSE 流式输出
- 基础 RAG 检索增强问答
- Embedding + 余弦相似度 Top-K 检索

## 项目说明

本项目主要用于学习和实践 AI 应用开发中的后端工程与 RAG 基础链路，重点实现从知识库检索、上下文组装到大模型流式生成与消息持久化的完整流程。
