from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = {
    "from_attributes": True
    }

class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: str
    date: date
    
class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: str
    date: date

    model_config = {
    "from_attributes": True
    }