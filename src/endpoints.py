from fastapi import FastAPI, File, UploadFile
from src.services.llm import llm

app = FastAPI(
    prefix="/v1/api"
)

app.post("/chat")
def chat_completion(text: str):
    output = llm.generate_response(text)
    return output

