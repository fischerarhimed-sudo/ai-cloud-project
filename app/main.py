from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="AI Text Generator")

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate_text(prompt: Prompt):
    response = requests.post(
        MODEL_URL,
        headers=headers,
        json={"inputs": prompt.text}
    )

    if response.status_code != 200:
        return {"error": response.text}

    return response.json()
