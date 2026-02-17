# app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CI/CD is working 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
