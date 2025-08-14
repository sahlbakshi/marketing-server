from io import BytesIO
from mutagen.mp3 import MP3

def get_audio_duration_ms(audio_bytes: bytes) -> int:
    f = BytesIO(audio_bytes)
    return int(MP3(f).info.length * 1000)
    