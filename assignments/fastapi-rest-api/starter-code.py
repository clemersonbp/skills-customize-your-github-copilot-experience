"""Starter FastAPI application for the assignment.

Follow the README tasks to evolve this file. Suggested incremental steps:
1. Run: pip install fastapi uvicorn
2. Start dev server: uvicorn main:app --reload (after renaming this file to main.py if desired)
3. Add CRUD endpoints as per assignment.
"""
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Assignment", description="API para gerenciar itens", version="0.1.0")

class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# In-memory storage (will be replaced with simple CRUD logic in Task 2)
_items: List[Item] = [
    Item(id=1, name="Caderno", price=12.5, in_stock=True),
    Item(id=2, name="Caneta", price=3.2, in_stock=True),
]

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items", response_model=List[Item])
def list_items():
    return _items

# TODO (Task 2): Implement POST /items, GET /items/{item_id}, PUT, DELETE
# Suggested helpers:
# def _next_id() -> int: return max([i.id for i in _items], default=0) + 1
# Remember to raise HTTPException(status_code=404, detail="Item não encontrado") when appropriate.

# TODO (Optional Task): Support filtering via query params (in_stock, q)
