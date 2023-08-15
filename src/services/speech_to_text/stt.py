import ffmpeg
import tempfile
import speech_recognition as sr
import io
import numpy as np
from whispercpp import Whisper

def transcribe_audio(audio_data):
    w = Whisper.from_pretrained("tiny.en")
    temp = create_temp_file(audio_data)

    
    return w.transcribe_from_file(temp)

def create_temp_file(data):
    temp = tempfile.NamedTemporaryFile().name
    audio_data = sr.AudioData(data, 16000, 2)
    wav_data = io.BytesIO(audio_data.get_wav_data())
    with open(temp, "bx") as f:
        f.write(wav_data.read())

    return temp
        