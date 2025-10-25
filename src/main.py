# src/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Orbcrucible!"}

@app.post("/nodes")
async def create_node(node: dict):
    return {"id": node.get("id"), "label": node.get("label")}