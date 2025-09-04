from fastapi import FastAPI
from routes import fake_text_video
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "https://marketing-client-three.vercel.app"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fake_text_video.router)

@app.get("/")
def health():
    return {"message": "running"}
