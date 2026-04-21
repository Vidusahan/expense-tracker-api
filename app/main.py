from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import users
from routes import expenses

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(expenses.router)
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Welcome to Expense Tracker API"}