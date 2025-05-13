import streamlit as st
import requests

st.title("Finance Assistant")

audio_input = st.file_uploader("Upload audio", type=["wav", "mp3"])

if st.button("Get Market Brief"):
    if audio_input is not None:
        response = requests.post("http://localhost:8000/market-brief", files={"audio_input": audio_input})
        st.audio("output.mp3")  # Play the audio response
        st.write(response.json())
    else:
        st.error("Please upload an audio file.")
