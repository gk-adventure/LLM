from typing import Union

from fastapi import FastAPI
from routers.chat import router as chat_router
from routers.report import router as report_router

app = FastAPI()

# 라우터 등록
app.include_router(chat_router, prefix="/api/chat", tags=["Chat"])
app.include_router(report_router, prefix="/api", tags=["Report"])

@app.get("/")
def main():
    return "Server is running"