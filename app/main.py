from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="AI Text Generator")

# Hugging Face token (обязательно для router API)
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# Новый официальный endpoint Hugging Face для text-generation
MODEL_URL = "https://api-inference.huggingface.co/models/gpt2?pipeline_tag=text-generation"

headers = {}
if HF_API_TOKEN:
    headers["Authorization"] = f"Bearer {HF_API_TOKEN}"


class Prompt(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "AI Text Generator is running"}


@app.post("/generate")
def generate_text(prompt: Prompt):
    try:
        response = requests.post(
            MODEL_URL,
            headers=headers,
            json={"inputs": prompt.text, "options": {"wait_for_model": True}},
            timeout=30
        )

        if response.status_code != 200:
            return {
                "error": "Hugging Face API error",
                "status_code": response.status_code,
                "details": response.text
            }

        return response.json()

    except Exception as e:
        return {"error": str(e)}
