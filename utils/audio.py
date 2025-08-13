import io
from mutagen.mp3 import MP3

def get_audio_duration_ms(audio_bytes: bytes) -> int:
    f = io.BytesIO(audio_bytes)
    return int(MP3(f).info.length * 1000)
    