# main.py

from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from models import Memo

app = FastAPI()

# 跨域配置，允许所有来源访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模拟存储备忘录的列表
memos = []

# 创建备忘录
@app.post("/memos/", response_model=Memo)
def create_memo(memo: Memo):
    memos.append(memo)
    return memo

# 获取所有备忘录
@app.get("/memos/", response_model=List[Memo])
def read_memos():
    return memos

# 更新备忘录
@app.put("/memos/{memo_id}", response_model=Memo)
def update_memo(memo_id: int, memo: Memo):
    for m in memos:
        if m.id == memo_id:
            m.title = memo.title
            m.content = memo.content
            return m
    raise HTTPException(status_code=404, detail="Memo not found")

# 删除备忘录
@app.delete("/memos/{memo_id}", response_model=Memo)
def delete_memo(memo_id: int):
    for i, m in enumerate(memos):
        if m.id == memo_id:
            return memos.pop(i)
    raise HTTPException(status_code=404, detail="Memo not found")
