from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return "Server is running"