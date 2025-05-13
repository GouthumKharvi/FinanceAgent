from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os

# Initialize the FastAPI app
app = FastAPI()

# Create a folder to store uploaded audio files
UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the directory exists

# Pydantic model for market-brief endpoint
class AudioInput(BaseModel):
    audio_input: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Finance Assistant API is running!"}

# Market brief endpoint (to be integrated with audio transcription)
@app.post("/market-brief")
async def market_brief(audio_input: AudioInput):
    return {"message": f"Market brief generated from audio: {audio_input.audio_input}"}

# Upload audio endpoint
@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        # Read the contents of the uploaded file
        contents = await file.read()
        print(f"Received file: {file.filename}, size: {len(contents)} bytes")  # Debugging line

        # Create full file path where it will be saved
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)

        # Save the uploaded file to the specified path
        with open(file_location, "wb") as f:
            f.write(contents)

        # Return a success message with file details
        return JSONResponse(
            content={
                "message": "File uploaded successfully",
                "filename": file.filename,
                "saved_to": file_location
            }
        )
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debugging line
        return JSONResponse(status_code=500, content={"message": str(e)})
