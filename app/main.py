from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="AI Text Generator")

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

API_URL = "https://router.huggingface.co/v1/completions"

headers = {
    "Content-Type": "application/json",
}

if HF_API_TOKEN:
    headers["Authorization"] = f"Bearer {HF_API_TOKEN}"


class Prompt(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "AI Text Generator is running"}


@app.post("/generate")
def generate_text(prompt: Prompt):
    payload = {
        "model": "openai-community/gpt2",
        "prompt": prompt.text,
        "max_tokens": 100,
        "temperature": 0.7
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        return {
            "error": "Hugging Face API error",
            "status_code": response.status_code,
            "details": response.text
        }

    data = response.json()
    return {
        "generated_text": data["choices"][0]["text"]
    }
