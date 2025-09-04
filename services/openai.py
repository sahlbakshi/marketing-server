from io import BytesIO
from config import openai
from schema.chat import MultilingualChat

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


def generate_chat(*, model: str, prompts: tuple[str, str], schema: dict) -> MultilingualChat:
    system_prompt, user_prompt = prompts

    response = openai.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        text_format=schema,
        temperature=1.2
    )
    
    return response.output_parsed
