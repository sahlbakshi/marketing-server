from fastapi import APIRouter
from config import AUDIO_CACHE_BUCKET
from schema.chat import ChatRequest, LineRequest, MultilingualChat, MessageAudio
from services.supabase import upload_audio_bytes
from services.openai import tts_to_bytes, generate_chat
from utils.audio import get_audio_duration_ms
from utils.prompts import fake_text_video_prompt
import uuid

router = APIRouter(prefix="/fake-text-video")

@router.get("/messages", response_model=MultilingualChat)
def get_messages(sentiment: str = "normal", num_messages: int = 8):
    chat = generate_chat(
        model='gpt-4.1',
        prompts=fake_text_video_prompt(sentiment, num_messages),
        schema=MultilingualChat
    )
    return chat

@router.post("/tts/batch", response_model=list[MessageAudio])
def post_tts_batch(request: ChatRequest):
    messages = request.messages
    sender_voice = request.sender_voice
    receiver_voice = request.receiver_voice

    folder = uuid.uuid4().hex

    response = []
    for index, message in enumerate(messages):
        voice = sender_voice if message.role == 'sender' else receiver_voice

        audio_bytes = tts_to_bytes(
            model="gpt-4o-mini-tts",
            voice=voice,
            text=message.text,
            instructions="Speak in a conversational Najdi arabic dialect",
        )

        public_url = upload_audio_bytes(
            bucket=AUDIO_CACHE_BUCKET,
            bytes=audio_bytes,
            index=index,
            folder=folder
        )

        duration_ms = get_audio_duration_ms(audio_bytes)
        response.append(MessageAudio(url=public_url, duration_ms=duration_ms))

    return response
    

@router.post("/tts/single", response_model=MessageAudio) 
def post_tts_single(request: LineRequest):
    text = request.text
    voice = request.voice

    folder = uuid.uuid4().hex

    audio_bytes = tts_to_bytes(
        model="gpt-4o-mini-tts",
        voice=voice,
        text=text,
        instructions="Speak in a conversational Najdi arabic dialect",
    )

    public_url = upload_audio_bytes(
        bucket=AUDIO_CACHE_BUCKET,
        bytes=audio_bytes,
        index=0,
        folder=folder
    )

    duration_ms = get_audio_duration_ms(audio_bytes)

    return MessageAudio(url=public_url, duration_ms=duration_ms)
