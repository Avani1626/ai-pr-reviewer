from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai_reviewer import ai_review_pr

# Create FastAPI app
app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define expected request body
class PRRequest(BaseModel):
    title: str
    description: str
    code: str

# API endpoint
@app.post("/review")
def review_pr(data: PRRequest):
    result = ai_review_pr(
        data.title,
        data.description,
        data.code
    )
    return result
