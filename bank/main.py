from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "bank service running"}