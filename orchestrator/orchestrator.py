from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import logging

from agents.voice_agent import speech_to_text, text_to_speech
from data_ingestion.api_agent import fetch_market_data
from agents.language_agent import generate_narrative

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/market-brief/audio")
async def market_brief_audio(symbol: str, audio_input: UploadFile = File(...)):
    logging.info("Received audio input")
    query = speech_to_text(audio_input.file)
    logging.info(f"Transcribed Query: {query}")
    market_data = fetch_market_data(symbol)
    narrative = generate_narrative(market_data)
    text_to_speech(narrative)
    logging.info("Narrative generated and spoken")
    return {"narrative": narrative}

class TextInputRequest(BaseModel):
    symbol: str
    query: str

@app.post("/market-brief/text")
async def market_brief_text(request: TextInputRequest):
    logging.info(f"Received text query: {request.query}")
    market_data = fetch_market_data(request.symbol)
    narrative = generate_narrative(market_data)
    text_to_speech(narrative)
    logging.info("Narrative generated and spoken")
    return {"narrative": narrative}
