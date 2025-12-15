from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="AI Text Generator")

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

MODEL_URL = "https://router.huggingface.co/hf-inference/models/openai-community/gpt2"

headers = {"Content-Type": "application/json"}
if HF_API_TOKEN:
    headers["Authorization"] = f"Bearer {HF_API_TOKEN}"


class Prompt(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "AI Text Generator is running"}


@app.post("/generate")
def generate_text(prompt: Prompt):
    response = requests.post(
        MODEL_URL,
        headers=headers,
        json={"inputs": prompt.text},
        timeout=30
    )

    if response.status_code != 200:
        return {
            "error": "Hugging Face API error",
            "status_code": response.status_code,
            "details": response.text
        }

    return response.json()
