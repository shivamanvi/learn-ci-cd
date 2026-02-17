# app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # return {"message": "CI/CD is working 🚀"}
    return {"message": "Broken CI"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
