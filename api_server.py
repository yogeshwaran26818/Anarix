from fastapi import FastAPI
from pydantic import BaseModel
from main import ask_question

app = FastAPI(
    title="AI Agent API",
    description="Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → You’ll be able to POST a question like 'What is my total sales?'",
    version="1.0.0"
)

class Query(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the AI agent!",
        "tip": "Visit /docs to POST a question like 'What is my total sales?'"
    }

@app.post("/ask")
def ask(query: Query):
    answer = ask_question(query.question)
    return {"answer": answer}