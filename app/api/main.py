from fastapi import FastAPI

app = FastAPI(
    title="AI Recruitment Assistant"
)

@app.get("/")
def home():
    return {
        "message": "AI Recruitment Assistant API"
    }