from pydantic import BaseModel
from typing import List

class Expense(BaseModel):
    category: str
    amount: int
    date: str
    description: str
    

class ReportRequest(BaseModel):
    userId: int
    month: str
    data: List[Expense]