from config import supabase

def upload_audio_bytes(
    *,
    bucket: str,
    folder: str,
    index: str,
    bytes: bytes,
) -> str:
    
    key = f"{folder}/{index}.mp3"
    response = supabase.storage.from_(bucket).upload(
        key,
        bytes,
        {"content-type": "audio/mpeg", "upsert": "true"},
    )

    return supabase.storage.from_(bucket).get_public_url(key)
