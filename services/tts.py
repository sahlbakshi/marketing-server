from io import BytesIO
from config import openai

"""
ERROR HANDLING NEEDED
"""

def tts_to_bytes(*, model: str, voice: str, text: str, instructions: str | None = None) -> bytes:
    buf = BytesIO()
    with openai.audio.speech.with_streaming_response.create(
        model=model,
        voice=voice,
        input=text,
        instructions=instructions,
    ) as response:
        for chunk in response.iter_bytes():
            buf.write(chunk)
    return buf.getvalue()
