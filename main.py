from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from models import Memo, SessionLocal, engine

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源访问，可以根据实际需要进行配置
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的请求头
)

# 数据库会话依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class MemoIn(BaseModel):
    title: str
    content: str

class MemoOut(BaseModel):
    id: int
    title: str
    content: str

# 创建备忘录
@app.post("/memos/", response_model=MemoOut)
def create_memo(memo: MemoIn, db: Session = Depends(get_db)):
    db_memo = Memo(title=memo.title, content=memo.content)
    # 处理额外的字段
    if hasattr(memo, 'type'):
        db_memo.type = memo.type
    db.add(db_memo)
    db.commit()
    db.refresh(db_memo)
    return db_memo



# 获取所有备忘录
@app.get("/memos/", response_model=List[MemoOut])
def read_memos(db: Session = Depends(get_db)):
    return db.query(Memo).all()

# 更新备忘录
@app.put("/memos/{memo_id}", response_model=MemoOut)
def update_memo(memo_id: int, memo: MemoIn, db: Session = Depends(get_db)):
    db_memo = db.query(Memo).filter(Memo.id == memo_id).first()
    if db_memo is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    db_memo.title = memo.title
    db_memo.content = memo.content
    db.commit()
    db.refresh(db_memo)
    return db_memo

# 删除备忘录
@app.delete("/memos/{memo_id}", response_model=MemoOut)
def delete_memo(memo_id: int, db: Session = Depends(get_db)):
    db_memo = db.query(Memo).filter(Memo.id == memo_id).first()
    if db_memo is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    db.delete(db_memo)
    db.commit()
    return db_memo
