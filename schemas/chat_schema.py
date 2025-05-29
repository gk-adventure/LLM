from pydantic import BaseModel
from typing import Union

class ChatRequest(BaseModel):
    userId: int
    message: str

class ExpenseData(BaseModel):
    save_type: int
    category: str
    amount: int
    date: str
    memo: str
    
class ChatResponse(BaseModel):
    type: str
    reply: str
    data: Union[ExpenseData, None] = None

