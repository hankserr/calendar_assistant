#!/bin/zsh
# Run the FastAPI app
source venv/bin/activate
uvicorn app.main:app --reload
