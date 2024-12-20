from fastapi import FastAPI
from .routers import lessons, users

app = FastAPI()
app.include_router(lessons.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello world!"}
