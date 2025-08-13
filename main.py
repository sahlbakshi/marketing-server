from fastapi import FastAPI
from routes import fake_text_video

app = FastAPI()

app.include_router(fake_text_video.router)

@app.get("/")
def health():
    return {"message": "running"}
