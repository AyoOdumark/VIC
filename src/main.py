from fastapi import FastAPI, File, UploadFile
from src.services.llm import llm
from src.services.speech_to_text import stt

app = FastAPI(
    prefix="/v1/api"
)

@app.post("/chat")
def chat_completion(text: str):
    output = llm.generate_response(text)
    return output

@app.post("/transcribe")
def transcribe(file: UploadFile):
    print(file)
    # content = await file.read()
    # print(content)
    audio_data = file.file.read()
    transcription = stt.transcribe_audio(audio_data)
    return transcription



