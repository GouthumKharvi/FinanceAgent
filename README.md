# Finance Assistant

## Overview
The Finance Assistant is a multi-source, multi-agent finance assistant that delivers spoken market briefs. It integrates various data sources, processes audio input, and generates market summaries using advanced AI techniques. The application is built using FastAPI for the backend and Streamlit for the frontend.

## Project Structure
finance_assistant/ │ ├── data_ingestion/ │ ├── api_agent.py # Fetches market data from Alpha Vantage API │ ├── scraping_agent.py # Scrapes financial filings from websites │ ├── agents/ │ ├── retriever_agent.py # Handles embeddings and retrieval of data │ ├── language_agent.py # Generates narratives using language models │ ├── voice_agent.py # Processes speech-to-text and text-to-speech │ ├── orchestrator/ │ └── orchestrator.py # FastAPI application to orchestrate agents │ ├── streamlit_app/ │ └── app.py # Streamlit application for user interaction │ ├── docs/ │ └── ai_tool_usage.md # Documentation of AI tool usage │ ├── README.md # Project documentation ├── requirements.txt # Python dependencies └── Dockerfile # Docker configuration for deployment
