from fastapi import FastAPI

app = FastAPI()

# 数据示例
items = [{"name": "英短"}, {"name": "英长"}]

# 路由1: 获取项列表
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return items[skip:skip + limit]

# 路由2: 欢迎消息
@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)



