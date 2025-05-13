import whisper
from gtts import gTTS
from langchain.chat_models import ChatOpenAI

model = whisper.load_model("base")

def speech_to_text(audio_file_path):
    result = model.transcribe(audio_file_path)
    return result["text"]

def process_transcription_with_llm(transcribed_text):
    llm = ChatOpenAI(temperature=0)
    prompt = f"Summarize the following market update: {transcribed_text}"
    response = llm.predict(prompt)
    return response

def text_to_speech(text, output_path="output.mp3"):
    tts = gTTS(text)
    tts.save(output_path)
    return output_path
