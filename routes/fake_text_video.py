from fastapi import APIRouter
from config import AUDIO_CACHE_BUCKET
from schema.converation import ChatRequest, LineRequest, Role
from services.storage import upload_audio_bytes
from services.tts import tts_to_bytes
from utils.audio import get_audio_duration_ms
import uuid

"""
- AUTOMATICALLY DELETE FOLDER IN AUDIO STORAGE
- GENERET MESSAGES
- ERROR HANDLING
"""

router = APIRouter(prefix="/fake-text-video")

@router.get("/messages")
def get_messages():
    pass

@router.post("/tts/batch") 
def post_tts_batch(request: ChatRequest):
    messages = request.messages
    sender_voice = request.voices.sender_voice
    receiver_voice = request.voices.receiver_voice

    folder = uuid.uuid4().hex

    response = []
    for index, message in enumerate(messages):
        voice = sender_voice if message.role == Role.SENDER else receiver_voice

        audio_bytes = tts_to_bytes(
            model="gpt-4o-mini-tts",
            voice=voice,
            text=message.text,
            instructions="Speak in the Najdi dialect",
        )

        public_url = upload_audio_bytes(
            bucket=AUDIO_CACHE_BUCKET,
            bytes=audio_bytes,
            index=index,
            folder=folder
        )

        duration_ms = get_audio_duration_ms(audio_bytes)
        response.append({"url": public_url, "duration": duration_ms})

    return response
    

@router.post("/tts/single")
def post_tts_single(request: LineRequest):
    text = request.text
    voice = request.voice

    folder = uuid.uuid4().hex

    audio_bytes = tts_to_bytes(
        model="gpt-4o-mini-tts",
        voice=voice,
        text=text,
        instructions="Speak in the Najdi dialect",
    )

    public_url = upload_audio_bytes(
        bucket=AUDIO_CACHE_BUCKET,
        bytes=audio_bytes,
        index=0,
        folder=folder
    )

    duration_ms = get_audio_duration_ms(audio_bytes)

    return {"url": public_url, "duration": duration_ms}
