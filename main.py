from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Memo(BaseModel):
    id: int
    title: str
    content: Optional[str] = None

# 存储备忘录的“数据库”
memos = []

@app.post("/memos/", response_model=Memo)
def create_memo(memo: Memo):
    if any(existing_memo.id == memo.id for existing_memo in memos):
        raise HTTPException(status_code=400, detail="Memo with this ID already exists")
    memos.append(memo)
    return memo

@app.get("/memos/", response_model=List[Memo])
def read_memos():
    return memos

@app.get("/memos/{memo_id}", response_model=Memo)
def read_memo(memo_id: int):
    for memo in memos:
        if memo.id == memo_id:
            return memo
    raise HTTPException(status_code=404, detail="Memo not found")

@app.put("/memos/{memo_id}", response_model=Memo)
def update_memo(memo_id: int, updated_memo: Memo):
    for i, memo in enumerate(memos):
        if memo.id == memo_id:
            memos[i] = updated_memo
            return updated_memo
    raise HTTPException(status_code=404, detail="Memo not found")

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    for i, memo in enumerate(memos):
        if memo.id == memo_id:
            del memos[i]
            return {"message": "Memo deleted successfully"}
    raise HTTPException(status_code=404, detail="Memo not found")
